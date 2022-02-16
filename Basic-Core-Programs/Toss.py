import random
head_count = 0
tail_count = 0
number = int(input("Enter Number of times you toss:"))
for i in range(0, number):
    toss_result = random.randint(0, 1)
    if toss_result == 0:
        tail_count += 1
    if toss_result == 1:
        head_count += 1
print(f"Percentage of Head:{(head_count/number)*100}\nPercentage of tail:{(tail_count/number)*100}")
