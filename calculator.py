
a=float(input("enter first number"))
operator=input("enter operator (+, -, *, /, %)")
b=float(input("enter second number"))
if operator =="+":
    result=a+b


elif operator =="-":
    result=a-b


elif operator =="*":
    result=a*b


elif operator=="/":
    if b !=0:
        result=a/b
    else:
        result="cannot divided by zero"

elif operator=="%":
    if b !=0:
        result=a%b
    else:
     result="cannot divided by zero"


else:
 result="invalid operator"
print("result=",result)
