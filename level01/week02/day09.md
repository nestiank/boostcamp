# Day09 (2022/01/27)

## 노트

### PyTorch Parallel Learning

데이터가 충분히 많지 않으면 batch 크기가 유의미하게 감소하여 성능에 영향이 있을 수 있다.

#### Plain PyTorch Implementation

```python
class SomeModel(nn.Module):
  def __init__(self, in_channels, out_channels):
    super().__init__()
    self.seq1 = nn.Linear(in_channels, 256).to('cuda:0')
    self.seq2 = nn.Linear(256, out_channels).to('cuda:1')

  def forward(self, x):
    x = self.seq1(x).to('cuda:1')
    x = self.seq2(x)
    return x
```

#### nn.DataParallel

```python
model = SomeModel()
parallel_model = nn.DataParallel(model)
for epoch in range(epochs):
  preds = parallel_model(inputs)
  loss = criterion(preds, labels)

  optimizer.zero_grad()
  loss.mean().backward()
  optimizer.step()
```

사용이 간단하지만 데이터를 균등 분배하기 때문에 메인 worker가 소재한 GPU에서 병목이 발생할 수 있다.

프로세스가 아닌 쓰레드 기반 병렬 처리 방식이다. 따라서 I/O 작업으로 인한 context switching이 많은 경우가 아니라면 global interpreter lock으로 인해 속도에서의 이점이 부족하다.

  * Single-GPU
    * Multi-threading: I/O가 별로 없으면 GIL 때문에 속도에서 큰 의미가 없고 I/O가 많으면 의미 있음
    * Multi-processing: 마찬가지
  * Multi-GPU
    * Multi-threading: I/O가 별로 없으면 GIL 때문에 일부만 병렬처리가 가능해서 속도에서 의미가 있긴 하나 부족함
      * nn.DataParallel
    * Multi-processing: GIL에서 자유롭기 때문에 훨씬 의미있으나 sampler 그리고 data pipe가 도입되므로 추가적인 연산이 요구됨
      * nn.parallel.DistributedDataParallel

#### nn.parallel.DistributedDataParallel

프로세스 기반 병렬 처리 방식이기 때문에 속도에서의 이점이 있지만 구현이 복잡하다.

  * Sampler: torch.utils.data.distributed.DistributedSampler()
  * Pipe: torch.distributed.init_process_group()
  * Execution: torch.multiprocessing.spawn()

#### Ray Train

사용해보지 않아서 모르겠으니 나중에 구현 프로젝트에서 직접 사용해 보기로 한다.

### PyTorch Monitoring Learning

#### tqdm

```python
for epoch in range(epochs):
  pbar = tqdm(dataloader)
  for ind, (images, labels) in enumerate(pbar):
    pbar.set_description("Epoch %02d | Loss %06.2f | Accuracy %06.2f" % (epoch, running_loss, running_acc))
  tune.report(accuracy=best_test_accuracy.item(), loss=best_test_loss)
```

진행률을 알고 싶은 iterable 객체를 tqdm()으로 감싸주기만 하면 진행률을 쉽게 확인할 수 있다.

### Hyperparameter Tuning

#### Ray Tune

> https://pytorch.org/tutorials/beginner/hyperparameter_tuning_tutorial.html <br>
> https://docs.ray.io/en/master/tune/tutorials/tune-pytorch-cifar.html

```python
from ray import tune
from ray.tune import CLIReporter
from ray.tune.schedulers import ASHAScheduler
from ray.tune.suggest.hyperopt import HyperOptSearch

config_space = {
  "NUM_EPOCH": tune.choice([4, 5, 6, 7, 8, 9]),
  "LearningRate": tune.uniform(0.0001, 0.001),
  "BatchSize": tune.choice([32, 64, 128])
}
search = HyperOptSearch(metric='accuracy', mode='max')
reporter = CLIReporter(
  parameter_columns=["NUM_EPOCH", "LearningRate", "BatchSize"],
  metric_columns=["accuracy", "loss"]
)
NUM_TRIAL = 10
scheduler = ASHAScheduler(
  metric="loss",
  mode="min",
  max_t=epochs,
  grace_period=1,
  reduction_factor=2
)

tune.run(
  some_train_func,
  config=config_space,
  search_alg=search,
  progress_reporter=reporter,
  num_samples=NUM_TRIAL,
  scheduler=scheduler,
  resources_per_trial={'gpu': 1}
)
```

자동으로 여러 hyperparameter 후보들을 대입해서 실험을 해주는 것은 좋지만, 매번 랜덤한 조합으로 실험을 하기 때문에 실험을 유력한 후보부터 순서대로 해주지는 않는다. 하지만 스케쥴러 등을 잘 사용하면 매우 유용할 것으로 보인다.

## 일지

### Daily scrum (10:00-10:10)

### 과제 수행 (10:10-12:00)

  * [과제] PyTorch Basics for AI
    * Transfer Learning & Parameter Tuning

### 과제 수행 (13:00-15:20)

  * [과제] PyTorch Basics for AI
    * Transfer Learning & Parameter Tuning

### 강의 수강 (15:20-16:00)

  * [강의] PyTorch Basics for AI
    * Multi-GPU Learning

### Peer session (16:00-17:00)

  * 기본과제 #2 이야기
  * 심화과제 이야기
  * 다음 peer session 준비
    * 주간 회고 양식 작성해 오기

### 과제 정답 확인 및 비교 (17:00-17:30)

### 강의 수강 (17:30-18:00)

  * [강의] PyTorch Basics for AI
    * Hyperparameter Tuning

### Office hour (18:00-19:20)

  * 과제 해설
  * torch.gather() 설명

### Daily report 작성 (19:20-20:00)

### 보충 학습 (20:00-22:00)

> https://dacon.io/competitions/official/235869/overview/description

  * Dacon Basic 참가
