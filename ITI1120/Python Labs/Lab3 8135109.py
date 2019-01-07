#1
def pay(wage, hours):
    if hours <= 40:
        return (hours*wage)
    elif hours > 40 and hours <= 60:
        return (40*wage + (hours - 40)*wage*1.5)
    else:
        overtimehours = hours - 60
        finalpay = (overtimehours*wage*2) + (wage*40) + (wage*1.5*20)
    return finalpay

#2
def rps():
    player1 = input("input your move, player 1 ")
    player2 = input("input your move, player 2 ")
    if (player1 == "R" or player1 == "r") and (player2 == player1):
        return int(0)
    elif (player1 == "R" or player1 == "r") and (player2 == "s" or player2 == "S"):
        return int(-1)
    elif (player1 == "R" or player1 == "r") and (player2 == "P" or player2 == "p"):
        return int(1)
    elif (player1 == "S" or player1 == "s") and (player2 == player1):
        return int(0)
    elif (player1 == "S" or player1 == "s") and (player2 == "P" or player2 == "p"):
        return int(-1)
    elif (player1 == "S" or player1 == "s") and (player2 == "r" or player2 == "R"):
        return int(1)
    elif (player1 == "P" or player1 == "p") and (player2 == player1):
        return int(0)
    elif (player1 == "P" or player1 == "p") and (player2 == "R" or player2 == "r"):
        return int(-1)
    elif (player1 == "P" or player1 == "p") and (player2 == "S" or player2 == "s"):
        return int(1)
#3a
def is_divisable(n, m):
    if n % m == 0:
        return ("Your first value", n, "is divisable by", m)
    else:
        return ("Your first value", n"is divisable by", m)

#3b
def is_divisable23n8(x):
    x = n
    if is_divisable(n, 2) == True and is_divisable(n, 3) == True and is_divisable(n, 8) == False:
        print(n, "is divisable by 2 and 3 but not 8")
    else:
        print(n, "is not divisable by 2 and 3 but not 8")


