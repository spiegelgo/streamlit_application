
import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def run_eda():
    st.subheader('탐색적 데이터 분석')
    st.text('데이터프레임과 통계치를 확인가능합니다.')
    
    radio_menu = ['데이터프레임','통계치']
    
    choice_radio = st.radio('선택하세요.', radio_menu)
    df = pd.read_csv('./data/Changed_Mobile._csv')
    df = df.drop(columns=['Unnamed: 0'])
    if choice_radio == radio_menu[0] :
        st.dataframe(df)
    
    elif choice_radio == radio_menu[1]:
        st.dataframe(df.describe(include='object'))
        st.dataframe(df.describe())
    # 각각의 어플리케이션 사용인원 
    st.subheader('각각의 어플리케이션 사용인원 상황입니다.')
    '''# "Y"를 1로, "N"을 0으로 바꾸기
    df_numeric = df.iloc[:, :17+1].apply(lambda col: col.str.count('Y'))

    # 합산하여 결과 출력
    sum_result = df_numeric.sum()
    st.dataframe(sum_result)'''
    df_numeric = df.iloc[:, :17+1].apply(lambda col: col.str.count('Y'))

    # 합산하여 결과 출력
    sum_result = df_numeric.sum()

    # 사용률 계산
    usage_rate = (sum_result / 64024 * 100).round(2)

    # 사용률을 데이터프레임에 추가
    sum_result = sum_result.to_frame(name='사용인원')
    sum_result['사용률'] = usage_rate.apply(lambda x: f"{x:.1f}%")

    # 결과 출력
    st.dataframe(sum_result)
    
    # 각 컬럼별로 카테고리컬 데이터를 따로 보여주는 화면 개발
    
    st.subheader('카테고리를 선택하면 각각의 데이터를 보여드립니다.')

    categories = ['성별', '나이', '결혼', '월_소득', '거주지역']

    # 사용자가 선택한 카테고리
    selected_category = st.selectbox('카테고리 선택', categories)

    # 카테고리에 따라 데이터 그룹화
    grouped_data = df.groupby(selected_category)

    # 각 그룹별 데이터 출력
    for group_name, group_data in grouped_data:
        st.subheader(f'{selected_category}: {group_name}')
        st.write(group_data)
    
