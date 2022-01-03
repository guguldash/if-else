unit=int(input('enter units number'))
if unit <=50:
	bill=(unit*0.50+20/100)
	bill=(30*0.50+20/100)
	print(bill)
elif unit<=100:
	bill=(unit*0.75+20/100)
	bill=(60*0.75+20/100)
	print(bill)
elif unit<=200:
	bill=(unit*1.20+20/100)
	bill=(150*1.20+20/100)
	print(bill)
elif unit>=250:
	bill=(unit*1.50+20/100)
	bill=(200*1.50+20/100)
	print(bill)
 #unit bill   