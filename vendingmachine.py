price = 150
sum = 0
coincount = 0

def change(sum):
    change = price - sum
    return(change)




while True:
    n = int(input("Please use one of the coins, 1, 5 , 10 or 20"))
    coincount = coincount + 1
    if n == 1 or n == 5 or n == 10 or n== 20:
        sum = sum+n
    else:
        print("this is not a valid coin, please try again")
    if sum >= 150:
        print("the change is", change(sum))
        break

print("You have paid all the money, thank you!")

