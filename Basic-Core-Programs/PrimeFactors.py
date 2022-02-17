
def primeFactors(number):
    '''
    Prints Prime factor of given number
    :param number:
    :return: Null
    '''
    while number % 2 == 0:
        print(2,)
        number = number / 2

    for i in range(3, int(number**(1/2)) + 1, 2):

        while number % i == 0:
            print(i,)
            number = number / i

    if number > 2:
        print(number)


number = int(input("Enter number:"))
print(primeFactors.__doc__)
primeFactors(number)
