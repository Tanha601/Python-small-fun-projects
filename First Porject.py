Rent = int(input("Enter your hostel/flat rent = "))
Food_price=int(input("Enter your food = "))
Total_electricity_spend=int(input("Enter your electricity spend = "))
Charge_per_unit=int(input("Enter the unit = "))
Total_bill=(Total_electricity_spend*Charge_per_unit)
Persons=int(input("Enter the number of persons living = "))
Output =(Rent+Food_price+Total_electricity_spend+Total_bill)//Persons
print("Each member will pay =",Output)