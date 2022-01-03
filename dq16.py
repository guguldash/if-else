cp=float(input("Enter the Cost Price : "));
sp=float(input("Enter the Selling Price : "));
if cp==sp:
    print("No Profit No Loss")
else:
    if sp>cp:
        print("Profit of ",sp-cp)
    else:
        print("Loss of ",cp-sp)