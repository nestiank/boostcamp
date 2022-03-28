# Day18 (2022/02/09)

## 노트

### Core CNN Models

#### Baselines

  * AlexNet
    * Used ReLU activation
    * Local Response Normalization
    * Overlapping Pooling
    * Data Augmentation
    * Dropout
  * VGGNet: Used only 3x3 convolutions
  * GoogLeNet: Used wise 1x1 convolutions
  * ResNet: Residual Network
  * DenseNet: Concatenation Network

#### Semantic Segmentation

  * Fully Convolutional Network
  * UNet: Auto-encoder Network
  * DeepLab

#### Object Detection

  * R-CNN
    * Selective Search
    * Bounding Box Regression
    * SVM
  * SPPNet: Spatial Pyramid Pooling
  * Fast R-CNN: ROI Pooling
  * Faster R-CNN: Region Proposal Network
  * YOLO
    * Without explicit bounding box sampling
    * Simultaneous prediction of bounding boxes and class probabilities

### Generative Models

  * Implicit Models: Generation only
  * Explicit Models: Estimate density

#### Related Tasks

  * Generation
  * Density Estimation
  * Unsupervised Representation Learning

#### Auto-regressive Models

  * Leveraging conditional independency
    * Neural Autoregressive Density Estimator: Consider every prior pixel
    * Pixel RNN: Consider some prior pixels
  * Ordering data patches
    * Pixel RNN with Row LSTM: Consider every top-left prior pixel
    * Pixel RNN with Diagonal BiLSTM: Consider diagonal prior pixels

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 및 퀴즈 제출 (10:10-12:00)

  * [강의] Deep Learning Basics
    * Modern CNN
    * Computer Vision Applications
  * [퀴즈] Deep Learning Basics
    * CNN

### 강의 영상 수강 및 퀴즈 제출 (13:00-14:30)

  * [강의] Deep Learning Basics
    * Generative Models I

### 과제 수행 (14:30-16:00)

  * [과제] Deep Learning Basics
    * ViT

### Peer session (16:00-17:00)

  * Transformer 관련 이야기
  * 대학원 연구실 관련 이야기

### Daily report 작성 (17:00-19:00)
