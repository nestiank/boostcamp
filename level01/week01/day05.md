# Day05 (2022/01/21)

## 노트

### Python generator

> https://wikidocs.net/16069

대용량 데이터를 처리할 때 generator를 사용하면 모든 데이터를 메모리에 미리 올릴 필요도 없고, 모든 데이터에 대해 미리 계산할 필요도 없다.

느슨한 평가라는 특징에서 알 수 있듯이 generator는 iterable 객체이다.

```python
def generator_func(value):
  for i in range(value):
    yield i

print("A", generator_list(10))
print("B", [i for i in generator_list(10)])

generator_item = (i for i in range(10))
print("C", generator_item)
print("D", [i for i in generator_item])
```

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] Python Basics for AI
    * Pythonic Code

### 주간 회고 작성 (13:00-13:30)

### 과제 정답 확인 및 비교 (13:30-15:00)

### Extended peer session (15:00-16:00)

  * Ice-breaking
  * 팀별 학습 방식 공유
  * 팀별 멘토링 방식 공유
  * 개인별 진로 계획 공유

### Peer session (16:00-17:00)

  * 다른 팀의 학습 상황 공유
  * 주간 팀 회고 진행
  * 취미 이야기

### Office hour (17:00-18:20)

  * 과제 해설

### Daily report 작성 (18:20-19:00)
