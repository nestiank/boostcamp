# Day02 (2022/01/18)

## 노트

### 확률분포 추정

데이터의 분포를 확인해서 확률분포를 추정한다면 이를 검정해야 한다.

정규분포의 모수에서 표본 분산은 불편추정량으로 구하게 되고, 따라서 자유도가 개입한다.

유효추정량의 관점에서, 추정량의 분산이 작을 수록 그 추정량은 더 유효하다. 그것은 분산이 클 수록 MSE가 커지기 때문이다.

### MLE

머신러닝에서, 정규분포의 MLE는 확률밀도함수를 평균과 표준편차에 대해 미분해서 할 수 있고, 카테고리 분포의 MLE는 표본별 확률의 곱을 확률 벡터에 대해 미분해서 할 수 있다. 이때 라그랑주 승수법을 사용한다.

딥러닝에서, 모델의 MLE는 정답 레이블인 경우의 MLP 결과값들의 곱을 가중치들로 미분해서 할 수 있다. 여기에는 연쇄법칙이 적용되기 때문에 역전파를 이용하면 미분 작업을 크게 줄일 수 있다.

보통 미분해야 하는 값에 로그를 취한다. 이는 시간복잡도를 줄여 주고, 계산의 지수 단위를 보다 현실적으로 만들어 준다.

### KL-Divergence

추정 확률분포와 실제 확률분포 사이의 KL 발산을 최소화하는 것은 MLE와 같다. 이는 엔트로피와 크로스 엔트로피가 가까워져 두 확률분포가 거의 같은 정보량을 가지게 되는 것을 의미한다.

목표는 크로스 엔트로피가 작아지는 것이 아니다. 분포에 따라 크로스 엔트로피가 작아지는 것의 의미는 예측 결과가 점차 한쪽으로 쏠린다는 것일 수도 있고, 점차 균형 있게 나뉜다는 것일 수도 있고, 둘 다 아닐 수도 있다.

## 일지

### Daily scrum (10:00-10:20)

### 어제의 daily report 보충 (10:20-10:40)

### 강의 영상 수강 및 과제 수행 (10:40-12:00)

  * [강의] Python Basics for AI
    * Python Variables
  * [과제] Python Basics for AI & AI Math
    * Gradient Descent

### 강의 영상 수강 및 과제 제출 (13:00-16:00)

  * [강의] Python Basics for AI
    * Python OOP
    * Python Module & Project
    * Python File & Exception & Log Handling
    * Python Data Handling
    * numpy
    * pandas I/II
  * [과제] Python Basics for AI
    * Basic Math
    * Text Processing I/II
  * [과제] Python Basics for AI & AI Math
    * Gradient Descent

### Peer session (16:00-17:00)

  * Ground Rule 발표 준비
  * 심화과제 #1 이야기
  * AI Math 강의 이야기
  * 대학원 연구실 관련 이야기
  * 멘토링에서 물어볼 질문 준비
  * 다음 peer session 준비
    * AI Math 8강까지 듣고 오기
    * AI Math 8강까지 퀴즈 풀고 오기
    * 심화과제 #3 확인하고 오기

### 강의 영상 수강 및 퀴즈 제출 (17:00-19:00)

  * [강의] AI Math
    * 확률론
    * 통계학
  * [퀴즈] AI Math
    * 확률론
    * 통계학

### Mentoring (19:00-19:50)

  * 멘토님 소개
  * 앞으로 멘토링에서 할 일 소개
  * 취업 관련 이야기
  * 연구 관련 이야기

### Daily report 작성 (19:50-20:30)
