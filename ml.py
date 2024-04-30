import streamlit as st
import joblib
import numpy as np
import pandas as pd

def run_ml():
    st.subheader('사용하는 어플 예측하기')
    
    # 1. 예측하기 위해, 유저한테 입력 받는다
    # Gender AGE MARRIAGE INCOME AREA
    
    st.text('성별을 선택하세요')
    GENDER = st.radio('성별 선택', ['남자','여자'])
    if GENDER =='남자':
        GENDER = 1
    elif GENDER == '여자' :
        GENDER = 0
    
    
    st.text('나이를 입력하세요')
    AGE = st.number_input('나이', min_value=10, max_value=120,value= 20, step=1)
    

        
    st.text('결혼 여부를 선택하세요')
    MARRIAGE = st.radio('결혼 여부', ['미혼 / 비혼','기혼','기타(이혼, 사별 등)'])
    if MARRIAGE =='기타(이혼, 사별 등)':
        MARRIAGE = 0
    elif MARRIAGE == '기혼' :
        MARRIAGE = 1
    elif MARRIAGE == '미혼 / 비혼' :
        MARRIAGE = 2
    
    
    st.text('월 소득')

    INCOME = st.number_input('월 소득을 입력해주세요, 단위는 만원', min_value=100, max_value=50000, value= 200, step=50)
     
       
    
    st.text('주거 지역')
    def label_encode_area(selected_area):
        area_list = ['서울', '경기', '인천', '충남', '경남', '부산', '대구', '울산', '광주',
                     '경북', '전북', '세종', '제주', '강원', '대전', '충북', '전남']
        return area_list.index(selected_area)
    selected_area = st.radio('주거지역을 선택하세요', ['서울', '경기', '인천', '충남', '경남',
                                             '부산', '대구', '울산', '광주', '경북', '전북', 
                                             '세종', '제주', '강원', '대전', '충북', '전남'])
    AREA = label_encode_area(selected_area)
    
    
    
    st.subheader('버튼을 누르면 예측합니다.')
    
    if st.button('예측하기') :
        # 2. 예측한다
        # 2-1. 모델이 있어야 한다
        model = joblib.load('./model/model.pkl')
        #print(model)
        # 2-2. 유저가 입력한 데이터를 모델이 예측하기 위해 가공해야 한다
        data = [GENDER] + [AGE] + [MARRIAGE] + [INCOME] + [AREA]
        #print(data) 

        new_data = []
        for item in data:
            if isinstance(item, list):
                new_data.extend(item)
            else:
                new_data.append(item)

        new_data = np.array(new_data).reshape(1, -1)
        new_data = np.array([data])
        #print(new_data)

        
        # 2-3. 모델의 predict 함수로 예측한다
        y_pred = model.predict_proba(new_data)
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




