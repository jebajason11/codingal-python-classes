units =int(input("enter the units consumed"))

if units <50:
    amount= units * 2.60 + 25
    print (amount)
elif units <=100:
    amount= (units* 2.60+25) + (units-50)*3.25+35
    print(amount)
elif units  <=200:
    amount=(130+162.50)+  ((units-100)*5.26+45)
    print(amount)

else:
    amount = 130+162.50+526+((units-200)*8.45)+75
    print(amount)