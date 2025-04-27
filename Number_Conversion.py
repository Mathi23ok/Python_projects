print(":::::::::Number Conversion System:::::::::")
def number_converter(a):
  print("Decimal value : ",a);
  print("Binary value: ",bin(a)[2:]);
  print("Octal value : ",oct(a)[2:]);
  print("Hexadecimal Value : ",hex(a)[2:].upper())

while True:
  try:
    num = int(input("Enter the Number for conversion : "));
    number_converter(num);
 
    repeat = input("Do you want to convert another number ?(yes/no)").lower();
    if(repeat!="yes"):
      print("Thank you come again ^-^");
      break;
      
  except ValueError:
    print("Please enter a valid integer !");
    continue    
    
