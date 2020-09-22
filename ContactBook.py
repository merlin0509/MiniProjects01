def cbook():
  print("you first have to save a contact\t\n")
  YN=True
  name=input("enter name of the person\n")
  number=int(input("enter contact number \n"))
  dict={name:number}
  print("contact saved")
  print(dict)
  while YN:
    Yno=int(input("If you want to add another contact press 1 \n if you want to refer address book press 2 \n if you want to delete contact press 3\n"))
    if Yno==1:
      name=input("enter name of the person\n")
      number=int(input("enter contact number\n"))
      dict1={name:number}
      dict.update(dict1)
      print(dict)
    elif Yno==2:
      namey=input("enter name of the person whose number you want to find\n")
      for i in dict:
        if i==namey:
          print(dict[namey])
    elif Yno==3:
      namei=input("enter name of the person whose number you want to delete\n")
      dict.pop(namei)
      print("deleted")
      print(dict)
cbook()
