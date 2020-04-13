
    # The function should look at each key (pennies, nickels, dimes and quarters) and 
    # perform the appropriate math on the integer value to determine how much money you have 
    # in dollars. Store that value in a variable named `dollarAmount` and print it.
#   def calc_dollars(**coins):
#     amounts = []
#     for (coin, amount) in coins.items():
#         if coin == "pennies":
#            amounts.append(amount/100)
#         elif coin == "nickels":
#             amounts.append(amount/20)
#         elif coin == "dimes":
#             amounts.append(amount/10)
#         elif coin == "quarters":
#             amounts. append(amount/4)
#     print(sum(amounts))
        
    

# calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)


dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}
def cash_to_coins(total):
    piggyBank["quarters"] = int(total*4)
    piggyBank["dimes"] = int((total - (piggyBank["quarters"]*.25))*10)
    piggyBank["nickels"] = int((total-(piggyBank["quarters"]*.25)-(piggyBank["dimes"]*.1))*20)
    piggyBank["pennies"] = round((total-(piggyBank["quarters"]*.25)-(piggyBank["dimes"]*.1)-(piggyBank["nickels"]*.05))*100)
    

cash_to_coins(dollarAmount)
print(piggyBank)