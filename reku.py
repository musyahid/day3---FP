def decrement(number) :
    if number == 0 :
        return  
    else :
        print(number)
        decrement(number - 1)

decrement(5)