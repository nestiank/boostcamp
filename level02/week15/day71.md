# Day71 (2022/04/25)

## 노트

Swin-L을 사용하기 위해서 먼저 공식 레포지토리를 확인했는데 segmentation task를 위한 체크포인트가 없었습니다. 그래서 timm을 봤더니 역시 없었습니다. 마지막으로 pytorch로 직접 구현하는 것을 고민했지만 너무 오래 걸릴 것 같아서 포기했습니다. 실험을 시작하지는 못했고 강의를 마저 들으면서 ImageNet 체크포인트를 사용해서 Swin-L을 학습시키자는 결정을 했습니다.

## 일지

### Daily scrum (10:00-10:10)

### 프로젝트 수행 (10:10-11:00)

  * 베이스라인 코드 확인

### 강의 수강 (11:00-12:00)

  * [강의] Semantic Segmentation
    * Introduction
    * EDA & Metric

### 강의 수강 (13:00-16:00)

  * [강의] Semantic Segmentation
    * Semantic Segmentation Basics
    * Upgrading FCNs I

### Peer session (16:00-17:00)

  * 개인별 학습 상황 공유
  * 최종 프로젝트 관련 이야기
    * SDEdit mask 관련 이야기
  * 장거리 여행 관련 이야기
  * 프로젝트에서 사용할 모델 이야기

### 강의 수강 (17:00-19:00)

  * [강의] Semantic Segmentation
    * Upgrading FCNs II
    * U-Nets

### 프로젝트 수행 (22:40-24:00)

  * Swin transformer 학습 준비
    * timm 베이스라인 코드 확인
    * 코드 작성
