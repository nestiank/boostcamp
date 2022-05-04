# Day78 (2022/05/04)

## 노트

Checkpoint 로드 문제와 online resize 문제가 갑자기 매우 간단하게 해결되었습니다. Checkpoint 로드 문제는 모델 구조를 checkpoint가 주장하는 것에 끼워 맞춰서 해결했습니다. Online resize 문제는 mmsegmentation 이슈에 올바른 답변이 다시 달리면서 해결되었습니다.

그런데 test 성능이 매우 나빴고 inference 결과를 시각화해 보니 매우 그럴듯하지만 대상 image와 전혀 관련이 없는 결과가 나오는 현상이 발견되었으나 원인을 찾지 못했습니다.

## 일지

### Daily scrum (10:00-10:10)

### 프로젝트 수행 (10:10-12:00)

  * Swin transformer 학습 시도
    * 코드 수정

### 프로젝트 수행 (13:00-15:30)

  * Swin transformer 학습
    * 코드 수정
  * Swin transformer 학습 모니터링

### 주간 회고 작성 (15:30-16:00)

### Peer session (16:00-17:00)

  * 개인별 프로젝트 진행 상황 공유
  * 주간 팀 회고 진행

### 프로젝트 수행 (17:00-19:00)

  * Swin transformer 학습 모니터링
  * Swin transformer 학습 결과 확인
    * 코드 수정
    * Prediction 생성 및 결과 확인
