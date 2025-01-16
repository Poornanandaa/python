def fibanocciSeries(num):
    # 0 1 1 2 3 5 8 13 21 34

    if num == 1:
        print(0)
        return
    
    firstNum = 0
    secondNum = 1
    print(firstNum)
    print(secondNum)
    for number in range(2, num):
        nextNum = firstNum + secondNum
        print(nextNum)
        firstNum = secondNum
        secondNum = nextNum

num = int(input("Enter a number:"))
fibanocciSeries(num)