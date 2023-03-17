import model.input_list as inputs
def main():
    minus_list = []
    plus_list = []
    input_list = inputs.inputList
    answer_list = []
    
    for val in input_list:
        # 3항연산자 비추
        # minusList.append(val) if val<0 else plusList.append(val)
        if val<0:
            minus_list.append(val)
        else:
            plus_list.append(val)
    
    # answer_list = minus_list.extend(plus_list)
    # list.extend()메소드는 return type이 없다
    answer_list = minus_list + plus_list
    print(answer_list)
   
if __name__=="__main__":
    main()
