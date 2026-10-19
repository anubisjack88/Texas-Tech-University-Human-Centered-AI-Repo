# Video Rental Calculator - Summer Promotion Upgrade

# Collect user input for rental counts and duration
new_releases = int(input("Welcome to Five Star Retro Video employee terminal! Please enter the number of new releases: "))
oldies_videos = int(input("Please enter the number of oldies_VHS: "))
nights = int(input("Please enter the number of nights you wish to rent for: "))

# Ask for the current semester to evaluate eligibility for the promotion
semester = input("Please enter the current semester (e.g., Summer, Fall, Spring): ").strip()

# Base calculations
total_movies = new_releases + oldies_videos
original_cost = (new_releases * 3.00 + oldies_videos * 2.00) * nights

discount = 0.0

# Summer Promotion Logic:
# Applies 20% discount if it's "Summer" AND (10+ total movies OR total cost is $50 or more)
if semester.lower() == "summer":
    if total_movies >= 10 or original_cost >= 50.0:
        discount = original_cost * 0.20

final_cost = original_cost - discount

# Output formatting
print("\n" + "=" * 45)
print("            FIVE STAR RETRO VIDEO RECEIPT            ")
print("=" * 45)
print(f"Total Movies Rented: {total_movies}")
print(f"Subtotal:           ${original_cost:.2f}")

if discount > 0:
    print(f"Summer Promotion:   -${discount:.2f} (20% Discount Applied)")
else:
    print("Summer Promotion:   $0.00 (No discount applied)")

print(f"Total Rental Cost:  ${final_cost:.2f}")
print("=" * 45)
print("Please tell the customer Thank you for renting at Five Star Retro Video!")
