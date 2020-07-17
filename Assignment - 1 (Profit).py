# Task - 1 :
# You work for a manufacturer as a programmer and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary (sales) containing the cost price per unit (in dollars), sell price per unit (in dollars), and the beginning inventory. Write a program to return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold. The name and the keys of the dictionary are constant, so use them as they are.

inventory = float(input())
sales = {
    'cost_price' : 9,
    'sell_price' : 12.5,
    'inventory' : inventory
}
total_profit = (sales['sell_price'] - sales['cost_price']) * sales['inventory']
print(round(total_profit))



# Task - 2 :
# Your boss wants you to prepare the payrolls of the workers in your department. You have to convert the amount of dollars into payroll format. In order to help move things along, you have volunteered to write a code that will take a float and return the amount formatting in dollars and cents. 

amount = float(input())
print('$'+ str(round(amount, 2)))