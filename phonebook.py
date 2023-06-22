d={}
def phnbk(d):
    print("\n----- PHONE BOOK -----")
    x=print(" 1.Create \n 2.Display \n 3.Delete \n 4.Update \n 5.Exit")
    ch=int(input("Enter your choice:"))

    xy(x,ch,d)
    
    
def xy(x,ch,d):
    if ch==1:
        name=input("\nName:")
        if name not in d :
            
            phn=input("Phone Number:")
            d[name]=phn
            print("\nAdd Successfully.....!")
            phnbk(d)
        else:
            print("\nAlready Exist...!")
            phnbk(d)

    
    
    elif ch==2:
        print("\n----- Contact List -----")

        for i in d:
            print(i,":",d[i])
        phnbk(d)
    
    
    elif ch==3:
        dt=input("\nEnter Name to Delete: ")
        if dt in d:
            d.pop(dt)
            print(" \nDeleted successfully...!")
            phnbk(d)
        else:
            print(dt," is not in Your Contact ")
            phnbk(d)


    elif ch==4:
        upn=input('\n What is Update Name : ')
    
        
        if upn in d:
              k=input("Enter the New Name  :")
              v=int(input("Enter the New Number :"))
              d.update({k:v})
              phnbk(d)
        else:
            print(upn," is not in Your Contact ")
            phnbk(d)


    elif ch==5:
        exit()


    else:
        print("\nInvalid Choice!. Please Check.....")

phnbk(d)