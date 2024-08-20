
import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px

def run_eda():
    
    # 한글 폰트 설정
    import platform
    from matplotlib import font_manager, rc
    plt.rcParams['axes.unicode_minus'] = False
    if platform.system() == 'Linux':
        rc('font', family='NanumGothic')
    
    # 캐시 비우기 버튼
    if st.button('캐시 비우기'):
        st.legacy_caching.clear_cache()
        st.success('캐시가 성공적으로 비워졌습니다.')    
    
    st.subheader('탐색적 데이터 분석')
    st.markdown('데이터프레임과 통계치를 확인가능합니다.')
    
    radio_menu = ['데이터프레임','통계치']
    
    choice_radio = st.radio('선택하세요.', radio_menu)
    df = pd.read_csv('./data/Changed_Mobile.csv')
    df = df.drop(columns=['Unnamed: 0'])
    if choice_radio == radio_menu[0] :
        st.info(f'전체 데이터의 갯수는 {df.shape}')
        st.markdown('Y, N은 해당 어플리케이션의 사용여부를 나타내고 Y는 사용함, N은 사용 하지않음을 의미')
        st.markdown('월_소득 부분의 단위는 만원 이며 100만원 미만은 100만원과 통일')
        st.markdown('1,000만원 이상은 1,000만원과 통일 시켰음')
        st.dataframe(df)

    
    elif choice_radio == radio_menu[1]:
        df_des = df.copy()
        df_des['나이'] = df_des['나이'].str.replace('이상','')
        df_des['나이'] = df_des['나이'].str.replace('대','')
        df_des['나이'] = df_des['나이'].astype(int)
        st.dataframe(df_des.describe(include='object'))
        st.dataframe(df_des.describe())
    # 각각의 어플리케이션 사용인원 
    st.subheader('각각의 어플리케이션 사용인원 상황입니다.')

    df_numeric = df.iloc[:, :17+1].apply(lambda col: col.str.count('Y')) # 콜럼별 Y갯수 카운트
    sum_result = df_numeric.sum()                                        # 각각의 사용인원 체크
    usage_rate = (sum_result / 64024 * 100).round(2)                     # 사용률 계산
    sum_result = sum_result.to_frame(name='사용인원')                     # 각각의 사용인원 데이터프레임으로 변환
    sum_result['사용률'] = usage_rate.apply(lambda x: f"{x:.1f}%")        # 사용률 데이터프레임에 추가

    st.dataframe(sum_result)
    
    # 각 컬럼별로 카테고리컬 데이터
    
    st.subheader('카테고리를 선택하면 각각의 데이터를 보여드립니다.')

    categories = ['성별', '나이', '결혼', '월_소득', '거주지역']
    selected_category = st.selectbox('카테고리 선택', categories)

    # 카테고리에 따라 데이터 그룹화
    grouped_data = df.groupby(selected_category)

    # 각 그룹별 데이터 출력
    for group_name, group_data in grouped_data:
        st.subheader(f'{selected_category}: {group_name} 의 데이터프레임')
        st.write(group_data)
        num_rows = group_data.shape[0]
        st.info(f'{selected_category}: {group_name} 그룹의 인원 수 : {num_rows: ,} 명')
        
        binary_columns = ['K-POP_아이돌', '게임', '사진_촬영', '방송_영상', '웹툰', '검색_포털', '금융', '예매', '여행', '음식_주문', '맛집_추천_예약', '쇼핑', '헬스', '전자지갑', '청소_가사노동', '부동산', '병원_약국_의약품_검색', '중고거래']
        for col in binary_columns:
            df[col] = df[col].map({'Y': 1, 'N': 0})


        # 선택한 카테고리의 데이터프레임에서 'K-POP_아이돌'부터 '중고거래'까지의 열을 추출
        selected_df = group_data[binary_columns].apply(lambda x: x.map({'Y': 1, 'N': 0}))


        # bar 차트 그리기
        bar_data = selected_df.sum().sort_values(ascending=False)
        fig_bar = px.bar(x=bar_data.index, y=bar_data.values, title=f'{selected_category}: {group_name} 의 어플 사용인원수')
        fig_bar.update_xaxes(tickangle=320)
        st.plotly_chart(fig_bar)
        
        # pie 차트 그리기
        fig_pie = px.pie(values=bar_data.values, names=bar_data.index, title=f'{selected_category}: {group_name} 의 어플 사용 비율', hole = 0.2)
        st.plotly_chart(fig_pie)
        
