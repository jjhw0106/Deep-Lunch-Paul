def solution(phone_book):
    answer = True
    
    phone_book.sort(key = len)
    
    checkLen = len(phone_book[0])
    target = phone_book[0]
    
    for e in enumerate(phone_book, start=1):
      # print(type(e))
      if e[1][0:checkLen] == target:
        return False
      # checkLen = len(e)
      # target = e
      
      
    
    # print(phone_book)
    
    
    return answer
  
solution(["119","1195524421" ,"97674223" ])
  
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"] false