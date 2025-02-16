# Stationary-shop-management
import csv,tabulate
import mysql.connector as m

#Admin Mode
def create():
    db=m.connect(user="root",host="localhost",passwd='',database="record")
    mycur=db.cursor()
    mycur.execute("drop table password")
    mycur.execute("create table password (password char(10))")
    p=input("Enter a Password with 8-10 Characters:")
    mycur.execute("insert into password values (%s)",(p,) )
    db.commit()
    with open("customer.csv","w",newline='') as f:
        w=csv.writer(f)
        w.writerow(["Phone no.","Name","Amount Spent","Store Credit"])
    with open("items.csv","w",newline='') as f1:
        w1=csv.writer(f1) 
        l=["Item ID","Description","Brand","Stock","SPrice","CPrice"]
        w1.writerow(l)
    with open("sales.csv","w",newline='') as f2:
        w2=csv.writer(f2) 
        w2.writerow(["Item ID","Quantity Sold","CP","Sp","Profit"])
    db.close()

def mode():
    db=m.connect(user="root",host="localhost",passwd='',database="record")
    mycur=db.cursor()
    mycur.execute("select * from password")
    for k in mycur: x=k[0]
    print("\tMODES\n1.Admin\n2.Customer")
    while True:
        mode=int(input("Enter Mode"))
        if mode in [1,2]:break
        else:print("invalid mode")
    if mode==1:
        for k in range (5):
            password=input("Enter Password")
            if password==x: break
            else: print("your Password Is Incorrect")
        else:
            mode=2
            print("You Can Log In As Customer")
    db.close()
    return mode

def search(d):
    with open("items.csv")as f:
        r=list(csv.reader(f)) ;l=[] ; temp=[]
        for k in r[1:]:
            if d.lower()==k[1].lower(): l+=[k[2]] ;temp+=[k[0]]
        if len(l)==1: return int(temp[0])
        elif len(l)==0: print("No Such Product") ;return 0
        else:
            print("The Product Is Available Brands:",end='')
            for k in l:
                print(k,end=',')
            b=input("\nEnter Brand")
            for k in range(len(l)):
                if l[k].lower()==b.lower():
                    return int(temp[k])
            print("Invalid")
            return 0

def genID():
    try:
        with open("items.csv","r") as f:
            r=csv.reader(f)
            l=list(r)
            return int(l[-1][0])+1
    except: return 100

def add():
    with open("items.csv","a",new='') as f1,open("sales.csv","a",new='') as f2:
        w1=csv.writer(f1)  ; w2=csv.writer(f2)
        d=input("Enter Product Description: ")
        b=input("Enter Brand: ")
        s=int(input("Enter Stock: "))
        sp=int(input("Enter Selling Price: "))
        cp=int(input("Enter Cost Price: "))
        id=genID()
        w1.writerow([id,d,b,s,sp,cp])
        w2.writerow([id,0,cp,sp,0])
    print("It Has Been Added with ID",id)

def view_stock(n):
    with open("items.csv","r") as f:
        l=[] ; r=list(csv.reader(f))
        for k in r[1:]:
            if int(k[3])<=n: l+=[k]
    if l: print(tabulate.tabulate(l,r[0]))
    else: print("All items have stock greater than",n)

