"""Nested Conditionals."""

# @TODO: Create variables with the initial ad price and company type
ad_price = 10
company_type = "Startup"

# @TODO: Convert the following decision logic into valid Python code.

if ad_price < 20: 
    if company_type == "Startup":
        print("expected revenue $500")
    elif company_type == "Existing":
        print("expected revenue $100")
    else:
        print("Company type is not specified")

    

# if the ad price is affordable (less than 20):
#     if the company is a startup:
#         print that the expected profit is 500
#     elif the company is existing:
#         print that the expected profit is 100
#     else:
#         print that the company type is not specified
# else:
#     print that the ad price is too expensive
