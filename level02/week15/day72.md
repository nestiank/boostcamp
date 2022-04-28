# Day72 (2022/04/26)

## 노트

ImageNet 체크포인트를 사용해서 학습시키기에 앞서 annotation 포맷의 문제가 발생했습니다. 대략적인 구조는 COCO Stuff와 비슷했지만 segmentation 인코딩 방식에 차이가 있었습니다. 인코딩을 변경하기보다는 custom dataset class를 만들거나 데이터셋의 구조를 변경하는 것이 낫겠다고 판단했습니다. 먼저 베이스라인 코드의 class를 이용해서 custom dataset class를 만들고자 시도했으나, 베이스라인 코드는 mmsegmentation과 관련이 없기 때문에 torch.nn의 Dataset class를 상속하고 있었고, 이것을 mmsegmentation에서 비슷하게 구현하려면 너무 많은 메소드를 오버라이딩해야 한다는 결론이 나와서 시간 내에 작업을 마치지 못했습니다. 그러나 데이터셋의 구조를 변경하는 것 또한 어려운 일이라서 어느 쪽으로 계속 시도할 지에 대해 고민했습니다.

## 일지

### 프로젝트 수행 (00:00-01:10)

  * Swin transformer 학습 준비
    * 코드 작성

### Daily scrum (10:00-10:10)

### 프로젝트 수행 (10:10-12:00)

  * Swin transformer 학습 준비
    * 코드 작성

### 프로젝트 수행 (13:00-16:00)

  * Swin transformer 학습 준비
    * 코드 작성

### Mentoring (16:00-17:40)

  * 대학원 면접 관련 이야기
  * 프로젝트 메타데이터 관련 이야기
  * 면접에서 나온 질문 소개

### Peer session (17:40-18:10)

  * 대학원 면접 관련 이야기
  * Transformer 관련 이야기

### 프로젝트 수행 (18:10-19:00)

  * Swin transformer 학습 준비
    * 코드 작성
