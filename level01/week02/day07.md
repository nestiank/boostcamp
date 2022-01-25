# Day07 (2022/01/25)

## 노트

### PyTorch Optimizers

#### Optimization Functions

  * torch.optim.Optimizer.zero_grad()
  * torch.optim.Optimizer.step()
  * torch.optim.Optimizer.state_dict()
  * torch.optim.Optimizer.load_state_dict()

#### Optimization Algorithms

  * torch.optim.Adagrad()
  * torch.optim.Adam()
  * torch.optim.RMSprop()
  * torch.optim.Rprop()
  * torch.optim.SGD()

### PyTorch Datasets

  * torch.utils.data.Dataset
    * Map-style Datasets
  * torch.utils.data.IterableDataset
    * Iterable-style Datasets

```python
class CustomDataset(Dataset):
  def __init__(self, path):
    self.data = some_dataloader_func(path)
    self.X = self.data['media']
    self.y = self.data['label']

  def __len__(self):
    return len(self.data)

  def __getitem__(self, idx):
    X = self.X[idx]
    y = self.y[idx]
    return X, y

class CustomIterableDataset(IterableDataset):
  def __init__(self, path, start, end):
    assert end > start
    self.start = start
    self.end = end
    self.path = path

  def __iter__(self):
    data = some_dataloader_func(self.path)
    for i in range(self.start, self.end):
      yield data['media'][i], data['label'][i]
```

데이터가 너무 큰 경우 yield를 사용하기 위해 IterableDataset으로 데이터를 가져오는 경우도 있다. 하지만 iterable object이기 때문에 Sampler와 함께 사용할 수 없고 multi-GPU 환경에서는 각 worker에서 다른 데이터를 불러올 수 있도록 worker_init_fn을 정의해 주어야 한다.

#### Sampler

  * SequentialSampler: Sequential
  * RandomSampler: Random
  * SubsetRandomSampler: Random without replacement
  * WeigthRandomSampler: Weighted random
  * BatchSampler: Wrapper for batch-based sampling
  * DistributedSampler: Used with torch.nn.parallel.DistributedDataParallel

#### Variable Length Datasets

가변 길이 데이터를 다룰 때에는 collate 함수를 정의하여 torch.utils.data.DataLoader의 collate_fn option에 넣어 주어야 한다.

```python
def collate_func(samples):
  data = []
  goal_len = 100
  for sample in samples:
    sample_fix = torch.cat([sample, sample.new_zeros(goal_len - len(sample))])
    data.append(sample_fix)
  return torch.stack(data)
```

### torchvision

> https://github.com/nestiank/action-recognition-cnn-bd-lstm

```python
transform_dataset_train = transforms.Compose([
  transforms.ToTensor(),
  transforms.Resize([224, 224]),
  transforms.RandomHorizontalFlip(),
  transforms.RandomCrop(112)
])

dataset_train_CIFAR10 = torchvision.datasets.CIFAR10(root='data/CIFAR10/',
                                                     train=True,
                                                     transform=transform_dataset_train,
                                                     download=True)

dataloader_train_CIFAR10 = torch.utils.data.DataLoader(dataset=dataset_train_CIFAR10,
                                                       batch_size=16,
                                                       shuffle=True,
                                                       collate_fn=collate_func)
```

#### torchvision.transforms

  * torchvision.transforms.Resize()
  * torchvision.transforms.RandomCrop()
  * torchvision.transforms.RandomRotation()
  * torchvision.transforms.RandomHorizontalFlip()
  * torchvision.transforms.RandomVerticalFlip()
  * torchvision.transforms.Compose()

#### torchvision.datasets

  * torchvision.datasets.MNIST()
  * torchvision.datasets.CIFAR10()
  * torchvision.datasets.HMDB51()

## 일지

### Daily scrum (10:00-10:10)

### 어제의 daily report 보충 (10:10-11:10)

### 강의 영상 수강 (11:10-12:00)

  * [강의] PyTorch Basics for AI
    * AutoGrad & Optimizer

### 강의 영상 수강 및 퀴즈 제출 (13:00-14:00)

  * [강의] PyTorch Basics for AI
    * Dataset & Dataloader
  * [퀴즈] PyTorch Basics for AI
    * PyTorch Architecture I

### 과제 제출 (14:00-16:00)

  * [과제] PyTorch Basics for AI
    * PyTorch Custom Dataset

### Peer session (16:00-17:00)

  * 기본과제 #1 이야기
  * Dacon 관련 이야기

### Daily report 작성 (17:00-19:00)

### Mentoring (19:00-20:00)

  * 논문 구현 스터디 관련 이야기
  * PyTorch Basics 라이브 코딩
  * PyTorch Lightning 소개
