unit=int(input("enter your unit"))
if unit<=100:
    print("no charge")
if  unit>100 and unit<200:
    print(unit-100*5)
if unit<200:
    print((100*0)+(100*5) +(unit-200 )*10)
else:
    print("enter your unit")    