def inc_stock():
    id=int(input('enter item id:'))
    with open('items.csv') as f:
        s=int(input('enter new stock:'))
        r=list(csv.reader(f))
        for k in r[1:]:
            if int(k[0])==id:
                k[3]=int(k[3])+s
                print("stock has incremented")
                break
        else: print('invalid id')
    with open('items.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerows(r)

def mod_p(x):
    id=int(input('enter item id.'))
    with open('sales.csv','r') as f:
        r=list(csv.reader(f))
    with open('sales.csv','w',newline='') as f:
        for k in r[1:]:
            if int(k[0])==id:
                k[x]=int(input('enter modified price:'))
                print('price has been changed')
                break
        else:
            print('invalid id')
        w=csv.writer(f)
        w.writerows(r)

def view_profit():
    with open("sales.csv") as f1,open('items.csv') as f2:
        l=[];p=0
        r1=list(csv.reader(f1)); r2=list(csv.reader(f2))
        for k in r1[1:]:
            for j in r2[1:]:
                if k[0]==j[0]:
                    l+=[[k[0],j[1],k[1],k[4]]]; p+=int(k[4])
        print(tabulate.tabulate(l,["Item ID","Item Name",'Quantity','Profit']))
        print("Total Profit",p)

def buy_bill():
    c=0 ; bill=[] ;t=[]
    with open("items.csv") as f ,open("sales.csv") as f1:
        f2=open("customer.csv") 
        r=list(csv.reader(f)) ; r2=list(csv.reader(f2))
        r1=list(csv.reader(f1))
        f2.close()
        pn=int(input("Enter Phone No."))
        while True:
            n=input("Enter Product ID (if you don't remember ID Enter *)")
            if n=="*": d=input("Enter Description") ;id=search(d)
            else: id=int(n)
            if id==0:
                continue
            for k in r[1:]:
                if int(k[0])==id:
                    q=int(input("Enter Quantity"))
                    bill+=[k[0:3]+k[4:5]+[q]+[int(k[4])*q]]
                    k[3]=int(k[3])-q
                    c+=(int(k[4])*q)
                    t+=[q]
                    break
            else: print("Invalid ID")
            for k in r1[1:]:
                if int(k[0])==id:
                    k[1]=int(k[1])+q
                    k[4]=int(k[4])+q*(int(k[3])-int(k[2]))
                    break
            print("Current Total:",c)
            x=input("Do you want to buy another item(y/n)")
            if x in "Nn": break
            elif x in "Yy" : continue
            else: print("invalid entry")
    with open("items.csv","w",newline='') as f:
        w=csv.writer(f)  
        w.writerows(r)
    with open("sales.csv","w",newline='') as f1:
        w1=csv.writer(f1)
        w1.writerows(r1)
    x=0; total=0
    for k in r2[1:]:
        if pn==int(k[0]):
            name=k[1] 
            temp=int(k[3])
            k[2]=int(k[2])+total
            if int(k[2])>1000: k[2]=int(k[2])-1000 ; k[3]=int(k[3])+10
            break
    else:
        temp=0 
        name=input("Enter Name")
        r2+=[[pn,name,total,0]]
    print("\t\tBill\nCustomer Name:",name)
    for k in bill:
        total+=int(k[3])*(t[x])
        x+=1
    print(tabulate.tabulate(bill,['ID','Description','Brand','Unit Price','Quantity','Total']))
    print("Total=Rs.",total)
    for k in r2[1:]:
        if pn==int(k[0]):
            k[2]=int(k[2])+total
            if int(k[2])>1000: k[2]=int(k[2])-1000 ; k[3]=int(k[3])+10
            break
    with open("customer.csv","w",newline='') as f:
        w=csv.writer(f)
        w.writerows(r2)
    pay(total,temp)

def change():              
    mydb=m.connect(user="root",host="localhost",passwd='',database="record")
    mycur=mydb.cursor()
    mycur.execute("select * from password")
    p=input("Enter old Password")
    for k in mycur: y=k[0]
    if p==y:
        x=input("Enter new password")
        mycur.execute("update password set password=%s",(x,))
        mydb.commit()
    else: print("Your Password is incorrect")
    mydb.close()

def create_p():
    with open("sales.csv") as f:
        r=list(csv.reader(f))
        for k in r[1:]:
            k[0]=0 ; k[3]=0
    with open("sales.csv","w") as f:
        w=csv.writer(f)
        w.writerows(r)
    print("New sales record has been created and old sales record has been\ deleted")

def pay(c,p=0):
    while True:
        print("\tOPTIONS\n1.Cash\n2.Card\n3.Store Credit/Coupons")
        print("Your Points:",p)
        x=int(input("Enter Choice"))
        if x==1:
            y=int(input("Enter Money Taken"))
            print("Change= Rs.",y-c)
            break
        elif x==2:
            y=int(input("Enter Card no."))
            p=int(input("Enter PIN"))
            print("Payment Done")
            break
        elif x==3:
            if p>c:
                with open("Customer.csv") as f:
                    r=list(csv.reader(f))
                    for k in r[1:]:
                        if pn==int(k[0]):
                            k[3]=int(k[3])-c
                            break
            else:print("You Don't Have Enough Points")
        else: print("Invalid Entry")
        with open("Customer.csv","w",newline='') as f:
            w=csv.writer(f)
            w.writerows(r)
            
def exchange(x,y=1):
    with open('items.csv') as f:
        r=list(csv.reader(f))
        for k in r[2:]:
            if int(k[0])==x:
                temp=int(k[4])
                k[3]=int(k[3])+y
                break
        else: print('invalid id')
    with open('items.csv','w',newline="") as f:
        w=csv.writer(f)
        w.writerows(r)
    with open('customer.csv') as f:
        r=list(csv.reader(f))
        ph=int(input('enter ph.number:'))
    for k in r[1:]:
        if int(k[0])==ph:
            k[3]=int(k[3])+temp*y
            print('exchange has been done')
            break
    else: print('invalid phone no.')
    with open('customer.csv','w',newline='') as f:
        w=csv.writer(f)
        w.writerows(r)

def coupon(x):
    p=int(input("Enter Phone No."))
    with open("customer.csv") as f:
        r=list(csv.reader(f))
        for k in r[1:]:
            if int(k[0])==p:
                k[3]=int(k[3])+x
                break
        else:
            print("invalid ph no. credit  not incremented")
            return
    with open("customer.csv","w",newline="") as f:
        w=csv.writer(f)
        w.writerows(r)
    print("Credit was incremented")  

def viewc(x=0):
    with open("customer.csv") as f:
        r=list(csv.reader(f)) ; l=[]
        for k in r[1:]:
            if k[2]>=x:l+=[k]
    print(tabulate.tabulate(l,r[0]))
    
#Customer Mode
def view():
  with open('items.csv') as f:
     r=list(csv.reader(f))
     print(tabulate.tabulate(r[1:],r[0]))

def view_stock(n):
    with open("items.csv","r") as f:
        l=[] ; r=list(csv.reader(f))
        for k in r[1:]:
            if int(k[3])<=n: l+=[k]
    if l: print(tabulate.tabulate(l,r[0]))
    else: print("All items have stock greater than",n)

def view_b(b):
    with open('items.csv')as f:
        l=[]; r=list(csv.reader(f))
        for k in r[1:]:
            if k[2].lower()==b.lower(): l+=[k]
    if l:print(tabulate.tabulate(l,r[0]))
    else:print('No product in brand',b)

def view_d(d):
    with open('items.csv')as f:
        l=[]; r=list(csv.reader(f))
        for k in r[1:]:
            if k[1].lower()==d.lower(): l+=[k]
    if l:print(tabulate.tabulate(l,r[0]))
    else:print('No product with description',d)

def view_p(ll,ul):
    with open("items.csv") as f:
        l=[]; r=list(csv.reader(f))
        for k in r[1:]:
            if ll<=int(k[4])<=ul: l+=[k]
    if l:print(tabulate.tabulate(l,r[0]))
    else: print("No Products in Price",ll,"to",ul)

#MAIN PROGRAM
create()
if mode()==1:
    print("\tMenu\n1.Create New Product List\n2.Add")
    print("3.View Stock less than 'n'")
    print("4.View profit stats\n5.Create New Sales Record")
    print("6.Increment Stock\n7.Modify Price\n8.Bill\n9.Change Password")
    print("10.View All\n11.Issue a Coupon to a Customer\n12.Exchange")
    print("13.View Customers who have spent more than Rs.'n'\n14.Exit")
    while True:
        y=input("Enter Choice")
        if y=='1':
            c=input("This will delete previous records are you sure(y/n)")
            if c in "yY": create()
            else: continue
        elif y=='2': add() 
        elif y=='3':
            n=int(input("Enter Value for n"))
            view_stock(n)  
        elif y=='4': view_profit()
        elif y=='5':
            c=input("This will delete Previous sales records are you sure(y/n)")
            if c in "yY": create_p()
            else: continue
        elif y=='6': Inc_stock() 
        elif y=='7':
            x=input("Do You want to modify CP or SP(Enter cp/sp)")
            if x.lower()=="cp": mod_p(2)
            elif x.lower()=="sp": mod_p(3)
            else: print("invalid entry")
        elif y=='8': buy_bill()
        elif y=='9': change()
        elif y=='10': view()
        elif y=='11':
            x=int(input("Enter coupon amount"))
            cupon(x)
        elif y=='12':
            x=int(input('enter id'))
            y=int(input('enter quantity'))
            exchange(x,y)
        elif y=='13':view_customer()
        elif y=='14':
            print("Exiting...")
            break
        else: print("invalid choice")
else:
    print("\tMENU\n1.View All Products \n2.View Products with Brand")
    print("3.View products with Description\n4.View products in price Range")
    print("\n5.Exit")
    while True:
        y=input("Enter choice")
        if y=="1":view()
        elif y=="2":
            b=input("Enter Product Brand")
            view_b(b)
        elif y=="3":
            d=input("Enter Product Description")
            view_d(d)
        elif y=="4":
            ll=int(input("Enter Lower Limit"))
            ul=int(input("Enter Upper Limit"))
            view_p(ll,ul)
        elif y=="5":
            print("Exiting...")
            break
        else: print("Invalid Entry")
