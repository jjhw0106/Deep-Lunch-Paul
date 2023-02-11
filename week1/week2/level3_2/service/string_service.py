from typing import List

# 카운트 김~
# 카운트 name
# 중복제거
# 중복제거 후 문자열 정렬
def count_with_family_nm(names:List[str], family_nm:str):
    '''성으로 카운트 세기'''
    count = 0
    for name in names:
        if name.startswith(family_nm):
            count+=1
    return count

def count_with_full_nm(names:List[str], full_name:str):
    '''이름으로 카운트 세기'''
    count = 0
    for name in names:
        if(name == full_name):
            count+=1
    return count
    
def remove_dup(names:List[str]):
    '''중복 제거'''
    return set(names)
    
if __name__ =="__main__":
    pass