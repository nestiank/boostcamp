# Day10 (2022/01/28)

## 노트

### Memory Tracking Tools

#### nvidia-smi

현재 GPU의 상태를 잘 정리해서 보여 준다.

#### GPUtil

```python
import GPUtil
GPUtil.showUtilization()
```

### Memory Shortage Troubleshooting

#### Common Solutions

  * del
  * nvidia-smi -r
  * torch.no_grad()
  * torch.cuda.empty_cache()

#### Computational Graph Verification

```python
for epoch in range(epochs):
  output = model(input)
  loss = criterion(output)

  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

  # total_loss += loss
  total_loss += loss.item()
```

모델의 computational graph에 불필요한 node가 추가되지 않도록 유의해야 한다.

## 일지

### Daily scrum (10:00-10:20)

### 어제의 daily report 보충 (10:20-11:20)

### 주간 회고 작성 (11:20-12:00)

### 강의 영상 수강 및 퀴즈 제출 (13:00-14:00)

  * [강의] PyTorch Basics for AI
    * PyTorch Troubleshooting
  * [퀴즈] PyTorch Basics for AI
    * PyTorch Applications

### Daily report 작성 (14:00-15:00)

### Extended peer session (15:00-16:00)

  * Ice-breaking
  * 팀별 학습 방식 공유
  * 팀별 멘토링 방식 공유
  * 개인별 진로 계획 공유

### Peer session (16:00-17:00)

  * 다른 팀의 상황 공유
  * 주간 팀 회고 진행
  * 디바이스 이야기

### Special lecture (17:00-18:00)

  * 데이터 중심 인공지능 이야기
  * 커리어 관련 이야기

### Daily report 작성 (18:00-19:00)
