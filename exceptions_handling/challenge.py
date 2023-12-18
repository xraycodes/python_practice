



def func():
    while True:
        try:
            num1 = int(input("number 1 "))
            num2 = int(input("number 2 "))
            ans = num1 / num2
            return ans
        except:
            print("Error used, enter valid number")
    
print(func())