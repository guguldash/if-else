from typing import _SpecialForm


chr=input("enter your chr")
if chr>"A" and chr>"Z":
    print("albhabet")
elif chr>="0" and  chr<="9" :
    print("digit")
elif  chr>="@"  and chr<="#":
     print("special")
else:
    print("nothing")

_#SpecialForm
