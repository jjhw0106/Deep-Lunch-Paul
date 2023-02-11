import service.string_service as service
import model.input_list as inputs

def main():
    print(service.count_with_family_nm(inputs.name_list, '김'),service.count_with_family_nm(inputs.name_list, '이'))
    print(service.count_with_full_nm(inputs.name_list, '이재영'))
    print(service.remove_dup(inputs.name_list))
    # print(list(service.remove_dup(inputs.name_list)).sort()) -> return 값이 없어서 출력x
    sorted_list=list(service.remove_dup(inputs.name_list))
    sorted_list.sort()
    print(sorted_list)
    
    
if __name__ == "__main__":
    main()