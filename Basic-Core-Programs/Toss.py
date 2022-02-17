import random

def HeadTailPer(number):
    '''
    Prints Percentage of Head and Tail.
    :param number: Number of times coin is tossed
    :return: Null
    '''
    head_count = 0
    tail_count = 0
    for i in range(0, number):
        toss_result = random.randint(0, 1)
        if toss_result == 0:
            tail_count += 1
        if toss_result == 1:
            head_count += 1
    print(f"Percentage of Head:{(head_count/number)*100}\nPercentage of tail:{(tail_count/number)*100}")

number = int(input("Enter Number of times you toss:"))
HeadTailPer(number)