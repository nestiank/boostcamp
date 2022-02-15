# Day21 (2022/02/14)

## 노트

### Project Lifecycle

<details>
<summary>Problem Solving Flow</summary>

#### Problem Validation

  * 풀어야 할 문제
    * 패턴이 분명하고 복잡한 문제
    * 목적 함수를 만들기 좋은 문제
    * 데이터를 구하기 좋은 문제
    * 자동화가 가능한 반복 작업이 요구되는 문제
  * 피해야 할 문제
    * 비윤리적인 문제
    * 너무 간단하여 패턴이 없는 문제
    * 데이터를 구하기 매우 어려운 문제
    * 오류의 결과가 치명적인 문제
    * 설명가능성이 중요한 문제
    * 비용의 관점에서 모델링이 비효율적인 문제

#### Project Design

  * 현상 파악
  * 문제 정의
    * 사용 가능한 기존의 솔루션 탐색
    * 데이터로 해결할 수 있는 방법인지 확인
    * 필요한 데이터의 보유 여부 확인
    * 간단한 방법부터 계획
  * 프로젝트 설계
    * 제약 조건 확인
      * 기술적 제약
      * 비용과 일정의 제약
      * 윤리적 제약 및 개인정보 관련 제약
      * 수용 가능한 오류의 한계의 제약
    * 최적화할 지표와 최적화 방식 설정
    * 평가 방법 정의
      * 평가에 사용할 지표 설정
      * 비교 대상이 될 베이스라인 설정
    * 비용을 고려하여 목표와 한계 설정
      * 목표들 간의 우선순위 설정
      * 목표별로 모델을 분리하여 학습
    * 일정을 고려하여 작업 순서 설정
    * 프로토타입 제작 및 테스트
      * Voila
      * Streamlit
      * Gradio

#### Project Execution & Evaluation

  * 프로젝트 진행
    * 데이터 수집
    * 데이터 무결성 확인
    * 모델 개발
    * 모델 학습
    * 모델을 서비스에 이식
    * 서비스 배포
  * 프로젝트 평가
    * A/B 테스트
    * 혹시 노이즈를 패턴으로 학습했는지 점검

#### Data Labeling

  * 레이블이 있는 경우: 바로 사용
  * 유사 레이블이 있는 경우: 양적 변수로 변환하여 사용
  * 레이블이 전혀 없는 경우: 레이블링하거나 self-supervised learning 진행

</details>

### Using Shell

<details>
<summary>Shell Commands</summary>

#### Bash Commands

  * man: manual
  * pwd: print working directory
  * bash: execute shell script
  * clear: not cls
  * history: shell commands history
    * !num: execute shell command with the number again
  * export: set environment variable
  * source: reload system setting file
    * source ~/.bashrc
  * alias
  * head
  * tail
  * sort
    * r: reverse order sort
    * n: numerical sort
  * uniq
  * grep
    * i: case-insensitive search
    * w: implicit word search
    * v: exclude given pattern
    * E: use regular expression
  * cut
    * f: field setting
    * d: seperator setting
  * ps -ef
  * curl: client url request
  * df: check disk capacity usage
  * scp: secure copy
    * scp local_path user@ip:remote_path
    * r: recursive copy
    * P: port setting
    * i: use ssh settings
  * nohup: no hangup due to session quit
    * &: background execution
    * 755 permission needed
  * chmod: change permission

#### Redirection & Pipe

  * Single angle bracket: overwrite
  * Double angle brackets: append
  * Vertical bar: pipe

#### Shell Script

> https://github.com/zzsza/shell-scripts

</details>

### Using Vim

<details>
<summary>Vim Commands</summary>

#### Command Mode

  * dd: remove current line
  * i: insert mode
  * x: remove current character
  * yy: copy current line
  * p: paste a line from clipboard
  * k: cursor up
  * j: cursor down
  * l: cursor right
  * h: cursor left

#### Insert Mode

  * ESC: command mode

#### Last Line Mode

  * w: save
  * q: quit
  * /: find
  * set nu: print line numbers

</details>

## 일지

### Daily scrum (10:00-10:10)

### 강의 영상 수강 (10:10-12:00)

  * [강의] AI Service Development Basics
    * Introduction
    * ML Project Lifecycle

### 강의 영상 수강 (13:00-16:00)

  * [강의] AI Service Development Basics
    * Linux & Shell Commands
    * AI & Copyright

### Peer session (16:00-17:30)

  * Transformer 정리 공유

### Daily report 작성 (17:30-19:00)
