def Harmonic():
    '''
    Taking Input of number from user.
    :return: Harmonic value of given number
    '''
    number = int(input("Enter value of number:"))
    harmonic = 0
    for i in range(1, number+1):
        harmonic += 1/i
    return harmonic

print(Harmonic())
print(Harmonic.__doc__)#Print Doc String of Function Harmonic.