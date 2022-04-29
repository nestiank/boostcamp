# Day75 (2022/04/29)

## 노트

> https://github.com/open-mmlab/mmsegmentation/issues/1530

대회 규정 때문에 이미지를 resize한 다음 inference를 진행해야 하는데, mmdetection이나 mmsegmentation은 당연히 TTA를 전부 복원하고 inference 결과를 내놓기 때문에, 복원되지 않는 resize 방법을 알아봐야 했습니다. mmsegmentation 레포지토리에 이슈를 작성하여 질문해 두었습니다.

어제 계획한 비교 실험을 진행한 결과 metric, loss, accuracy 모두 checkpoint 사용 여부와 관계 없이 그래프가 일정하게 그려졌습니다. 불확실성의 제거를 위하여 아예 checkpoint를 사용하지 않고 높은 초기 learning rate로 오랫동안 학습시키기로 하고, 실험을 시작했습니다.

## 일지

### 프로젝트 수행 (00:00-01:30)

  * Swin transformer 학습
    * 코드 수정

### Daily scrum (10:00-10:10)

### 프로젝트 수행 (10:10-12:00)

  * Swin transformer 학습 준비
    * 코드 수정

### 프로젝트 수행 (13:00-15:30)

  * Swin transformer 학습 준비
    * 코드 수정

### 주간 회고 작성 (15:30-16:00)

### Peer session (16:00-17:00)

  * 주간 팀 회고 진행
  * 멘토링 관련 이야기

### Office hour (17:00-18:00)

  * 베이스라인 코드 해설

### 프로젝트 수행 (18:00-19:00)

  * Swin transformer 학습
    * 코드 수정
