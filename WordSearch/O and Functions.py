"""
def checknums(x, y):
    if x*y > 25:
        return True
    else:
        return False

x = int(input("give me nummies "))
y = 20
print(checknums(x, y))
"""

""""
with open("odd.txt", "a") as odd:
    for i in range(1, 10):
        if i % 2 == 0:
            continue
        else:
            odd.write(str(i)+"\n")
odd.close()
"""

"""
def readfile(sum):
    file = open("odd.txt", "r")
    data = file.readlines()
    for i in range(0, 5):
        sum += int(data[i])
    return sum
sum = 0
print(readfile(sum))
"""

"""
from random import randint

def mainp(rand):
    with open("odd.txt", "r+") as odd:
        odd.write(str(rand))
        check = odd.readlines()
        guess = input("guess a number between 1 and 15 ")
        if guess == check[0]:
            print("you got it")
        else:
            print("not right")


rand = randint(0, 15)
print(mainp(rand))
"""
words = [i.strip().split() for i in open("5words.txt").readlines()]
print(words)
print(words[0][0][0])
