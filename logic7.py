user=int(input("enter time when he start"))
user1=int(input("enter the stop time"))
i=0
while i<user:
    if i<user1:
        if (user1-user)<3:
            print("not complete")
            break
        else:
            print("completed")
            break
        i=i+1