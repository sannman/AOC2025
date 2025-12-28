def main():
    user_input = "269351-363914,180-254,79-106,771-1061,4780775-4976839,7568-10237,33329-46781,127083410-127183480,19624-26384,9393862801-9393974421,2144-3002,922397-1093053,39-55,2173488366-2173540399,879765-909760,85099621-85259580,2-16,796214-878478,163241-234234,93853262-94049189,416472-519164,77197-98043,17-27,88534636-88694588,57-76,193139610-193243344,53458904-53583295,4674629752-4674660925,4423378-4482184,570401-735018,280-392,4545446473-4545461510,462-664,5092-7032,26156828-26366132,10296-12941,61640-74898,7171671518-7171766360,3433355031-3433496616"
    ranges = user_input.split(",")
    total_sum = 0
    
    for range_str in ranges:
        stnumber, ndnumber = map(int, range_str.split("-"))
        dublicate_numbers_list = []
        for num in range(stnumber, ndnumber+1):
            if dublicate(num):
                dublicate_numbers_list.append(num)
                print(f"Found dublicate number: {num}")
        range_sum = sum(dublicate_numbers_list)
        total_sum += range_sum
        print(f"Sum for range {range_str}: {range_sum}")
    
    print(f"Total sum of all dublicate numbers: {total_sum}")





def dublicate(num):
    num_str = str(num)
    num_len = len(num_str)
    
    # Try all possible pattern lengths (1 to half the length)
    for pattern_len in range(1, num_len // 2 + 1):
        if num_len % pattern_len == 0:
            pattern = num_str[:pattern_len]
            repeat_count = num_len // pattern_len
            if pattern * repeat_count == num_str:
                return True
    
    return False





main()