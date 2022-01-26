# Day08 (2022/01/26)

## 노트

### PyTorch Transfer Learning

#### Model Saving & Loading

```python
model = SomeModel()
torch.save(model, os.path.join(PATH, "model.pt"))
model = torch.load(os.path.join(PATH, "model.pt"))

model_params = SomeModel()
torch.save(model_params.state_dict(), os.path.join(PATH, "params.pt"))
model_params.load_state_dict(torch.load(os.path.join(PATH, "params.pt")))
```

#### Freezing for Fine-tuning

```python
for param in model.parameters():
  param.requires_grad = False
for param in model.tuning_layer.parameters():
  prama.requires_grad = True
```

### PyTorch Monitoring Learning

#### torchsummary

```python
from torchsummary import summary

model = SomeModel()
summary(model, input_size_tuple)
```

#### TensorBoard

> https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html <br>
> https://pytorch.org/docs/stable/tensorboard.html

```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter(PATH)
epochs = 16
img = np.zeros((epochs, 3, 100, 100))

for epoch in range(epochs):
  # Scalar Data
  writer.add_scalar('Loss/train', loss['train'][epoch], epoch)
  writer.add_scalar('Loss/test', loss['test'][epoch], epoch)
  writer.add_scalar('Accuracy/train', accuracy['train'][epoch], epoch)
  writer.add_scalar('Accuracy/test', accuracy['test'][epoch], epoch)
  writer.add_scalars('Data', {'a': epoch, 'b': epoch * 2}, epoch)

  # Continuous Data
  x = np.random.random(1000)
  writer.add_histogram('Histogram', x + epoch, epoch)

  # RGB Image Data
  img[epoch, 0] = np.arange(0, 10000).reshape(100, 100) / 10000 * epoch / epochs
  img[epoch, 1] = (1 - np.arange(0, 10000).reshape(100, 100) / 10000) * epoch / epochs
  img[epoch, 2] = np.transpose(np.arange(0, 10000).reshape(100, 100) / 10000) * epoch / epochs
  writer.add_images('Image', img, epoch)

  # Hyperparameter Data
  writer.add_hparams({'lr': 0.1 * epoch, 'bsize': epoch}, # hparams
                     {'accuracy': 10 * epoch, 'loss': 10 * epoch}) # metrics

# Model Graph Data
model = SomeModel()
data = some_dataloader_func(path)
writer.add_graph(model, data)

writer.flush()
writer.close()

%load_ext tensorboard
%tensorboard --logdir PATH
```

#### Weights and Biases

> https://docs.wandb.ai/guides/track

매뉴얼만 보고 정리하기는 어려우니 나중에 구현 프로젝트에서 직접 사용해 보기로 한다.

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] PyTorch Basics for AI
    * Loading Models

### 강의 영상 수강 및 퀴즈 제출 (13:00-14:30)

  * [강의] PyTorch Basics for AI
    * Monitoring Tools for PyTorch
  * [퀴즈] PyTorch Basics for AI
    * PyTorch Architecture II

### Daily report 작성 (14:30-16:00)

### Peer session (16:00-17:00)

  * 기본과제 #2 이야기
  * 월요일 peer session 활용 방법 이야기
  * 다음 peer session 준비
    * 다음 주 목요일까지 ResNet-34 구현해 오기

### Daily report 작성 (17:00-18:00)

### 어제의 daily report 보충 (18:00-19:00)
