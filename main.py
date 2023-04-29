import datetime
import generate_bill
i=1
sno=1
while(i):
    print("Enter your choice:")
    print("1: Make entry")
    print("2: View current bill")
    print("3: Generate bill")
    print("4: Exit")
    choice=int(input())
    if choice==1:
        with open('current_bill.txt',"r") as f:
            sno = sum(1 for _ in f)
        print("Enter Consignee, Dest, Weight and Amount:")
        inp=input().split()
        with open("current_bill.txt","a+") as f:
            f.write(str(sno+1)+" ")
            f.write(datetime.date.today().strftime("%d/%m/%Y")+" ")
            for j in inp:
                f.write(j+" ")
            f.write("\n")
        
    elif choice==2:
        with open("current_bill.txt","r") as f:
            for j in f:
                print(*j.split())

    elif choice==3:
        with open("bill_no.txt","r") as f:
            bno=f.read()
        generate_bill.generatepdf(bno)
        open("current_bill.txt","w")
        with open("bill_no.txt","w") as f:
            f.write(str(int(bno)+1))


    elif choice==4:
        i=0