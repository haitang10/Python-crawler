def addinterest(balance,rate):
    newBalance = balance * (rate + 1)
    balance = newBalance
    return balance
def main():
    amount = 1000
    rate = 0.05
    amount = addinterest(amount,rate)
    print(amount)
main()
