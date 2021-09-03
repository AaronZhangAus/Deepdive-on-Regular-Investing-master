from RegularInvest import RegularInvest
import pandas_datareader.data as web
import pandas as pd
from yahoo_fin import stock_info as si
import csv


def read_all_ETFs():
    # read ETF tickers from ETFs.csv
    with open('ETFs_industrials.csv', newline='') as f:
        reader = [i[0] for i in csv.reader(f)]
        full_list = list(reader)
        print(full_list)
    return full_list


def read_all_stocks_price():
    # read in all stock price in nasdaq
    df1 = pd.DataFrame(si.tickers_nasdaq())

    # convert dataframe to a list then to a set
    s_list = df1[0].values.tolist()
    print(s_list)
    return s_list


stock_list = []
stock_id = 0

# list of all cryto currency tickers
# simulation plot to save in cryto_stocks folder
# stock records to save in cryto_records folder
crypto_list = [
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

# stock_list = read_all_stocks_price() # test all stocks in Nasdaq
#stock_list = read_all_ETFs()  # test all ETFs in Nasdaq
# stock_list = crypto_list #test all crytos
stock_list = ['FNILX'] #test individual stock


for stock_ticker in stock_list:
    print(stock_list.index(stock_ticker))
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
