import os,time

myToDoList = []

def printToDoList():
  print() 
  for item in myToDoList:
    print(item)
  print() 

while True:
  print("ToDo List Manager")
  print()
  print("Do you want to view, add, edit or remove the todo list?")
  show = input("Enter 'view', 'add', 'edit' or 'remove': ")
  
  if show == "view":
    printToDoList()
    time.sleep(5)
    os.system("clear")
  elif show == "add":
    item = input("Who should I add to the ToDo list?: ")
    myToDoList.append(item)
    print()
    print(f"{item} was added to the ToDo list")
    time.sleep(3)
    os.system("clear")
  elif show == "edit":
    printToDoList()
    item = input("Who should I edit in the ToDo list?: ")
    index = myToDoList.index(item)
    item = input("What should I replace it with?: ")
    myToDoList[index] = item
    print()
    print(f"{item} was edited in the ToDo list")
    time.sleep(3)
    os.system("clear")
  elif show == "remove":
    item = input("Who should I remove from the ToDo list?: ")
    if item in myToDoList:
      confirm = input("Are you sure you want to remove this item? (yes/no): ")
      if confirm == "yes":
        myToDoList.remove(item)
        print()
        print(f"{item} was removed from the ToDo list")
    else:
      print()
      print(f"{item} was not in the ToDo list")
    time.sleep(3)
    os.system("clear")