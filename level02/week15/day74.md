# Day74 (2022/04/28)

## 노트

Checkpoint 로드 과정에서 key를 바꿔 주어야 했습니다. 그리고 size mismatch로 인해서 pretrained weight가 로드되지 않은 layer들이 많았습니다. Missing keys 문제나 unexpected keys 문제도 상당히 있었습니다. 이런 상황에서 어제 학습을 시작한 실험 결과가 나왔는데, 학습이 되기는 됐지만 성능이 너무 느리게 올라가서, checkpoint 로드가 효과가 있는지를 확인하기 위하여 checkpoint를 사용하지 않고 학습시키는 비교 실험을 진행하기로 했습니다.

비교 실험을 시작하기 전에 learning rate를 확인해 보니 poly type의 learning rate답게 학습 후반부의 learning rate가 심각하게 작았습니다. 그러나 비교 실험은 변인 통제를 위해서 learning rate 설정을 수정하지 않고 진행하기로 했습니다. 일단 비교 실험을 마치면, 가장 먼저 learning rate 설정을 수정한 실험부터 하기로 했습니다.

## 일지

### Daily scrum (10:00-10:10)

### 프로젝트 수행 (10:10-11:00)

  * Swin transformer 학습 모니터링

### 프로젝트 수행 (11:30-16:00)

  * Swin transformer 학습 결과 확인
    * 코드 수정
    * Prediction 생성 및 결과 확인

### Peer session (16:00-17:00)

  * 개인별 프로젝트 진행 상황 공유
  * 포켓몬 빵 관련 이야기
  * 대학원 입학 관련 이야기
  * 다음 peer session 준비
    * 주간 회고 양식 작성해 오기

### 프로젝트 수행 (17:00-19:00)

  * Swin transformer 학습 결과 확인
    * 코드 수정
    * Prediction 생성 및 결과 확인
  * Swin transformer 학습 준비
    * 코드 수정
