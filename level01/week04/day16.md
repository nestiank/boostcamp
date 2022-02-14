# Day16 (2022/02/07)

## 노트

### Computer Vision Research

#### Key Components

  * Data
  * Model
    * Single Model
    * Sequential Model
    * Ensemble Model
  * Loss
  * Optimization
    * SGD
    * Momentum
    * Nesterov Accelerated Gradient
    * Adagrad
    * Adadelta
    * RMSprop
    * Adam

#### Problems

  * Image Classification
  * Semantic Segmentation
  * Matching
    * Geometric Matching: Image A에 나오는 것을 다른 각도에서 찍은 사진이 image B인데, 같은 물체를 sparse하게 찾아내서 image A를 warp하여 image B처럼 geometric transformation을 해라.
    * Semantic Matching: Image A에 나오는 것과 비슷한 것을 다른 배경에서 찍은 사진이 image B인데, 비슷한 물체를 sparse하게 찾아내서 image A를 warp하여 image B처럼 geometric transformation을 해라.
    * Optical Flow: Video와 같이 image들의 시계열 data가 주어지면 이것을 frame별로 쪼갠 다음 frame들을 dense하게 서로 비교해서 frame마다 image 속의 물체들이 어떻게 움직였는지를 frame A를 warp하여 frame B처럼 geometric transformation을 해서 보여라.
  * Object Detection
  * Pose Estimation
  * Image Synthesis
  * Visual Q&A

#### Optimization Techniques

  * Weight Decay
  * Learning Rate Decay
  * Mixup
  * Bootstrapping
    * Bagging
    * Boosting
  * Bayesian Optimization

#### Regularization Techniques

  * Mini-batch Training
  * Early Stopping
  * Parameter Norm Penalty
  * K-fold Validation
  * Data Augmentation
  * Noise Robustness
  * Label Smoothing
  * Dropout
  * Batch Normalization

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 및 퀴즈 제출 (10:10-11:40)

  * [강의] Deep Learning Basics
    * Historical Review
    * MLP
    * MLP Implementation
  * [퀴즈] Deep Learning Basics
    * Deep Learning Basics

### 과제 제출 (11:40-12:00)

  * [과제] Deep Learning Basics
    * MLP

### 강의 영상 수강 및 퀴즈 제출 (13:00-14:20)

  * [강의] Deep Learning Basics
    * Optimization
    * Optimization Implementation
  * [퀴즈] Deep Learning Basics
    * Optimization

### 과제 제출 (14:20-14:40)

  * [과제] Deep Learning Basics
    * Optimization

### 강의 영상 수강 및 과제 제출 (14:40-16:00)

  * [강의] Deep Learning Basics
    * CNN
    * CNN Implementation
  * [과제] Deep Learning Basics
    * CNN

### Peer session (16:00-17:10)

  * R-CNN 구현 시도 공유

### Daily report 작성 (17:10-19:00)
