def solution(input_string):
    answer = ''
    if len(input_string) == 1:
      return input_string
    
    new_input = ''
    for idx, e in enumerate(input_string):
      if e == input_string(idx+1):
        new_input.join('')
        print(new_input)
        
    return answer
  
  
solution('aabbccc')