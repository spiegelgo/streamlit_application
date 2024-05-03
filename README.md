# streamlit_application


모바일 이용자 특성 이라는 데이터를 이용하여<br/>
사용자에게 정보를 입력받아<br/>
사용자가 사용하는 어플리케이션을 예측하려한다<br/><br/>

[링크](https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=9f027c94-92fd-4eeb-bf1c-7532f9c8375e, "문화 빅데이터 플랫폼")<br/>  
에서 데이터를 내려받았으며  202305,202311 버전이 두개가 중복데이터가 없는 다른 데이터였기때문에<br/>
병합시킨뒤 필요없는 데이터는 삭제 후 NaN이 있나 검색하였고<br/>
문자열 데이터 처리중<br/>
월소득 부분에서 '모름'이 나와서 해당 데이터를 NaN으로 처리후 삭제 함<br/><br/>

성별은 레이블인코딩<br/>
나이와 월소득은 그대로 두고<br/>
결혼여부와 지역은 원-핫 인코딩하여<br/>
랜덤포레스트 클래시파이어로 모델을 만들어 진행하였음<br/><br/>


model.pkl의 데이터 사이즈가 100mb를 초과하여<br/>
model.zip으로 압축하여<br/>
압축해제 코드 추가 작성함<br/><br/>

EDA페이지에서 먼저 데이터프레임과 describe를<br/>
라디오버튼으로 선택하여 볼수 있게 만들었음<br/><br/>

각각의 어플리케이션의 사용인원과 사용률을 보여줌<br/><br/>

성별,나이,결혼,월소득,거주지역등 을 선택하면<br/>
각각의 카테고리별 사용하는 어플들의 목록을 보여줌<br/><br/>

ML페이지에서는 이제 유저의 정보<br/>
즉, 성별, 나이, 결혼 여부, 월소득, 거주지역등을 입력받아<br/>
입력받은 버튼을 누르면 결과값으로 어떤 어플리케이션을 사용할지 예측하고<br/>
예측한 결과물을 각각의 퍼센트와 함께 유저에게 보여줌<br/>



