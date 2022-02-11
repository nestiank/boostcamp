# Day19 (2022/02/10)

## 노트

### Core Generative Models

#### Variational Auto-encoder

  * Variational Inference: Posterior density를 가장 잘 근사할 수 있는 variational density를 찾는 과정
    * ELBO: Evidence Lower Bound
    * log density = ELBO + KL(variational||posterior)
    * KL-Divergence >= 0이므로 ELBO는 evidence density의 하한이 됨
    * KL-Divergence를 최소화하기 위해 ELBO를 최대화(샌드위치 방식)
  * ELBO = reconstruction term - prior fitting term
    * Auto-encoder의 reconstruction loss를 최소화
    * Variational density와 latent density의 차이를 최소화
  * Latent density를 구하는 방법: Isotropic Gaussian density로 가정
    * KL-Divergence의 미분가능성을 고려한 결정

#### Adversarial Auto-encoder

  * Latent density를 미리 정하고 샘플링을 해서 샘플이 강제로 latent density를 따르게 함
  * VAE의 학습을 GAN 방식으로 진행

#### GAN

  * GAN: Repetitive minimax game between generator and discriminator
    * Generator는 discriminator가 optimal하다고 바라보고 Jensen-Shannon Divergence의 최소화를 시도함
  * DCGAN: USed leakly ReLU and deconvolution instead of MLPs
  * InfoGAN: Auxiliary class를 도입하여 모델이 class를 결정하는 one-hot vector에 집중할 수 있도록 함
  * Text2Image: For image synthesis task
  * PuzzleGAN: For image recovery task
  * CycleGAN: Cycle-consistency loss를 위해 GAN을 사용
  * StarGAN: For style transfer task
  * ProgressiveGAN: For high-fidelity generative task

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 및 퀴즈 제출 (10:10-11:20)

  * [강의] Deep Learning Basics
    * Generative Models II
  * [퀴즈] Deep Learning Basics
    * Generative Models

### 과제 수행 (11:20-11:40)

  * [과제] Deep Learning Basics
    * AAE

### 과제 정답 확인 및 비교 (11:40-12:00)

### 보충 학습 (13:00-16:00)

> https://arxiv.org/pdf/1706.03762.pdf

  * Transformer 논문 읽기

### Peer session (16:00-17:00)

  * 심화과제 이야기
  * Positional encoding 이야기
  * 다음 peer session 준비
    * 주간 회고 양식 작성해 오기

### Office hour (17:00-18:00)

  * 과제 해설

### Daily report 작성 (18:00-19:00)
