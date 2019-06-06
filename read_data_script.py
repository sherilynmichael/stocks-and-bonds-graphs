"""
Description:    This program reads stocks and bonds data from two csv files

Author: Sheri Michael

Date Created: 4/30/19 (restructured HW4 code)
Last Revision: 6/5/19
"""

# Import functions from module, stock_functions
from classes_stock import *

# instantiate investor Bob Smith's information
investorBob = Investor(1, 'bob smith', 'denver, CO', '720-555-5555')
#print(investorBob.get_investor_info())

stockOwners =['Bob Smith']

#Call function read_data
data = read_data()
#print(data)

stockSymbol = data[0]
#print(stockSymbol)
numShares = data[1]
purchasePrice = data[2]
currentValue = data[3]
purchaseDate = data[4]
coupon = data[5]
output = data[6]
# Call function, loss-gain(), (from module, classes_stock_functions) to calculate net loss/gain of each stock
losses_gains = Bond(currentValue, purchasePrice, numShares, purchaseDate, stockSymbol, coupon, output).loss_gain()
#print("losses_gains", losses_gains)

# Call function, percentage_diff(curentValue, purchasePrice)
year_diff = Bond(currentValue, purchasePrice, numShares, purchaseDate, stockSymbol,coupon, output).year_diff()
percent_diff = Bond(currentValue, purchasePrice, numShares, purchaseDate, stockSymbol,coupon, output).percentage_diff()
#print("yearDiff", year_diff, "percentDiff", percent_diff)

# Call function, yearly_earnings(), to calculate yearly earnings/loss
yearly_earnings = Bond(currentValue, purchasePrice, numShares, purchaseDate, stockSymbol,coupon, output).yearly_earnings()
#print("yearly_earnings", yearly_earnings)

# Call function, stock_earnings_dix, to create dicttionary of investor data
stock_earnings = Bond(currentValue, purchasePrice, numShares, purchaseDate, stockSymbol,coupon, output).stock_earnings_dix(stockSymbol, numShares, losses_gains, yearly_earnings, coupon, output)
#print("stock_earnings", stock_earnings)
