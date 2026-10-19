

new_releases = int(input("Welcome to Five Star Retro Video employee terminal! Please enter the number of new releases: "))
oldies_videos = int(input("Please enter the number of oldies_VHS: "))
nights = int(input("Please enter the number of nights you wish to rent for: "))
total_cost = (new_releases * 3.00 + oldies_videos * 2.00) * nights #Calculates cost of both new releases and oldies.

print(f"Total rental cost: ${total_cost:.2f}") #The '2f' formats the output amount to two decimal places.
print(f"Please tell the customer Thank you for renting at Five Star Retro Video!")