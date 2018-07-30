n=eval(input("How many numbers are there ?"))
sum = 0.0
for i in range (n):
    x=eval(input("Enter a number:"))
    sum = sum + x
print("\n The average is:",sum/n)
