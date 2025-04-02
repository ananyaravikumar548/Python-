def temperature_converter():
    print('temperature')
    temp=float(input('enter temperature'))
    print("convert")
    print("1.C to F")
    print("2.F to C")
    choice =input("enter choice")
    if choice == '1':
        fahrenhiet= (temp*9/5)+32
        print(fahrenhiet)
    elif choice =='2':
        celsius =(temp-32)*5/9
        print(celsius)
    else :
        print('invalid input')
temperature_converter()
