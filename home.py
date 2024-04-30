
import streamlit as st

def run_home() :
    st.subheader('당신은 어떤 어플리케이션을 사용하나요?')
    st.text('재미삼아 해봅시다')
    st.text('데이터는 문화 빅데이터 플랫폼 이라는 사이트에서 내려받았으며')
    st.text("'컨슈머인사이트'에서 제공한")
    st.text('모바일 어플리케이션 이용자 특성(202305).csv 와')
    st.text('모바일 어플리케이션 이용자 특성(202311).csv 로 만들어졌습니다')
    st.link_button('해당 사이트로 연결됩니다','https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=9f027c94-92fd-4eeb-bf1c-7532f9c8375e')
    st.image('./img/hand.jpg')
    