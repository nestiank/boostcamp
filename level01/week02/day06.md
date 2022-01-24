# Day06 (2022/01/24)

## 노트

### Pytorch Functions

#### Matrix Multiplication

  * torch.mm(): Non-broadcasting multiplication
  * torch.bmm(): Non-broadcasting batch-based multiplication
  * torch.matmul(): Broadcasting multiplication

#### View vs Reshape

  * torch.view(): Contiguity needed
  * torch.reshape(): Copy when not contiguous
    * Compatible with the results of those
      * torch.t()
      * torch.narrow()
      * torch.expand()
      * torch.permute()

#### Shapes

  * torch.index_select()
  * torch.gather()
  * torch.flatten()
  * torch.expand()
  * torch.numel()

#### Model Learning

loss, criterion, backward 등 전반적인 구조를 이루는 함수들에 관해 정리할 예정.

#### Others

  * torch.fill_()

과제에서 나온 함수들에 관해 정리할 예정.

과제가 너무 오래 걸려서 도저히 정리를 제대로 마치지 못했다.

과제를 끝낸 데에 의의를 두고 내일 정리하기로..

### Colab Environment

  * colab_ssh(with ngrok)

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] PyTorch Basics for AI
    * Introduction to PyTorch
    * PyTorch Basics

### 강의 영상 수강 (13:00-13:50)

  * [강의] PyTorch Basics for AI
    * PyTorch Project Architecture

### 퀴즈 제출 (13:50-14:00)

  * [퀴즈] PyTorch Basics for AI
    * PyTorch Basics

### 과제 수행 (14:00-16:00)

  * [과제] PyTorch Basics for AI
    * PyTorch Custom Model

### Peer session (16:00-17:00)

### 과제 제출 (17:00-21:00)

  * [과제] PyTorch Basics for AI
    * PyTorch Custom Model

### Daily report 작성 (21:00-21:10)
