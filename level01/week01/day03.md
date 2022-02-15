# Day03 (2022/01/19)

## 노트

### MAP

> https://enfow.github.io/study/statistics/2020/03/04/mle_map <br>
> (https://archive.is/RVqVb)

베이즈 정리를 이용하여 MLE보다 정확한 추정을 할 수 있다. 베이즈 정리에서 등장하는 개념들이 매우 혼란스러운데, 정리하면 다음과 같다.

  * Likelihood: 모델의 추정 확률밀도함수를 이용하여 표본별로 그 결과가 나올 확률을 구해 모두 곱한 값
  * Prior: 모델의 가능한 확률밀도함수들 중 추정 확률밀도함수가 참일 확률
  * Posterior: 이들의 곱

일단 posterior 값은 prior 값과 likelihood 값의 사이에 위치한다.

위처럼 정의한다면 prior 값은 확정되지 않고 확률분포를 따르게 됨을 알 수 있다. 표본에 대해 베르누이 분포를 가정하면 prior 값이 베타분포를 따르게 되므로, 베르누이 분포의 경우 MLE에서 사용한 표본의 크기가 100이고 prior 값의 결정에 기여한 표본의 크기가 50이면 posterior 값을 결정할 때 likelihood 쪽이 prior 쪽보다 제곱만큼 혹은 두 배 더 유효하다.

### 베이즈 정리

한편 posterior 값을 새로운 prior 값으로 사용해서 다시 posterior 값을 구하는 것은 어디까지나 확정된 확률밀도함수는 그대로 두고 시행을 여러 번 해서 그런 순서로 결과가 나올 확률을 구하는 과정이다. 앞에서 다룬 MAP과 혼동하기 쉬우니 주의가 필요하다.

식을 전개해 보면 다음이 모두 같다.

  * P(θ|D1, D2)
  * P(θ) * P(D1, D2|θ) / P(D1, D2)
  * P(θ|D1) * P(D2|θ) / P(D2|D1)

### 중첩요인

확률을 비교할 때 비교하려는 확률들이 서로 다르게 구성된 표본으로부터 계산되었을 경우에는 표본의 특징의 차이를 보정해 주어야 한다. 보통 조건부확률을 계산한 것을 합하여 확률을 다시 계산함으로써 해결한다. 중첩요인을 남겨두면 다중공선성 문제가 발생할 수 있으므로 각별히 유의해야 한다.

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] Python Basics for AI
    * Function & Console I/O
    * Conditionals & Loops
    * String & Advanced Function Concept

### 과제 수행 (13:00-14:00)

  * [과제] Python Basics for AI & AI Math
    * Maximum Likelihood Estimation

### 강의 영상 수강 및 퀴즈 제출 (14:00-16:00)

  * [강의] AI Math
    * 베이즈 통계학
  * [퀴즈] AI Math
    * 베이즈 통계학

### Peer session (16:00-17:00)

  * 심화과제 #3 이야기
  * 베이즈 통계학 관련 이야기
  * 다음 peer session 준비
    * AI Math 10강까지 듣고 오기
    * AI Math 10강까지 퀴즈 풀고 오기
    * 심화과제 #2 확인하고 오기

### 커뮤니티 세션 (17:00-17:40)

  * 캠프 구성원 소개

### Daily report 작성 (17:40-19:00)
