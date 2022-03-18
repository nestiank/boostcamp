# Day43 (2022/03/16)

## 노트

### Multi-modal Learning

#### Main Tasks

  * Matching: Image tagging
  * Translation: Image captioning
  * Referencing: Visual question answering

#### Dataset Issues

  * Different representations according to modality
  * Unbalance between feature spaces

Modality에 따라서 데이터의 자료구조가 달라지고 같은 semantics를 가지는 서로 다른 modality의 데이터들은 일대일 대응이 되지 않는다. 결국 모든 modality의 모든 데이터를 동일한 자료구조로 임베딩하는 것이 해답인데 이걸 어떻게 하는 것이 가장 좋은지는 특히 3D 쪽에서는 아직 합의되지 않은 것 같다.

일단 NLP task에서는 skip-gram model인 word2vec이 de facto 표준이 된 것이 거의 확실해 보인다.

Joint embedding을 사용하게 되면 cosine similarity loss와 semantic regularization loss를 같이 사용하는 등의 방법으로 모델이 low-level 그리고 high-level semantics를 모두 matching할 수 있도록 해야 한다.

#### Architecture Design Issues

모델이 특정 modality에 집중하게 되는 경우가 많은데 information gain의 관점에서 바라보면 이런 경우는 반드시 막아야 한다. 가끔 보면 사람이 데이터를 직접 보고 어느 modality의 데이터가 더 많은 정보를 담고 있는지 판단해서 모델의 편향된 학습이 성능에 별로 영향을 주지 못하는 것처럼 보이면 개발 일정 등의 이유로 이를 방치하는 경우가 있는데, 서비스 배포 이후 모델에서 generalization 관점에서 대형 사고를 일으켜서 실제로 서비스에서 사고가 발생할 수도 있다는 점을 명심해야 할 것이다.

아예 CV task는 CNN으로 feature extraction을 하고 NLP task는 RNN으로 attention을 계산하는 방식이 있는데 학습 시간을 고려하면 모델의 경량화도 어느 정도 중요해 보인다.

#### Beam Search

Image captioning과 같이 NLP task가 들어 있는 경우 그쪽에서 recurrent layer를 사용하기 때문에 CV에서는 자주 사용되지 않는 beam search를 사용해야 한다. 이런 경우들을 볼 때마다 폭넓은 학습이 중요하다는 생각이 든다.

#### Dealing with Sound Data

Waveform의 분해를 위해 short time Fourier transform이 사용되며 데이터 시각화는 보통 spectogram으로 한다.

SoundNet의 경우 visual recognition networks가 object distribution network과 scene distribution network으로 나눠지기 때문에 sound waveform network의 끝에서 두 개의 head를 사용하여 두 개의 KL-divergence loss를 사용한다는 점이 인상적이었다. 그리고 CV에서도 마찬가지이긴 하지만 waveform에 대한 pooling layer가 more generalizable semantic information을 얻는 데에 특별히 유용하다는 점은 modality에 따라서 어떤 방식으로 information gain이라는 목표에 도달할 것인지를 다르게 설계해야 한다는 점을 지적해 준다.

Image-to-speech synthesis의 경우 같은 문장을 다른 사람이 말하는 경우와 다른 문장을 같은 사람이 말하는 경우를 잘 분별해서 학습하도록 하는 것이 어려웠을 것이다. 이것을 위해서 당연히 self-supervised learning을 했다고 하는데 좋은 성능을 내기 위해서 영상을 수백만 개나 사용했다고 하니 앞으로는 보다 현실적인 규모의 영상 데이터셋으로도 이런 task를 처리할 수 있을지가 중요할 것으로 보인다.

Sound source localization은 앞의 task보다는 약간 쉬워 보인다.

## 일지

### Daily scrum (10:00-10:10)

### 과제 수행 (10:10-12:00)

  * [과제] Computer Vision Basics & Research Trends
    * Conditional GAN

### 강의 수강 및 퀴즈 제출 (13:00-14:30)

  * [강의] Computer Vision Basics & Research Trends
    * Multi-modal Learning
    * Image Captioning
  * [퀴즈] Computer Vision Basics & Research Trends
    * Multi-modal Learning

### 과제 수행 (14:30-16:00)

  * [과제] Computer Vision Basics & Research Trends
    * Multi-modal Applications with CLIP

### Peer session (16:00-17:00)

  * 기본과제 이야기

### 과제 제출 (17:00-17:40)

  * [과제] Computer Vision Basics & Research Trends
    * Multi-modal Applications with CLIP

### 과제 제출 (17:40-20:30)

  * [과제] Computer Vision Basics & Research Trends
    * Conditional GAN
