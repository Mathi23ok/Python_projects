print("::::::::::::::::::::TO-DO LIST:::::::::::::::::::::::")
list1 = []
def add():
    s = input("\nEnter the task :")
    list1.append(s)
    print("\nTask added")
def view():
    if len(list1)==0:
        print("\nNo tasks yet")
    else:
        print("\nTasks:")
        for index,task in enumerate(list1,start = 1):
            print(f"{index}.{task}")

def delete():
    if len(list1)==0:
        print("\nNo tasks to delete")
        return
    view()
    try:
        index = int(input("\nEnter the task number to delete :"))
        if 1<=index<=len(list1):
            list1.pop(index-1)
            print("\nTask deleted")
        else:
            print("\nInvalid Task number")
            
    except ValueError:
        print("Enter a valid number")        
def to_do(n):
    if n==1:
        add()
    elif n==2:
        view()
    elif n==3:
        delete()
    elif n ==4:
        print("\nExiting the To-Do list ^-^")
        return False
    else:
         print("Enter a valid input")
    return True
while True:
    try:
        print("\n1.Add Task")
        print("2.View Task")
        print("3.Delete Task")
        print("4.Exit")
        
        num = int(input("\nEnter your choice :"))
        if not to_do(num):
            break
    except ValueError:
        print("Enter a valid number")
        
        
        
