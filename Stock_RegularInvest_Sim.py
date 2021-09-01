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
stock_id = 3501

# read in all stock tickers
stock_list = read_all_stocks_price()
# stock_list = ['ACGLP']

# list of all cryto currency tickers
# simulation plot to save in cryto_stocks folder
# stock records to save in cryto_records folder
cryto_list = [
    'BTC-USD',
    'ETH-USD',
    'ADA-USD',
    'BNB-USD',
    'USDT-USD',
    'XRP-USD',
    'HEX-USD',
    'DOGE-USD',
    'SOL1-USD',
    'USDC-USD',
    'DOT1-USD',
    'UNI3-USD',
    'LUNA1-USD',
    'BCH-USD',
    'LINK-USD',
    'LTC-USD',
    'ICP1-USD',
    'MATIC-USD',
    'ETC-USD',
    'XLM-USD',
    'VET-USD',
    'AVAX-USD',
    'FIL-USD',
    'THETA-USD',
    'TRX-USD'
]

for stock_ticker in stock_list[3594:4000]:
    print(stock_id)
    print(stock_ticker)
    exp1 = RegularInvest(weeks=52, stock=stock_ticker, invest_amount=100, beta=3000)
    # exp1 = RegularInvest(weeks=52, stock="fb", invest_amount=100, beta=3000)

    # assume the stock is valid
    valid_stock = True

    valid_stock = exp1.populate_stock_price()
    # valid_stock is false when records are less than 20

    # for valid stock
    if valid_stock:
        # calculate the investment list
        exp1.populate_investment()

        # calculate number of shares purchased over time as well as assets
        exp1.populate_owned_coins()

        # plot the stock price, investment vs assets and number of shares
        exp1.plot_stock_and_result()

        # store the results to a file as stock_name.txt in records folder
        exp1.create_ri_records()

    # clear all list
    exp1.reset()
    stock_id = stock_id + 1
