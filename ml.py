import streamlit as st
import joblib
import numpy as np
import pandas as pd
import zipfile
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import plotly.express as px
import matplotlib.pyplot as plt


def run_ml():
    # 한글 폰트 설정
    import platform
    from matplotlib import font_manager, rc
    plt.rcParams['axes.unicode_minus'] = False
    if platform.system() == 'Linux':
        rc('font', family='NanumGothic')
    st.subheader('사용하는 어플 예측하기')
    


    # 사용자 입력 받기
    GENDER = st.radio('성별 선택', ['남자','여자'])
    AGE = st.number_input('나이', min_value=10, max_value=120,value= 30, step=1)
    MARRIAGE = st.radio('결혼 여부', ['미혼 / 비혼','기혼','기타(이혼, 사별 등)'])
    INCOME = st.number_input('월 소득을 입력해주세요, 단위는 만원', min_value=100, max_value=50000, value= 250, step=50)
    AREA = st.radio('주거지역을 선택하세요', ['서울', '경기', '인천', '충남', '경남',
                                                '부산', '대구', '울산', '광주', '경북', '전북', 
                                                '세종', '제주', '강원', '대전', '충북', '전남'])
    
    if GENDER == '남자':
        GENDER = 'M'
    elif GENDER == '여자':
        GENDER = 'F'
    # 입력데이터 레이블 인코딩    
    X_label_encoder = joblib.load('./model/X_label_encoder.pkl')
    GENDER = X_label_encoder.transform([GENDER])[0]
    # 사용자 입력 데이터를 DataFrame으로 변환
    new_data = pd.DataFrame({'성별': [GENDER], '나이': [AGE], '결혼': [MARRIAGE], '월_소득': [INCOME], '거주지역': [AREA] })
    

 
    st.subheader('버튼을 누르면 예측합니다.')
    
    if st.button('예측하기') :

        # 데이터 타입 변환
        new_data['성별'] = new_data['성별'].astype(int)
        new_data['결혼'] = new_data['결혼'].astype(str)
        new_data['월_소득'] = new_data['월_소득'].astype(int)
        new_data['나이'] = new_data['나이'].astype(int)
        new_data['거주지역'] = new_data['거주지역'].astype(str)

        # 디버깅: 데이터 타입과 내용 확인
        st.write("new_data 데이터 타입:")
        st.write(new_data.dtypes)

        # 입력데이터 원-핫인코딩
        st.dataframe(new_data)
        ct = joblib.load('./model/ct.pkl')
        st.write(type(ct))
        st.write(ct)

        if not isinstance(ct, ColumnTransformer):
            st.error("ct가 ColumnTransformer 객체가 아닙니다.")
            return

        # # OneHotEncoder 개별 확인
        # for name, transformer, columns in ct.transformers:
        #     if name == 'onehot':
        #         st.write(f"OneHotEncoder 대상 컬럼: {columns}")
        #         ohe = transformer
        #         try:
        #             encoded_sample = ohe.transform(new_data[columns])
        #             st.write("OneHotEncoder 테스트 인코딩 결과:")
        #             st.write(encoded_sample)
        #         except Exception as e:
        #             st.error(f"OneHotEncoder 에러: {e}")
        #             return

        try:
            encoded_features = ct.transform(new_data)
            st.write(encoded_features)
        except Exception as e:
            st.error(f"ct.transform 에러: {e}")
            return
        # 모델에 예측할 데이터 전달
        X_new = encoded_features.toarray()
        st.write(X_new)
        # 2. 예측한다
        # 2-1. 모델이 있어야 한다
        file = zipfile.ZipFile('./model/model.zip')
        file.extractall('./model')
        model = joblib.load('./model/model.pkl')
        #print(model)
        # 2-2. 유저가 입력한 데이터를 모델이 예측하기 위해 가공해야 한다
        
        # 2-3. 모델의 predict 함수로 예측한다
        y_pred = model.predict_proba(X_new)
        #print(y_pred)
        df = pd.read_csv('./data/Changed_Mobile.csv')
        df.drop('Unnamed: 0',axis=1,inplace=True)

        
        # 각 컬럼 이름과 예측 확률을 저장할 리스트
        # column_names = df.columns[0:17+1]
        # result_str = ""
        probabilities = []

        # 각 컬럼의 이름과 예측 확률을 추출하여 리스트에 저장
        for i, pred in enumerate(y_pred):
            prob = round(pred[0][0] * 100, 2)  # 소수점 2번째 자리까지 반올림
            col_name = df.columns[i]  # 콜럼 이름 가져오기
            probabilities.append((col_name, prob))

        # Bar 차트 그리기
        probabilities.sort(key=lambda x: x[1], reverse=False)  # 확률에 따라 내림차순 정렬
        fig_bar = px.bar(x=[p[1] for p in probabilities], y=[p[0] for p in probabilities], orientation='h',
                        labels={'x': '확률 (%)', 'y': '어플'}, title='각 어플 사용 확률')
        st.plotly_chart(fig_bar)

        # 행의 개수와 열의 개수 설정
        n_rows = 6
        n_cols = 3

        # Pie 차트를 subplot으로 그리기
        fig, axs = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(9, 15))


        # 확률을 기준으로 내림차순으로 정렬
        probabilities.sort(key=lambda x: x[1], reverse=True)

        # Pie 차트 그리기
        for i, (col_name, prob) in enumerate(probabilities):
            row = i // n_cols  # 현재 인덱스의 행 번호
            col = i % n_cols   # 현재 인덱스의 열 번호
            if row < n_rows and col < n_cols:  # 행과 열이 범위 내에 있는지 확인
                axs[row, col].pie([prob, 100 - prob], labels=[f'사용확률: {prob}%',  '사용안함'], autopct='%1.2f%%', startangle=90)
                axs[row, col].set_title(f'{col_name} 어플 사용 확률')


        plt.tight_layout()
        st.pyplot(fig)


        # 각 어플의 예측 확률 정보 출력
        for col_name, prob in probabilities:
            st.info(f"당신이 '{col_name}' 관련 어플을 사용할 확률은 {prob}% 입니다.")


