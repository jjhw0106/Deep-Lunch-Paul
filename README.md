## 사용법
route.py : 프로그램 진입점, 실행 시 콘솔을 통해 라우팅<br>
basic.py : 파이썬 문법, tip 등 정리<br>
week1/.. : 각 주차 별 실행 파일<br>
...

## 딥런치 시작
___
1. OT <br>
- GIT 생성 및 연결
2. 함수 <br>
- 함수 사용법

COLAB  설치

- 구글 제공
- 구글 클라우드 서버에서 구동
- COLAB에서 작성한 파일은 노트북 파일이라 부르며, 구글 드라이브에 저장됨

Tensorflow

- import 및 version 확인
      import tensorflow as tf
      print(tf.__version__)

DataSet

- 속성 & 클래스
  - ex) 1 ~ 16의 속성이 주어지고 17번째에 결과값이 있다면, 1 ~ 16번은 속성, 17번째 결과는 클래스라 부름
- dataset
  - 집합은 대문자, 원소는 소문자로 표시
  - 속성 + 클래스 dataset
        X = Data_set[:,0:16] # [행 범위,열 범위]
  - 클래스 집합  datset
        y = Data_set[:,16] # 모든행의 17번째(클래스)만 담겠다.
    

케라스

- 텐서플로를 보다 쉽게 사용할 수 있도록 도와주는 역할
- models  클래스
  - Sequential()
  - 딥러닝은 여러 층이 정보를 주고받으며 출력층까지 전달되는 형태
  - add함수로 한층 한층을 쌓아올릴 수 있도록 제공
- layers  클래스
  - Dense() : 각 레이어의 입력과 출력을 촘촘하게 연결
