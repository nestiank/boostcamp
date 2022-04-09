# Day22 (2022/02/15)

## 노트

### Docker

#### Docker Commands

  * docker pull image_name:tag
  * docker images
  * docker inspect
  * docker build dockerfile_location -t image_name:tag
  * docker run --name container_name image_name:tag
    * d: daemon mode
    * i: interactive mode
    * t: activate tty
    * p: host_port:container_port
    * v: host_folder:container_folder
  * docker attach
  * docker ps -a
  * docker exec -it container_name /bin/bash
  * docker stop container_name
  * docker rm container_name

#### Requirements

  * pip freeze > requirements.txt
  * pip list --not-required --format=freeze > requirements.txt

#### Dockerfile

```Dockerfile
FROM image_name:tag

COPY . /app
WORKDIR /app
ENV PYTHONPATH /app
ENV PYTHONBUFFERED=1

RUN pip install pip==21.2.4 && \
    pip install -r requirements.txt

CMD ["python", "main.py"]
```

  * RUN: Build process
  * CMD: Mutable initial process
    * docker run image_name:tag echo hello = echo hello
  * ENTRYPOINT: Immutable initial process
    * docker run image_name:tag echo hello = python main.py echo hello
    * May cause error

### MLflow

#### MLflow Commands

  * mlflow experiments create --experiment-name experiment_name
  * mlflow experiments list
  * mlflow run mlproject_location --experiment-name experiment_name --no-conda
    * P: passing an argument
  * mlflow ui
  * mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root $(pwd)/artifacts
    * export MLFLOW_TRACKING_URI="http://127.0.0.1:5000"

#### MLflow Autolog

```python
from sklearn.linear_model import LogisticRegression
import mlflow
import mlflow.sklearn

if __name__: '__main__':
  mlflow.sklearn.autolog()

  lr = LogisticRegression(solver=sys.argv[1], penalty=sys.argv[2], l1_ratio=float(sys.argv[3]))

  with mlflow.start_run() as run:
    lr.fit(X, y)

  score = lr.score(X, y)
```

#### MLProject

```
name: project_name
entry_points:
  main:
    parameters:
      solver:
        type: string
        default: "saga"
      penalty:
        type: string
        default: "l2"
      l1_ratio:
        type: float
        default: 0.1
    command: "python main.py"
```

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] AI Service Development Basics
    * Docker
    * MLflow

### 어제의 daily report 보충 (13:00-15:00)

### Daily report 작성 (15:00-16:00)

### Peer session (16:00-17:00)

  * 다음 peer session 준비
    * 내일까지 data structure 면접 질문 공부해 오기
    * 다음 주 월요일까지 ViT 구현해 오기

### 커뮤니티 세션 (17:00-18:20)

  * 대학원 입학 관련 이야기
  * 스마트 팩토리 이야기

### Daily report 작성 (18:20-19:00)

### Mentoring (19:00-20:00)

  * Swish Activation 소개
  * 사전 질문들에 대한 답변
