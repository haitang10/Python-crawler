#quadratic.py
import math
def main():
    print("Let us finds the solution to a quadratic")
    a,b,c=eval(input("\nDo enter the coefficients (a,b,c):"))
    delta=b*b-4*a*c
    if delta < 0:
        print("\n The equation has no real roots!")
    elif delta ==0:
        x=-b/(2*a)
        print("\n There is a double toot at",x)
    else :
        discRoot=math.sqrt(delta)
        x1=(-b+discRoot)/(2*a)
        x2=(-b-discRoot)/(2*a)
        print("\n The solution are:",x1,x2)
main()
