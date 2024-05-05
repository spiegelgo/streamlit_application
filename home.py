
import streamlit as st

def run_home() :
    st.subheader('당신은 어떤 어플리케이션을 사용하나요?')
    st.markdown('재미삼아 해봅시다')
    st.markdown("#### 데이터는 '문화 빅데이터 플랫폼' 에서 내려받았으며")
    st.markdown("'컨슈머인사이트'에서 제공한")
    st.markdown('모바일 어플리케이션 이용자 특성(202305).csv 와')
    st.markdown('모바일 어플리케이션 이용자 특성(202311).csv 로 만들어졌습니다')
    st.link_button('해당 사이트로 연결됩니다','https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=9f027c94-92fd-4eeb-bf1c-7532f9c8375e')
    
    st.markdown('#### 분야별 모바일 어플리케이션 1개월 내 경험 유무에 대한 데이터')
    st.markdown('### 모바일 어플리케이션은 총 18개 분류로')
    st.markdown('##### 뮤직/공연/아이돌, 게임, 카메라, 방송/동영상, 만화/웹툰, 금융, 티켓 예매, 여행, 음식 주문/배달, 맛집 추천/예약, 쇼핑, 헬스케어, 전자지갑, 청소/가사/시터, 부동산 중개, 동네 병원/약국 찾기, 중고거래로 나뉨.')
    st.markdown('응답자 특성으로는 (성별, 연령대, 거주지역, 소득수준 등)이 포함됨.')

    st.markdown('### 예측되는 데이터 활용.')
    st.markdown(' 시의성 있는 이동통신 데이터 확보를 통해 목표 집단 세분화 및 타겟 집단 선정 등 마케팅 커뮤니케이션에 활용.')
    st.image('./img/hand.jpg')
    