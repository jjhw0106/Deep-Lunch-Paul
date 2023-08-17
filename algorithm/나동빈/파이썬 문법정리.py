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
oddList = [i for i in range(20) if i % 2 == 1]
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

# ===================================================