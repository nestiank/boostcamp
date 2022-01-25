# Day06 (2022/01/24)

## 노트

### PyTorch Functions

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
  * torch.chunk()
  * torch.swapdims()
  * torch.Tensor.scatter_()
  * torch.einsum()
  * torch.flip()
  * torch.trace()
  * torch.eye()

#### Others

  * torch.fill_()
  * torch.state_dict()
  * hasattr()

### PyTorch Modules

#### nn.ModuleList

학습 순서를 nn.ModuleList 형태로 정리하면 PyTorch가 해당 모듈을 nn.Module에 등록하여 optimizer() 같은 작업에서 해당 모듈의 parameter들이 학습 대상이 되도록 만든다. 다시 말해서, 일반 list를 사용하면 학습이 되지 않는다.

경우에 따라 nn.ModuleDict를 사용할 수도 있다.

#### nn.parameter.Parameter

학습에 필요한 parameter를 nn.parameter.Parameter 형태로 정리하면 PyTorch가 해당 parameter를 nn.Module에 등록하여 optimizer() 같은 작업에서 해당 parameter들이 학습 대상이 되도록 만든다. 다시 말해서, 일반 Tensor를 사용하면 학습이 되지 않는다.

#### Buffer

  * nn.Module.register_buffer()
  * nn.Module.get_buffer()
  * nn.Module.buffers()
  * nn.Module.named_buffers()

#### Architecture

  * nn.Module.named_modules()
  * nn.Module.named_children()
  * nn.Module.get_submodule()
  * nn.Module.named_parameters()
  * nn.Module.get_parameter()
  * nn.Module.extra_repr()

### PyTorch Hooks

#### Tensor Hooks

  * torch.Tensor.register_hook()

#### Module Hooks

  * nn.Module.register_forward_pre_hook()
  * nn.Module.register_forward_hook()
  * nn.Module.register_backward_hook()
  * nn.Module.register_full_backward_hook()

### PyTorch Apply

  * nn.Module.apply()
  * functools.partial()

### PyTorch Model Learning

> https://github.com/nestiank/action-recognition-cnn-bd-lstm

모델의 구조를 이루는 함수들은 따로 정리하기보다는 이전에 어떻게 썼는지를 보는 것이 나을 것 같아서 링크를 첨부한다. 사실 너무 많아서 정리하기 곤란하다.

#### docstring

모듈이나 함수에 설명을 달아 놓는 습관을 가지자.

#### PyTorch vs TensorFlow

동적 그래프 방식으로 연산하기 때문에 실행 중 내부 값을 확인할 수 있어 디버깅이 편하다. 다른 관점에서도 차이가 있다고 하지만 개인적으로는 큰 차이라고 느끼지 못했다. 정적 그래프 방식으로 연산하면 포팅하기 편하다는 말이 있다.

#### Colab Environment

다른 서버들처럼 ngrok 기반 colab_ssh 라이브러리를 이용해 원격 터미널을 이용할 수 있다.

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
