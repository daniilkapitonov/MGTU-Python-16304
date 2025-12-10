def convert(temp):
    print('-----------------')
    far = temp*9/5+32
    # if far >= 40:
    #     return far
    # else:
    #     return 0 
    return far
    

cel = int(input("Cel - "))
converted_temp = convert(cel)

convert(cel)

print(converted_temp)