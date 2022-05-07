import pymongo
from pymongo import MongoClient
import pprint as pprint
''' database '''
myclient = pymongo.MongoClient()

mydb = myclient['astore']

''' collection'''

mycol = mydb["medstore"]
ans=True
while ans:

    print ("\n\t1. Status \n\t2. Import\n\t3. Purchase\n\t4. Exit/Quit ")
    ans=int(input("What would you like to do?\n"))
    
    #STATUS
    flag=0 
    tlag=0   
    if ans==1:
      print("\n\tNAME\tBRAND\tQTY.\tPRICE")
      for s in mycol.find():
        print("\t",s['name'],"\t",s['Brand'],"\t",s['qty'],"\t",s['price']) 
    elif ans==2:
        mname=input("\nEnter the name of Medicine\n") #import
        mbrand=input("\nEnter the Brand Name\n")
        mqty=int(input("\nEnter the Quantity\n"))
       
        for s in mycol.find():
                if (s['name']==mname ):
                    totalqty= s['qty']+mqty
                    myquery = { "name": mname }
                    newvalues = { "$set": { "qty": totalqty } }
                    mycol.update_one(myquery, newvalues)
                    flag=1
                    break
        if(flag==0):
            mprice=input(" \nEnter the price\n")
            mydict = { "name": mname, "Brand": mbrand, "qty": mqty, "price": mprice }
            x = mycol.insert_one(mydict)
              
    elif ans==3:
        mname1=input("\nEnter the name of Medicine\n") #billing
        mbrand1=input("\nEnter the Brand Name\n")
        mqty1=int(input("\nEnter the Quantity\n "))
        for a in mycol.find():
            if(a['name']==mname1):
                if(a['qty']>=mqty1):
                    totalprice= int(a['price']) * mqty1
                    print("Total price to pay-" ,totalprice)
                    totalqty1= a['qty']-mqty1
                    myquery = { "name": mname1 }
                    newvalues = { "$set": { "qty": totalqty1 } }
                    mycol.update_one(myquery, newvalues)
                else:
                    print("Sorry insufficent stock\n");
                    print("Current avliable stock\n")
                    print("\n\tNAME\tBRAND\tQTY.\tPRICE")
                    print("\t",a['name'],"\t",a['Brand'],"\t",a['qty'],"\t",a['price'])
                tlag=1    
        if(tlag==0):
                print("\n**** Sorry not avliable ****\n")           
    elif ans==4:
        exit()
    
    

    
