
def ChickenMonkey():
    for num in range(0, 101):
        if num%5==0:
            print("chicken")
        elif num%7==0:
            print('Monkey')
        else:
            print(num)
    
ChickenMonkey()
