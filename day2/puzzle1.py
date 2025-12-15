def main():
    user_input = input("Enter the range: ")
    stnumber , ndnumber = map(int, user_input.split("-"))
    dublicate_numbers_list = []
    for num in range(stnumber, ndnumber+1 ):
        if dublicate(num):
            dublicate_numbers_list.append(num)
            print(f"Found dublicate number: {num}")
    sum = 0
    for i in range(len(dublicate_numbers_list)):
        
        sum += dublicate_numbers_list[i]
    print(f"Sum of dublicate numbers: {sum}")



def dublicate(num):
    num_len = len(str(num))
    half_len = num_len//2
    list_first_half=[]
    list_second_half=[]
    for i in range(num_len):
        if i < half_len:
            list_first_half.append(str(num)[i])
        else:
            list_second_half.append(str(num)[i])
    if list_first_half == list_second_half:
        return True
    else:
        return False


main()