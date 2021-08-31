from RegularInvest import RegularInvest
import pandas_datareader.data as web
import pandas as pd
from yahoo_fin import stock_info as si


def read_all_stocks_price():
    # read in all stock price in nasdaq
    df1 = pd.DataFrame(si.tickers_nasdaq())

    # convert dataframe to a list then to a set
    s_list = df1[0].values.tolist()
    print(s_list)
    return s_list


stock_list = []

# read in all stock tickers
stock_list = read_all_stocks_price()
# stock_list = ['ACGLP']

for stock_ticker in stock_list[1254:2000]:
    print(stock_ticker)
    exp1 = RegularInvest(weeks=52, stock=stock_ticker, invest_amount=100, beta=3000)
    # exp1 = RegularInvest(weeks=52, stock="fb", invest_amount=100, beta=3000)
    # exp1.populate_coin_price()
    # exp1.populate_coin_price_with_sin()

    # assume the stock is valid
    valid_stock = True

    valid_stock = exp1.populate_stock_price()
    if valid_stock:
        exp1.populate_investment()
        exp1.populate_owned_coins()
        exp1.plot_stock_and_result()
        exp1.create_ri_records()

    exp1.reset()

# sorted_stock_list = RegularInvest.sort_growth_rate()
# print("TOP 30 HIGHEST GAIN STOCKS FOR REGULAR INVESTING:")
# for i in sorted_stock_list[:30]:
#     print(i['ticker'])
#     print(i['growth_rate'])
