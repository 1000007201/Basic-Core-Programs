
def PowofTwo(number):
    '''
    Prints power of two upto given number
    :param number: upto which we need power of two.
    :return:NULL
    '''
    for i in range(1, number+1):
        print(f"2 ^ {i} = {2**i}")

number = int(input("Enter maximum number of power:"))
PowofTwo(number)