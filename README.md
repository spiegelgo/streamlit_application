# streamlit_application

## 🎇기획의도🎇
모바일 이용자 특성 이라는 데이터를 이용하여<br/>
**사용자에게 정보를 입력**받아<br/>
**사용자가 사용하는 어플리케이션**을 **예측**하려한다<br/>
- - - - - - - - - 

## 🎉데이터셋 정보🎉
[문화 빅데이터 플랫폼](https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=9f027c94-92fd-4eeb-bf1c-7532f9c8375e, "문화 빅데이터 플랫폼")에서 데이터를 내려받았으며 <br/>  
202305,202311 버전 2개가 **중복데이터가 없는 데이터**였기때문에<br/>
**병합**시킨뒤 필요없는 데이터는 삭제 후 NaN이 있나 검색하였고 없는것을 확인했으나<br/>
문자열 데이터 처리중<br/>
월소득 부분 데이터 중 **모름**이 나와서 **해당 데이터를 NaN으로 처리후 삭제** 함<br/>
- - - - - - - - - - - - - - - - - - 

## 🏃‍♂️To Do List 작성🏃‍♂️
1. *X가 되는 데이터들은 추후에 유저에게 정보를 입력받을 데이터들*<br/>
2. *y가 되는 데이터들은 예측 하려하는 것*<br/>
3. *X와 y의 인코딩*<br/>
4. *모델 생성 및 예측*<br/>
5. *유저에게 입력받아 새로운 예측하기*<br/>
- - - - - - - - - - - - - - - - - - 
## ✌개발과정✌
+ **1. X 지정**<br/>
    + 성별, 나이, 결혼여부, 월소득, 지역 선택<br/><br/>

+ **2. y 지정**<br/>
    + 나머지 어플리케이션 컬럼 전부 선택<br/><br/>

+ **3. 인 코 딩**<br/>
    + 우선적으로 y인 어플리케이션들은 전부 값이 Y와 N뿐이었기에 바로 **레이블인코딩** 진행하였고<br/>
    + X 부터가 문제가 되었는데 **성별**은 **레이블인코딩**,<br/>
    + 나이와 월소득은 **문자열**을 **정수**로 **변환**,<br/>
    + **결혼여부**와 **지역**은 **원-핫 인코딩**하였고<br/>
    + 이때 0의 행렬이라고 불러도 좋을 희소행렬이 되었다<br/><br/>

+ **4. 모델생성 및 예측**<br/>
    + **다중 이진 분류** 문제다 보니 의사결정트리 보다 효과가 좋다고 판단되는 **랜덤포레스트 클래시파이어** 모델을 만들어 진행하였음<br/><br/>

+ **5. 유저에게 입력받아 예측**
    + 아무 문제 없이 잘 작동하는것을 확인<br/>
    + **각각의 확률**을 **텍스트**로 띄워 보여주는것으로 하였다<br/>
    + 테스트과정중 각각의 확률을 **bar차트**와 **pie차트**로 볼 수 있으면 좋겠다는 생각이 들어 **추가**함<br/><br/>

+ **6. 데이터설명**
    + 데이터에 대해 안내하는 페이지를 추가하기로 결정<br/>
    + 데이터 페이지에서 **전체 데이터프레임**과<br/>
    + **통계치**를 **라디오버튼**으로 **확인 가능**하게끔 진행<br/>
    + 대부분의 데이터가 Y/N인데 나이와 월소득의 정수타입때문에 보기 어려운 모습이 연출되어<br/>
    + **통계치**를 **문자열**과 **정수**타입을 **따로** 볼 수 있도록 진행함<br/>
    + 각각의 어플리케이션 **사용인원**과 **백분율**로도 확인 가능케 진행<br/>
    + 예측에 필요한 정보들 = **카테고리컬 데이터**들을 **선택**하면 **그룹별 인원수**와 **데이터프레임**,<br/>
    + 각각 어떤 어플리케이션을 사용하는지 보여주는 **각각의 bar차트**와 **pie차트 확인 가능**케 진행<br/>
- - - - - - - - - 

## ✔테스트과정 및 문제점 개선✔
로컬에서 진행당시에는 문제가 없었으나<br/>
깃허브에 올리려고보니<br/>
model.pkl의 **데이터 사이즈가 100mb를 초과**하여 깃허브에 올릴 수 없어<br/>
model.zip으로 **압축**하여<br/>
**압축해제** 코드 **추가 작성**함<br/><br/>

그후 EC2 서버에서 테스트하던 중<br/>
아무래도 모델 사이즈가 사이즈라서인지<br/>
**AWS 프리티어**의 **메모리**가 감당하지못하여 **서버**가 **터져버리는 상황**이 발견됨<br/>
**Swap memory**를 2GB 설정하여 일단 급한 불을 꺼놓긴 하였지만<br/>
아무래도 가상메모리라 속도가 시원시원하지는 못함<br/>
물론 **결제** 한다면 **해결**되는 상황이니 큰 문제는 아니라고 판단됨<br/>
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
## 🎈결과🎈
💕💕[만들어진 웹 사이트](http://ec2-3-39-248-200.ap-northeast-2.compute.amazonaws.com:8504/)💕💕<br/>