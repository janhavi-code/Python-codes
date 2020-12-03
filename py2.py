
# Difference between division and modulus
# # take input from user

# number_one=18
# number_two=9

# # formula

# result1=number_one/number_two
# result2=number_one%number_two

# # result
# print("Result is:",result1)
# print("Result is:",result2)

# ----------------------------------------------------------------------------------------------------------------------------------------

# if-else
# Check whether the number is even or odd
# take value

# number=int(input("Enter the number"))

# # condition
# if number%2==0 :
#     print("Entered number is even!")
# else:
#     print("Oops the entered number is odd")

# --------------------------------------------------------------------------------------------------------------------------------------

# Check if the entered year is a leap year or not

# year=int(input("Enter the year:"))

# # condition
# if year%4==0 :
#     print("The entered year ia a leap year")
# else:
#     print("sorry its not the leap year")

# --------------------------------------------------------------------------------------------------------------------------------------

# check whether who is the youngest amongst the three children

# boy1_age=10
# boy2_age=2
# boy3_age=5

# if boy1_age<=boy2_age and boy1_age<=boy3_age :
#     print("Boy1 is youngest")
# elif boy2_age<=boy1_age and boy2_age<=boy3_age :
#     print("Boy2 is younger")
# else :
#     print("Boy3 is the youngest")

# ------------------------------------------------------------------------------------------------------------------------------------------

# Pythagoras theorem

side_1=int(input("Enter side 1:"))
side_2=int(input("Enter side 2:"))
side_3=int(input("Enter side 3:"))

if side_1>=side_2 and side_1>=side_3 :
    a,b,c = side_2,side_3,side_1
    # a=side_2
    # b=side_3
    # c=side_1
    print(f'side 1 is {side_1}')                      #f is formatting
elif side_2>=side_1 and side_2>=side_3:
    a,b,c = side_1,side_3,side_2
    print("Side 2 is the largest")
else:
    a,b,c = side_1,side_2,side_3
    print("Side 3 is the largest")

# R.H.S

rhs_value=c*c


# L.H.S

lhs_value=(a*a) + (b*b)

# logic
if rhs_value==lhs_value :
    print("Pythagoras Theorem is proved")
else :
    print("Try again")
# # --------------------------------------------------------------------------------------------------------------------------------------

# # Simple Interest

# principal=int(input("Enter the principal amount:"))
# no_or_period=int(input("Enter no. of period:"))
# rate_of_interest=float(input("Enter rate of interest:"))

# simple_interest=(principal * no_of_period * rate_of_interest)/ 100

# print("The simple interest is:",simple_interest)

# --------------------------------------------------------------------------------------------------------------------------------------

# Profit and Profit%

# cost_price=20
# selling_price=80

# # profit formula
# profit=(selling_price-cost_price)
# print(profit)

# # profit percentage formula
# profit_percentage= (profit / cost_price) * 100
# print(profit_percentage)

# --------------------------------------------------------------------------------------------------------------------------------------

