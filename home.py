
import streamlit as st

def run_home() :
    st.subheader('당신은 어떤 어플리케이션을 사용하나요?')
    st.text('재미삼아 해봅시다')
    st.text('데이터는 문화 빅데이터 플랫폼 이라는 사이트에서 내려받았으며')
    st.text("'컨슈머인사이트'에서 제공한")
    st.text('모바일 어플리케이션 이용자 특성(202305).csv 와')
    st.text('모바일 어플리케이션 이용자 특성(202311).csv 로 만들어졌습니다')
    st.link_button('해당 사이트로 연결됩니다','https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=9f027c94-92fd-4eeb-bf1c-7532f9c8375e')
    
 #   - 모바일 어플리케이션은 총 18개 분류로 뮤직/공연/아이돌, 게임, 카메라, 방송/동영상, 만화/웹툰, 금융, 티켓 예매, 여행, 음식 주문/배달, 맛집 추천/예약, 쇼핑, 헬스케어, 전자지갑, 청소/가사/시터, 부동산 중개, 동네 병원/약국 찾기, 중고거래로 나뉨.
#- 본 데이터 셋에는 응답자 특성(성별, 연령대, 거주지역, 소득수준 등)이 포함됨.
    st.image('./img/hand.jpg')
    