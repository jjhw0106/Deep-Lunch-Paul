n = 20 # 총 빈병 
a = 2 # 빈병
b = 1 # 콜라
answer = (n//a*b)
while(1):
    if n<a:
        break
    answer += (n%a + b*(n//a))
    n = n%a
    n += n//a
    print(answer)   
