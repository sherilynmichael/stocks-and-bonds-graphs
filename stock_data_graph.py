"""
Description: This program outputs bar graph of yearly earnings/losses to file, yearly_earnings.png

Author: Sheri Michael

Created: 6/5/2019
"""


from read_data_script import *
import matplotlib.pyplot as plt


#Create bar chart showing yearly_earnings
df = pd.DataFrame(data=stock_earnings)
#print(df)
df = df[[1,4]]
df.columns = ['symbol', 'yearly_earnings']
df=df.set_index('symbol')
#print(df)
#print(df.dtypes)
df['yearly_earnings']=df['yearly_earnings'].astype(float)
#print(df.dtypes)
df.plot.bar(y='yearly_earnings', legend=False, title='Yearly Earnings/Losses in millions($)', rot=0)
#plt.show()
plt.savefig('/Users/sheri/Desktop/Python_Scripts/ict4370_python/W10/yearly_earnings.png')
