sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
per=(sub1+sub2+sub3+sub4+sub5/500*100)
if per>=90:
    print("grade A") 
if per>=80:
    print("grade B")
if per>=70:
    print("grade C") 
if per>=60:
    print("grade D") 
if per>40:
    print("grade E")          

else:
    print("grade F")

