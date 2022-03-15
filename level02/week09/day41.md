# Day41 (2022/03/14)

## 노트

### Landmark Localization

Gaussian heatmap은 연산량이 상당했을 것인데 시도되었다는 것 자체가 상당히 놀랍다. 결국 이후에 hourglass structure나 pyramid structure를 사용한 모델이 나오면서 빠르게 대체된 것으로 보인다.

### Conditional GAN Loss

Conditional GAN을 학습시키기 위한 loss가 아래의 두 종류로 이루어지는 것은 이해가 되는데 주로 l2 loss 대신 l1 loss가 채택되는 이유가 궁금하다. 아마 square 과정을 거치면서 l2 loss가 l1 loss보다 조금 더 극단적인 값을 가지게 된다는 것이 고려된 것 같은데 그렇다면 바로 linear loss를 사용하는 대신 power 값으로 2가 아니라 1.2 같은 값을 사용해 볼 수도 있었을 것이다. 이유를 생각해 보자면 아마 연산량 때문에 바로 linear loss를 사용했을 것 같다.

  * GAN loss
  * L1 loss

### Perceptual Loss

Loss network으로 여러 모델 중에서도 주로 VGG-Net이 채택되는 이유가 궁금하다. 아마 feature extraction을 가장 높은 가성비로 진행할 수 있는 모델이라 채택된 것 같다.

  * Feature reconstruction loss
  * Style reconstruction loss

## 일지

### Daily scrum (10:00-10:10)

### Time off (10:10-11:40)

  * 다른 트랙 강의 둘러보기 진행

### Time off (11:40-12:10)

  * 인터넷 공유기 설정 오류 수정

### 강의 수강 및 퀴즈 제출 (12:10-13:00)

  * [강의] Computer Vision Basics & Research Trends
    * Instance / Panoptic Segmentation & Landmark Localization
  * [퀴즈] Computer Vision Basics & Research Trends
    * Ohter Tasks

### 강의 수강 (13:00-14:30)

  * [강의] Computer Vision Basics & Research Trends
    * Conditional Generative Model

### Time off (14:30-15:00)

  * 긴급한 개인적인 서류 작업 진행

### 강의 수강 및 퀴즈 제출 (15:00-15:30)

  * [강의] Computer Vision Basics & Research Trends
    * Conditional Generative Model
  * [퀴즈] Computer Vision Basics & Research Trends
    * Image Generation

### 보충 학습 (15:30-16:00)

> https://arxiv.org/pdf/2006.11239.pdf

  * Denoising diffusion probabilistic models 논문 읽기

### Peer session (16:00-17:00)

  * Denoising diffusion probabilistic models 논문 소개
  * 다음 peer session 준비
    * 수요일까지 기본과제 완료하고 오기
    * 금요일까지 diffusion model 이해하고 오기

### 과제 수행 (17:00-20:00)

  * [과제] Computer Vision Basics & Research Trends
    * Conditional GAN
