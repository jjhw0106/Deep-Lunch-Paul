print("hello world")

# 모듈 import
import math
import random

# random값 뽑기
print(random.random())

# 여러 줄 print
print('''
      Hello
      World
      ''')

# 문자열 반복
print('Hello World' * 100)

# 문자 len구하기
print(len('Hello world'))

# 문자열 replace
print('Hello world'.replace('world', 'universe'))

# List만들기
students = ['Mike','Jack','Egoing']
print("students[1]:", students[1])

# List에서 가장 큰,작은 값 찾기
grades = [2,109,34,55]
print(max(grades), min(grades))

# 통계 모듈
import statistics
print(statistics.mean(grades)) # 평균

# random으로 List의 랜덤값 뽑아내기
print(random.choice(students))

# 입출력
name = input('글자를 입력하세요: ')
print(name)

# pandas 패키지 import하기
# 파이썬 패키지 검색하기 -> PyPI : 파이썬 패키지 찾는 사이트
# pandas 설치
# Terminal : python3 -m pip install pandas라고 작성 (pip프로그램이 pypi에서 pandas 라이브러리르 찾아서 설치)
import pandas
house = pandas.read_csv('house.csv') # csv파일 읽어서 house에 대입
print(house)
print(house.head(2)) # 위 두개
print(house.describe) # 각 컬럼의 통계자료 요약

# 3항 연산자
print("참") if 1 else print("거짓")