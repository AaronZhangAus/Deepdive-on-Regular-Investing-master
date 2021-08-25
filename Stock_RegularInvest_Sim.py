from RegularInvest import RegularInvest
import pandas_datareader.data as web

for i in range(1):
    exp1 = RegularInvest(weeks=52, stock="fb", invest_amount=100, beta=3000)
    #exp1.populate_coin_price()
    #exp1.populate_coin_price_with_sin()
    exp1.populate_stock_price()
    exp1.populate_investment()
    exp1.populate_owned_coins()
    exp1.plot_stock_and_result()
