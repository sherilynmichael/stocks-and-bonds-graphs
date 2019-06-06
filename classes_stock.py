"""
Description:    This program reads data from cvs files and creates the following classes:
                    1. Investor
                    2. Stock
                    3. Bond

Author: Sheri Michael

Date Created: 4/30/19
Last Revision: 5/15/19
"""

from datetime import datetime
import pandas as pd
import sqlite3


def read_data():
    #Read in Stock Files & create lists
    dfStocks = pd.read_csv('/Users/sheri/Downloads/Lesson6_Data_Stocks.csv')
    #print(dfStocks)
    stockSymbolStocks = dfStocks['SYMBOL'].values.tolist()
    #print(stockSymbolStocks)
    numSharesStocks = dfStocks['NO_SHARES'].values.tolist()
    #print(numSharesStocks)
    purchasePriceStocks = dfStocks['PURCHASE_PRICE'].values.tolist()
    #print(purchasePriceStocks)
    currentValueStocks = dfStocks['CURRENT_VALUE'].values.tolist()
    #print(currentValueStocks)
    purchaseDateStocks = dfStocks['PURCHASE_DATE'].values.tolist()
    #print(purchaseDateStocks)
    #Create 2 empty lists for Bond coupon and yield(output) = length of Stock files
    couponStocks = ['n/a'] * len(stockSymbolStocks)
    outputStocks = ['n/a'] * len(stockSymbolStocks)

    #Read in Bond Files & create lists
    dfBonds = pd.read_csv('/Users/sheri/Downloads/Lesson6_Data_Bonds.csv')
    #print(dfBonds)
    stockSymbolBonds = dfBonds['SYMBOL'].values.tolist()
    #print(stockSymbolBonds)
    numSharesBonds = dfBonds['NO_SHARES'].values.tolist()
    #print(numSharesBonds)
    purchasePriceBonds = dfBonds['PURCHASE_PRICE'].values.tolist()
    #print(purchasePriceBonds)
    currentValueBonds = dfBonds['CURRENT_VALUE'].values.tolist()
    #print(currentValueBonds)
    purchaseDateBonds = dfBonds['PURCHASE_DATE'].values.tolist()
    #print(purchaseDateBonds)
    couponBonds = dfBonds['Coupon'].values.tolist()
    #print(couponBonds)
    outputBonds = dfBonds['Yield'].values.tolist()
    #print(outputBonds)


    #Merge Stocks & Bonds lists
    stockSymbol = stockSymbolStocks + stockSymbolBonds
    numShares = numSharesStocks + numSharesBonds
    purchasePrice = purchasePriceStocks + purchasePriceBonds
    currentValue = currentValueStocks + currentValueBonds
    purchaseDate = purchaseDateStocks + purchaseDateBonds
    coupon = couponStocks + couponBonds
    output = outputStocks + outputBonds

    return stockSymbol, numShares, purchasePrice, currentValue, purchaseDate, coupon, output

class Investor():
   """identifies investors"""

   def __init__(self, investorID, name, address, phoneNumber):
       """Initialize investorId, name, address, and phonNumber attributes"""
       self.investorID = investorID
       self.name = name
       self.address = address
       self.phoneNumber = phoneNumber

   def get_investor_info(self):
       print("Investor's Info:")
       print("Investor ID: " + self.investorID)
       print("Name: " + self.name.title())
       print("Address: " + self.address.title())
       print("Phone Number: " + self.phoneNumber)

class Stock():
    """identifies stocks and bonds"""

    def __init__(self, currentValue, purchasePrice, numShares, purchaseDate, stockSymbol, *purchasedId):
        """Initialize currentValue, purchasePrice, numShares attributes"""
        self.currentValue = currentValue
        self.purchasePrice = purchasePrice
        self.numShares = numShares
        self.purchaseDate = purchaseDate
        self.stockSymbol = stockSymbol

class Bond(Stock):
    def __init__(self,stockSymbol,currentValue, purchasePrice, numShares, purchaseDate, coupon, output, *purchasedId):
        #Initialize attributes of parent class, Stock
        super().__init__(stockSymbol, currentValue, purchasePrice, numShares, purchaseDate, *purchasedId)
        #Check Stock class initialized
        #print("in Bond", currentValue)
        #Initialize bond attributes
        self.coupon = coupon
        self.output = output

    # Calculate the loss/gain of an inverstor's stocks (loss_gain (params))
    def loss_gain(self):
        net = []

        for i in range(0, len(self.purchasePrice)):
            total = (self.currentValue[i]-self.purchasePrice[i]) * self.numShares[i]
            total = format(total, ".2f")
            net.append(total)
        return net

    # The difference in years between stock currentDate and purhaseDate (year_diff(param))
    def year_diff(self):
        #currentDate = date.today()
        currentDate = datetime.today()
        #global yearDiff
        yearDiff = []

        for i in self.purchaseDate:
            datetimeDate = datetime.strptime(i, '%m/%d/%Y')
            #print (datetimeDate)
            diffInDays = (currentDate - datetimeDate).days
            diffInYears = diffInDays/365
            #print (diffInYears)
            yearDiff.append(diffInYears)
        #print(yearDiff)
        return yearDiff

    # Calculate the percentage yield/loss for each of the stocks,
    def percentage_diff(self):
        percentDiff = []
        for i in range(0, len(self.currentValue)):
            percentDifference = (self.currentValue[i] - self.purchasePrice[i])/self.purchasePrice[i]*100
            percentDifference = format(percentDifference, ".2f")
            percentDiff.append(percentDifference)
        #print(percentDiff)
        return(percentDiff)

    # Calculate the yearly earnings/loss rate (yearly_earnings(params)),
    def yearly_earnings(self):
        yearDiff = self.year_diff()
        yearly_earnings_losses = []
        #print(len(self.currentValue),len(self.purchasePrice), len(yearDiff))

        for i in range(0, len(self.currentValue)):
            #earnings = (((currentValue[i]-purchasePrice[i])/purchasePrice[i])/(yearDiff[i]))*100
            earnings = ((self.currentValue[i]-self.purchasePrice[i])/self.purchasePrice[i])/(yearDiff[i])*100
            earnings = format(earnings, ".2f")
            yearly_earnings_losses.append(earnings)
        return yearly_earnings_losses

    def stock_earnings_dix(self, stockSymbol, numShares, losses_gains, yearly_earnings_losses, coupon, output):
        # Create a tuple of earnings/losses by user for each stock
        sbId = []
        for i in range(len(stockSymbol)):
            x = i + 1
            sbId.append(x)
        stockEarnings = list(zip(sbId, stockSymbol, numShares, losses_gains, yearly_earnings_losses, coupon, output))
        return stockEarnings
