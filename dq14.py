a = int(input('Please Enter the First Angle of a Triangle: '))
b = int(input('Please Enter the Second Angle of a Triangle: '))
c = int(input('Please Enter the Third Angle of a Triangle: '))
if a + b > c or b + c > a:
    print("valid")
else:
    print ("not valid")        