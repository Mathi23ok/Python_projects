print(":::::::::Simple Calculator:::::::::")
def calc(a,b,operation):
    if operation == '+':
        print(a+b);
    elif operation == '-':
        print(a-b);
    elif operation == '*':
        print(a*b);
    elif operation == '/':
        if b==0:
            print("we cannot divide by zero");
        else:
            print(a/b);
    else:
        print("Please enter a valid operation !")
        
while True:
  try:
    num1 = float(input("Enter the Number 1: "));
    num2 = float(input("Enter the Number 2: "));
    operation = input("Enter the operation(+,-,*,/) : ");
    result  = calc(num1,num2,operation);

    repeat = input("Do you want to perform another operation ?(yes/no)").lower();
    if(repeat!="yes"):
      print("Thank you come again ^-^");
      break;
  except ValueError:
    print("Please enter a valid number !");
    continue      
    
