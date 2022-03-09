# Day36 (2022/03/07)

## 노트

### Transfer Learning

지난 프로젝트에서 앞쪽을 얼리고 fc layer를 학습시키는 것과 fc layer를 바꿔 달고 전체를 학습시키는 것은 모두 해 보았지만, 뒤쪽에 softmax with temperature를 적용하거나 fc layer의 learning rate를 feature layers보다 크게 하는 것은 해 보지 못했다. Softmax 그리고 double learning rates의 사용은 모델의 성능을 개선할 것으로 보이기 때문에, 다음 프로젝트에서는 사용해 볼 예정이다.

### Knowledge Distillation

EfficientNet의 근간이 되는 구조인데 모델을 계속 바꿔 가면서 학습할 수도 있다.

  * Distillation loss: KL-divergence loss
  * Student loss: cross entropy loss

Softmax 과정에서 temperature parameter를 도입하면 확률분포가 덜 극단적이도록 만들 수 있다.

## 일지

### 프로젝트 정리 (00:20-00:50)

  * 프로젝트 보고서 작성

### 커뮤니티 세션 (10:00-10:20)

  * 캠프 소개

### Meetup session (10:20-10:40)

  * 현재 peer session 진행 상황 공유
  * 다음 peer session 준비
    * Peer session 어떻게 할 것인지 생각해 오기

### 강의 수강 (10:40-12:00)

  * [강의] Computer Vision Basics & Research Trends
    * Computer Vision Overview
    * Image Classification I

### 강의 수강 (13:00-14:00)

  * [강의] Computer Vision Basics & Research Trends
    * Annotation Data Efficient Learning

### Time off (14:00-15:40)

  * 안과 진료(고안압증)

### Time off (15:40-16:00)

  * 다른 트랙 강의 둘러보기 진행

### Peer session (16:00-17:00)

  * Ice-breaking
  * Ground rule 이야기

### 강의 수강 (17:00-19:00)

  * [강의] Computer Vision Basics & Research Trends
    * Image Classification II
