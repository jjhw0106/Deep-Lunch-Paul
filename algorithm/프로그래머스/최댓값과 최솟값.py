def solution(s):
    answer = ''
    
    a = s.split(' ')
    print(a)
    min = int(a[0])
    max = int(a[0])
    
    for e in a:
      if min > int(e):
        min = int(e)
      if max < int(e):
        max = int(e)
    # print("{} {}".format(min, max))
    return "{}".format(min, max)
  
solution("1 2 3 4")

"1 2 3 4"
"-1 -2 -3 -4"
"-1 -1"