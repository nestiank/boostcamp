# Day04 (2022/01/20)

## 노트

### CNN

대부분의 CV 연구에서는 이미지의 feature 추출 작업을 거친다. 사실 모델을 어떻게 만드는지는 feature 추출을 어떻게 하는 지에 절반 정도 달려 있다고 생각된다. 여기서 convolution 연산은 각 pixel 자료에 위치를 부여하기 때문에, 반드시 사용된다. 만일 FC 레이어를 사용한다면 각 pixel 자료의 위치 정보가 사라진다. 이는 convolution 연산이 cross-correlation 과정이기 때문이다.

#### Backpropagation of CNN

그라디언트를 합해 보면 CNN의 역전파는 다시 convolution 연산이 됨을 알 수 있다.

#### Encoder-decoder Architecture

이미지를 다룰 때 다음과 같은 pixel 단위의 작업을 해야 한다면 주로 encoder-decoder 구조를 사용한다.

  * Semantic segmentation
  * Depth estimation
  * Super-resolution
  * Image denoising

### LSTM

> https://wikidocs.net/48920 <br>
> https://wikidocs.net/147234

주로 NLP 분야의 많은 연구들에서 attention이나 다른 널리 알려진 레이어 인사이트들을 LSTM에 도입하는 방식으로 LSTM의 보완을 시도해 왔다. 주목할 점은 이런 시도들이 모델의 성능을 향상시키면서도 의외로 학습 시간에 큰 영향을 주지 않는다는 점이다.

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] Python Basics for AI
    * Python Data Structure

### 강의 영상 수강 및 퀴즈 제출 (13:00-14:30)

  * [강의] AI Math
    * CNN
    * RNN
  * [퀴즈] AI Math
    * CNN
    * RNN

### 과제 수행 (14:30-15:30)

  * [과제] Python Basics for AI & AI Math
    * Backpropagation

### 어제의 daily report 보충 (15:30-16:00)

### Peer session (16:00-17:00)

  * 심화과제 #2 이야기
  * 다음 peer session 준비
    * 주간 회고 양식 작성해 오기

### Special lecture (17:00-18:00)

  * 수학 공부 관련 이야기
  * 인공지능 대학원 관련 이야기
  * 커리어 관련 이야기

### Daily report 작성 (18:00-19:00)
