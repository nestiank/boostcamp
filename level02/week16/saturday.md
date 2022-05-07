# Week16 Saturday (2022/05/07)

## 노트

Inference 결과가 뒤섞인 것을 확인하였고, 결과를 파일명에 따라 정렬하여 해결했습니다. 그러나 shuffle을 하지 않도록 코드를 작성해 두었는데 어째서 뒤섞였는지는 알 수 없었고, 코드에 대한 이해를 높이기 위해 계속 알아보기로 했습니다.

Inference 결과의 일부를 다시 시각화해 보았는데, 작은 물체는 잘 탐지하지 못했습니다. 그러나 다른 모델에 비해서 mIoU 점수가 높았기 때문에, 더 많은 inference 결과를 시각화해 보기로 했습니다.

그리고 이것들을 진행하는 동안 GPU를 사용하지 않을 이유가 없으므로, 일단 learning rate 그리고 batch size tuning을 진행해 보기로 했습니다.

## 일지

### 프로젝트 수행 (00:20-02:00)

  * Swin transformer 학습 결과 확인
    * 코드 수정
    * Prediction 생성 및 결과 확인
  * Swin transformer 학습
    * 코드 수정

### 프로젝트 수행 (12:00-14:20)

  * Swin transformer 학습
    * 코드 수정
  * Swin transformer 학습 모니터링

### 프로젝트 수행 (23:30-24:00)

  * Swin transformer 학습 모니터링
  * Swin transformer 학습 결과 확인
    * Prediction 생성 및 결과 확인
