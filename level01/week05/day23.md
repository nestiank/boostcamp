# Day23 (2022/02/16)

## 노트

### Service Oriented AI Development Process

#### Data Collection

  * 데이터셋의 종류 설정
    * 도메인 정의: 고등학교 교육과정 범위의 수식
    * 표현 형태 정의: 인쇄된 수식과 손글씨
    * 표현 상태 정의
      * 내용: 수정 테이프, 형광펜, 취소선
      * 배경: 종이의 질감, 그림자, 잘림, 접힘, 구겨짐, 회전
      * 이미지 하나에 여러 개의 수식이 포함된 경우
  * 데이터셋의 종류별 수량 설정

#### Modeling

  * 모델의 정답 요구사항 설정
    * 영역 검출
      * 직사각형: 좌표 2개
      * 직사각형과 회전 각도
      * 사각형: 좌표 4개
    * 출력 형태
      * 좌표
      * 마스킹한 입력 이미지
  * 모델의 기술적 요구사항 설정
    * QPS
    * Accuracy
    * Serving requirements
      * Local or cloud
      * Device specifications

#### Testing

  * Offline
    * Filtering model candidates
    * Final model selection
  * Online
    * Automatic service senario evaluation
  * After deployment
    * Voice of customer

### Source of Bias

  * Target definition
  * Data labeling
  * Data collection
    * Underrepresentation
    * Overrepresentation
  * Feature selection
    * Unintentional redlining
    * Intentional result masking

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] AI Service Development Basics
    * Service Oriented AI Development

### 강의 영상 수강 (13:00-15:00)

  * [강의] AI Service Development Basics
    * AI Ethics

### Special lecture (15:00-16:00)

  * 개발자 취업 이야기

### Peer session (16:00-17:00)

  * Data structure 면접 질문 이야기
  * 다음 peer session 준비
    * 금요일까지 statistics 면접 질문 공부해 오기

### Daily report 작성 (17:00-19:00)
