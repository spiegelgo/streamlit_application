import streamlit as st
import joblib
import numpy as np
import pandas as pd
import zipfile
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def run_ml():
    st.subheader('사용하는 어플 예측하기')
    
    # ct.pkl 파일 로드
    ct = joblib.load('./model/ct.pkl')

    # 사용자 입력 받기
    GENDER = st.radio('성별 선택', ['남자','여자'])
    AGE = st.number_input('나이', min_value=10, max_value=120,value= 20, step=1)
    MARRIAGE = st.radio('결혼 여부', ['미혼 / 비혼','기혼','기타(이혼, 사별 등)'])
    INCOME = st.number_input('월 소득을 입력해주세요, 단위는 만원', min_value=100, max_value=50000, value= 200, step=50)
    AREA = st.radio('주거지역을 선택하세요', ['서울', '경기', '인천', '충남', '경남',
                                                '부산', '대구', '울산', '광주', '경북', '전북', 
                                                '세종', '제주', '강원', '대전', '충북', '전남'])
    
    if GENDER == '남자':
        GENDER = 'M'
    elif GENDER == '여자':
        GENDER = 'F'
    
    X_label_encoder = joblib.load('./model/X_label_encoder.pkl')
    GENDER = X_label_encoder.transform([GENDER])[0]
    # 사용자 입력 데이터를 DataFrame으로 변환
    new_data = pd.DataFrame({'성별': [GENDER], '나이': [AGE], '결혼': [MARRIAGE], '월_소득': [INCOME], '거주지역': [AREA] })

    # ColumnTransformer를 사용하여 원-핫 인코딩 수행
    encoded_features = ct.transform(new_data)

    # 모델에 예측할 데이터 전달
    X_new = encoded_features.toarray()
 
    st.subheader('버튼을 누르면 예측합니다.')
    
    if st.button('예측하기') :
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
        df = pd.read_csv('./data/Changed_Mobile._csv')
        df.drop('Unnamed: 0',axis=1,inplace=True)
        column_names = df.columns[0:17+1]
        result_str = ""
        
        for i, pred in enumerate(y_pred):
            prob = pred[0][0] * 100  # 앞의 값만 가져와서 *100
            prob = round(prob, 2)  # 소수점 2째 자리까지 반올림
            col_name = df.columns[i]  # 콜럼 이름 가져오기
            st.info(f"당신이 '{col_name}' 관련 어플을 사용할 확률은 {prob}% 입니다.")




