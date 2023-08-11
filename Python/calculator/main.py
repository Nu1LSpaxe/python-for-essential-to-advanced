from calculator import Calculator
import sys

if len(sys.argv) != 4:
    print("You need to input two number and an operator, such as '2 + 3'.")
    sys.exit(1)
else:
    __filename, n1, operator, n2 = sys.argv
    n1, n2 = map(int, [n1, n2])
    
    cal = Calculator(n1, n2)
    result = ""

    if operator == "+":
        result = str(cal.add())
    elif operator == "-":
        result = str(cal.sub())
    elif operator == "*":
        result = str(cal.mul())
    elif operator == "/":
        result = str(cal.div())
    else:
        print("invalid operator")
        sys.exit(1)
    
    print("result is " + result)
