# 1 e3 = 1 * 10^3
# 10억
print(1e3)
# 3.954
print(3954e-3)

# 반올림
a = 0.05439
print(round(a,4))

# x^y
x = 5
y = 3
print(x ** y)

# 리스트 초기화
n = 10
a = [4] * n
print(a)

# 리스트 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = a[0:4] # 0번이상 4번 미만 인덱스 
print(b)

# ================ 리스트 컴프리헨션 ================
# 대괄호([])안에 조건문과 반복문을 넣어 초기화
# 0부터 19 중 홀수만 포함하는 리스트
# oddList = [i for i in range(20) if i % 2 == 1]
oddList = [i for i in range(20) if i%2 == 1]
print(oddList)

# 1부터 9까지의 제곱값
squareList = [i*i for i in range(9)]
print(squareList)

# 2차원 배열 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)
# cf) "_" => 변수의 값을 무시할 때 사용
# for _ in range(5):
#   print('hello')          => hello 5번 출력

array2 = [[0 for i in range(5)] for u in range(10)]
print(array2)
# ===================================================

# 파이썬에서 모든 원소 지우기
# 파이썬은 remove_all()을 지원하지 않는다.
# remove_set에 없는 애들만 result에 넣는 방식으로 진행
a = [1,2,3,4,5,5,5]
remove_set = [3,5]
array3 = [i for i in a if i not in remove_set]
print(array3)

# 문자열 연산
a = "Hello"
b = "World"
print(a + " " + b)
print(a*3)
# 문자열은 내부적으로 리스트처럼 처리
c = 'abcdef'
print(c[2:4])

# 튜플과 리스트의 차이
# 튜플은 선언된 값을 변경할 수 없다
# 튜플은 소괄호()를 사용한다.
tuple = (1,2,3,4)
print(tuple, tuple[2])
# tuple[2] = 10 => 에러 발생, 튜플 값 변경 불가

# 함수 밖에 선언된 변수(전역 변수)를 변경하기 위해선 함수 내부에서 
# global 키워드를 이용하여 변수를 초기화 해줘야 한다.
globalVar = 20
def funcGlo():
    global globalVar
    globalVar = 256
    print(globalVar)

funcGlo()
print(globalVar)

# 백준 파이썬 입출력받기
# vs code에서는 디버그 모드로 실행시켜야 파이썬 입출력이 실행된다
# num = int(input('숫자를입력하세요:'))
# data = list(map(int, input().split()))
# a, b, c = map(int, input().split())

# map함수
# map(function, iterable한 객체)
# 객체를 돌면서 요소 각각을 function에 매개변수로 전달하여 결과값을 return
a = [1,2,3,4,5]
def x3(e):
    return e*3
print(list(map(x3, a)))
print(list(map(int, '12345')))
# result = list(map(function(x){return x*3}, a))
# print("Ff",result)
    