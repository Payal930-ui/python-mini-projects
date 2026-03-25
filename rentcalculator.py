persons=int(input("total no. of persons living: "))
rent=int(input("Enter the amount of rent of Flat/Room: "))
food=int(input("Enter the amount spend on food: "))
electricity_spend=int(input("Enter the amount of units used: "))
charge_per_unit=int(input("Enter the charge per unit: "))
bill=electricity_spend*charge_per_unit
output=(food+rent+bill)//persons
print("Each persons have to pay",output,smile)
