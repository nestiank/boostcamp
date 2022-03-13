# Day40 (2022/03/11)

## 노트

### Focal Loss

프로젝트에서 f1 loss는 사용해 봤지만 focal loss는 사용해 보지 못했는데 프로젝트 데이터에 심각한 class imbalance 문제가 있었던 점을 고려하면 아마 focal loss를 사용했더라면 더 좋은 성과를 낼 수 있었을 것으로 보인다. 다음 프로젝트에서 직접 사용해 보기로 한다.

### DETR

RetinaNet의 경우에도 pyramid structure를 채택했지만 transformer를 사용한 DETR의 경우에도 deformable DETR이 나오면서 pyramid structure를 채택했다. 아무래도 넓은 receptive field를 가지는 것의 이점이 큰 것으로 보인다.

### CNN Visualization

#### Dimensionality Reduction

데이터 시각화 과정에서 데이터의 복잡도가 높은 경우 보통 t-SNE 등의 기법으로 차원 축소를 진행하는데, 이 과정에서 다중공선성 문제가 발생하여 비슷한 semantic feature dimension들이 여러 개 살아남는 경우 데이터 시각화의 결과가 실제 데이터의 분포와는 다소 다를 수 있음에 유의해야 한다. 차원 축소를 해 보기 전에 먼저 모든 feature dimension들의 correlation 등을 파악해야 할 것이다.

#### Activation Map

가장 기초적인 방법인데 데이터 시각화를 위해 activation map을 바로 확인하는 방법이 있다. 여기서는 layer activation을 그대로 눈으로 확인할 수도 있고 maximally activated patch를 확인할 수도 있다.

#### Gradient Ascent

비어 있는 이미지나 노이즈 이미지를 사용해서 gradient가 어떻게 형성되어 있는지를 확인하는 방법이 있다. 여기서는 각 convolution layer별 gradient를 확인할 수는 없다.

#### Occlusion Map

데이터 시각화를 위해 occlusion map을 만들어 볼 때 sailency map을 만들 수도 있고 deconvolution을 진행할 수도 있는데 차이점은 역전파 과정에서의 activation function의 적용 여부이다.

#### GradCAM

모델 자체를 수정해서 fc layer 대신 GAP layer를 달아서 데이터 시각화를 진행하는 방법이다. 모든 task에 범용으로 사용 가능하다는 장점이 있고 guided backpropagation과 같이 사용해서 결과를 서로 곱하면 scouter처럼 negative occlusion map도 구할 수 있다. 이것을 GAN dissection 등에서 활용하면 이미지 합성에도 활용할 수 있다.

## 일지

### Daily scrum (10:00-10:10)

### 강의 수강 및 퀴즈 제출 (10:10-12:00)

  * [강의] Computer Vision Basics & Research Trends
    * Object Detection
    * CNN Visualization
  * [퀴즈] Computer Vision Basics & Research Trends
    * Object Detection
    * CNN Visualization

### 과제 수행 (13:00-14:30)

  * [과제] Computer Vision Basics & Research Trends
    * CNN Visualization

### 주간 회고 작성 (14:30-15:00)

### Extended peer session (15:00-16:00)

  * Ice-breaking
  * 최종 프로젝트 관련 이야기
  * 취미 & 가상자산 이야기
  * 개인별 프로젝트 경험 이야기
  * 42 Seoul 관련 이야기
  * AutoGrad 관련 이야기

### Peer session (16:00-17:00)

  * Welcome party
    * 준비해 온 과자 소개
    * 밸런스 게임 진행
  * 주간 팀 회고 진행
  * 다음 peer session 준비
    * 다음 주 월요일까지 denoising diffusion probabilistic models 논문 리뷰해 오기

### 강의 수강 (17:00-18:00)

  * [강의] Computer Vision Basics & Research Trends
    * AutoGrad

### 커뮤니티 세션 (18:00-19:30)

  * 취업 관련 이야기
  * 부스트캠프 수료 이후에 대한 이야기
