"""
Lab 2 - Data Types, Variables, and Expressions
Course:  HCAI-3301 Programming Logic in Human-Centered AI
Student: Gemar Johnston

Program Goal: Answer the textbook questions by actually running the code instead of
just guessing.
"""

import keyword  # We will check if a word is reserved (like "class" or "for") so we are not bogged down by errors. 


def section(title):
    """Santa's Little Helper so the output is human readable when I turn this in."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ----------------------------------------------------------------------
# Question 1: string operations
# ----------------------------------------------------------------------
section("Question 1: String operations (x = 'dog', y = 'cat')")

x = "dog"
y = "cat"

# a) + on two strings is concatenation. Python will NOT add a space by default on this one,
#    so this squishes them together: "dogcat"
print("a) x + y =", x + y)

# b) Common mistake: forgetting the spaces INSIDE the quotes. I put a space
#    after "the " and around "chases" so it reads like a real sentence.
print("b) 'the ' + x + ' chases the ' + y =", "the " + x + " chases the " + y)

# c) * on a string repeats it. Needs an int on the other side
#    ("dog" * 4.0 would crash with a TypeError).
print("c) x * 4 =", x * 4)


# ----------------------------------------------------------------------
# Question 2: valid variable names
# ----------------------------------------------------------------------
section("Question 2: Valid variable names")

# Rules I'm checking: letters/digits/underscores only, can't Start with a
# digit, and can't be a reserved keyword. str.isidentifier() checks the
# first two rules for me, and keyword.iskeyword() covers the third.
names = ["_player", "168hrs", "MEDIA_54", "currencyIn$"]

for name in names:
    is_valid = name.isidentifier() and not keyword.iskeyword(name)
    print(f"{name:<12} -> {'VALID' if is_valid else 'INVALID'}")

# My reasoning for each one:
#   a) _player      VALID   -  User starting with an underscore is allowed by the rules.
#   b) 168hrs       INVALID - starts with a digit
#   c) MEDIA_54     VALID   - digits are fine as long as they aren't first
#                             (all caps is just a convention for constants,
#                             not a rule)
#   d) currencyIn$  INVALID - the $ symbol isn't allowed in Python names
#                             (it is in some other languages, which is the trap and can throw your code out of sorts.)


# ----------------------------------------------------------------------
# Question 3: picking the right data type
# ----------------------------------------------------------------------
section("Question 3: Most appropriate data types")

months_in_year = 12     # a) whole number that never has a fraction -> int
circle_area = 3.14159 * 5 ** 2   # b) pi makes it a decimal -> float
minimum_wage = 7.25     # c) dollars and cents -> float
my_name = "Gemar Johnston"       # d) text -> str

# type() prints what Python actually decided, which is a nice sanity check
print("a) months in a year  :", months_in_year, type(months_in_year))
print("b) area of a circle  :", circle_area, type(circle_area))
print("c) minimum wage      :", minimum_wage, type(minimum_wage))
print("d) your name         :", my_name, type(my_name))

# Note: minimum wage is a float in this problem because it has cents. If I were
# utilizing real money math, the decimal module is safer since floats can have
# tiny rounding errors (0.1 + 0.2 != 0.3 exactly), but float is the
# expected answer for this class.


# ----------------------------------------------------------------------
# Question 4: int vs. float
# ----------------------------------------------------------------------
section("Question 4: int vs. float")

# An int is a whole number (positive, negative, or zero) with no decimal
# point, and Python stores it exactly with no size limit.
# A float is a number with a decimal point (or written in scientific
# notation) and is stored as an approximation, so it can have tiny
# rounding errors.
print("int example  : 7      ->", type(7))
print("float example: 7.0    ->", type(7.0))

# Trick: 7 and 7.0 are equal in value, but they are different TYPES.
print("7 == 7.0 ?", 7 == 7.0)

# Trick: a float's rounding error is real and shows up in simple math.
print("0.1 + 0.2 =", 0.1 + 0.2)   # prints 0.30000000000000004, not 0.3

# Trick: dividing with / always gives a float, even if it divides evenly.
print("8 / 2 =", 8 / 2, type(8 / 2))   # 4.0, not 4


# ----------------------------------------------------------------------
# Question 5: Arithmetic Expressions
# ----------------------------------------------------------------------
section("Question 5: Expressions (x = 8, y = 2)")

x = 8
y = 2

# a) Order of operations: multiplication happens before addition,
#    so it is 8 + (2 * 3) = 14 (NOT (8 + 2) * 3).
print("a) x + y * 3     =", x + y * 3)

# b) Parentheses go first: (8 + 2) * 3 = 30
print("b) (x + y) * 3   =", (x + y) * 3)

# c) ** is exponent (power), NOT multiplication or XOR like ^ would be.
#    8 squared = 64
print("c) x ** y        =", x ** y)

# d) % is the remainder (modulo). 8 divided by 2 leaves nothing: 0
print("d) x % y         =", x % y)

# e) Dividing by a float (12.0) gives a float. 8 / 12 is a repeating decimal
print("e) x / 12.0      =", x / 12.0)

# f) // is floor division: it divides and chops off the remainder.
#    8 / 6 = 1.33..., so the answer is 1 (an int, since both sides are ints)
print("f) x // 6        =", x // 6)

# Extra trick I want to remember: // rounds DOWN toward negative infinity,
# not toward zero, so negatives can surprise you.
print("   (bonus) -8 // 6 =", -8 // 6)   # -2, not -1


# ----------------------------------------------------------------------
# Question 6: round() and int()
# ----------------------------------------------------------------------
section("Question 6: round() and int() (x = 4.66)")

x = 4.66

# a) round() goes to the NEAREST whole number: 4.66 is closer to 5
print("a) round(x) =", round(x))

# b) int() does NOT round. It just cuts off the decimal part (truncates),
#    so 4.66 becomes 4. This is the most common mix-up with this question.
print("b) int(x)   =", int(x))

# Extra trick: Python's round() uses "banker's rounding" on exact .5 ties,
# meaning it rounds to the nearest EVEN number, so it's not always up.
print("   (bonus) round(2.5) =", round(2.5), "| round(3.5) =", round(3.5))
# That prints 2 and 4. This can make your young self from elementary school scratch their head!


# ----------------------------------------------------------------------
# Question 7: rounding a float to the nearest int
# ----------------------------------------------------------------------
section("Question 7: Rounding a float to the nearest int")

# Answer: use the built-in round() function. When you give it just one
# argument it returns an int. int() would only truncate, so it is the
# wrong tool here.
price = 9.7
print("round(9.7) =", round(price), type(round(price)))

# If I want to round to a certain number of decimal places instead, I pass
# a second argument. That version stays a float.
print("round(3.14159, 2) =", round(3.14159, 2))


# ----------------------------------------------------------------------
# Question 8: incrementing a variable
# ----------------------------------------------------------------------
section("Question 8: Increment x by 1 (x = 55)")

x = 55

# Assignment statement: compute the right side first (55 + 1), then store
# the result back into x.
x = x + 1
print("x = x + 1  ->", x)   # 56

# Shorthand that does the same thing:
x += 1
print("x += 1     ->", x)   # 57 (it ran a second time, so it went up again)

# Common trap if you're used to C, Java, or JavaScript: Python has no x++
# operator. Writing x++ gives a SyntaxError. I had this trap trip me up for a 
# a good amount of time due to my JavaScript past!
