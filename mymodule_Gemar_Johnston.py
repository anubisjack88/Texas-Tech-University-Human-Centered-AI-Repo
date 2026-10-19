#This Module contains the function pay_calculator that will be called by program2
#During testing, I found that I did not indent line 5 and this stopped my code from running.
#I made sure to return the total_pay so that I could break out of my code and end the function.

def pay_calculator(hourly_wage, regular_hours, overtime_hours):
    total_pay = (regular_hours * hourly_wage) + (overtime_hours * 1.5 * hourly_wage)
    return total_pay
