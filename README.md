# streamlit_application


모바일 이용자 특성 이라는 데이터를 이용하여<br/>
사용자에게 정보를 입력받아<br/>
사용자가 사용하는 어플리케이션을 예측하려한다<br/><br/>

[링크](https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=9f027c94-92fd-4eeb-bf1c-7532f9c8375e, "문화 빅데이터 플랫폼")<br/>  
에서 데이터를 내려받았으며  202305,202311 버전이 두개가 중복데이터가 없는 다른 데이터였기때문에<br/>
병합시킨뒤 필요없는 데이터는 삭제 후 NaN이 있나 검색하였고<br/>
문자열 데이터 처리중<br/>
월소득 부분에서 '모름'이 나와서 해당 데이터를 NaN으로 처리후 삭제 함<br/><br/>


model.pkl의 데이터 사이즈가 100mb를 초과하여<br/>
model.zip으로 압축하여<br/>
압축해제 코드 추가 작성함<br/>


