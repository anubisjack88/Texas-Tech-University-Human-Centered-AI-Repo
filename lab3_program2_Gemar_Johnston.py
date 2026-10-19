

from mymodule_Gemar_Johnston import pay_calculator #This call is importing functionality from the module my_module

print("Welcome to Employee Weekly Pay Calculator! Please enter your wage, regular hours, and overtime.")

hourly_wage = float(input("Enter hourly wage: ")) #By utilizing flot, the string or text can be converted into a decimal number.
regular_hours = float(input("Enter total regular hours: "))
overtime_hours = float(input("Enter total overtime hours: "))

total_pay = pay_calculator(hourly_wage, regular_hours, overtime_hours) #This line of code calculates the total pay by combining relative data.

print(f"Your total weekly pay is: ${total_pay:.2f} "f"Thank you for using the Employee Weekly Pay Calculator!")
