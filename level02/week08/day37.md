# Day37 (2022/03/08)

## 노트

### DeepLab

#### Conditional Random Field

경계선을 잡아 주는 작업인데 성능이 매우 좋다고 한다. 다만 이것을 사용하면 학습 시간이 상당히 길어질 것이기 때문에 어떻게 하면 학습 속도의 저하를 최소화하며 사용할 수 있을 지에 대한 고민이 필요하다.

#### Dilated Convolution

Dilated convolution이 어떤 효과가 있는지 잘 몰라서 사용하지 않고 있었는데 receptive field를 확장시키는 효과가 있다고 하니 다음 프로젝트에서 넓은 receptive field를 가지는 모델이 유리할 것으로 예상될 경우 사용해 볼 예정이다.

#### Pyramid Structure

Pyramid 구조는 많은 논문에서 채택한 것이기 때문에 앞으로 fully convolutional model 여러 개를 ensemble할 경우 결과만을 가지고 hard voting 또는 soft voting ensemble하기보다는 pyramid 구조로 엮어서 같이 학습될 수 있도록 하나의 모델로 만들어 볼 예정이다. 현재로서는 pyramid 구조의 성능 개선 가능성에 대해 확신이 있지는 않지만 multiple learning rates와 softmax with temperature를 같이 사용한다면 성능 개선에 도움이 될 수도 있을 것으로 보인다.

#### Separable Convolution

Depthwise convolution과 pointwise convolution을 나눠 two step으로 convolution을 진행하면 parameter 수는 줄이면서도 성능은 떨어뜨리지 않을 수 있다고 한다. 시간복잡도 최적화와 비슷한 맥락인데, 앞으로 모델을 구성할 때에는 이런 최적화가 가능한 지 반드시 검토해 볼 예정이다.

## 일지

### Daily scrum (10:00-10:10)

### 강의 수강 및 퀴즈 제출 (10:10-12:00)

  * [강의] Computer Vision Basics & Research Trends
    * Semantic Segmentation
  * [퀴즈] Computer Vision Basics & Research Trends
    * Image Classification & Data Augmentation
    * Semantic Segmentation

### 과제 수행 (13:00-14:30)

  * [과제] Computer Vision Basics & Research Trends
    * ResNet-34 Implementaion & Fine-tuning

### Time off (14:30-15:00)

  * 정신건강의학과 진료(불면증)

### 과제 수행 (15:00-16:00)

  * [과제] Computer Vision Basics & Research Trends
    * ResNet-34 Implementaion & Fine-tuning

### Peer session (16:00-17:00)

  * Test dataset augmentation 관련 이야기
  * CRF & DeepLab 관련 이야기
  * LRN & DenseNet & DCN 관련 이야기
  * Image blur 관련 이야기
  * 다음 멘토링 준비
    * 최종 프로젝트의 task 정의 생각해 오기
    * 최종 프로젝트에서 사용할 모델 생각해 오기
    * 최종 프로젝트에서 사용할 프로젝트 데이터 생각해 오기
    * 최종 프로젝트에서 사용할 기술 스택 생각해 오기

### 과제 수행 (17:00-18:00)

  * [과제] Computer Vision Basics & Research Trends
    * ResNet-34 Implementaion & Fine-tuning

### Special lecture (18:00-19:20)

  * 이력서 이야기

### 과제 제출 (19:20-19:30)

  * [과제] Computer Vision Basics & Research Trends
    * ResNet-34 Implementaion & Fine-tuning
