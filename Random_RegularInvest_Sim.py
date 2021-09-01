from RegularInvest import RegularInvest
import pandas_datareader.data as web

# random generate 50 stock prices and emulate the regular investment strategy
for i in range(1):

    # Regular Investing $100 for 52 weeks, beta:fluctuation rate
    exp1 = RegularInvest(weeks=52, stock="", invest_amount=100, beta=3000)

    # Random generate stock price
    # exp1.random_populate_coin_price()
    exp1.populate_coin_price_with_sin()
    # exp1.populate_stock_price()

    # Populate the actual investment amount each week
    exp1.populate_investment()

    # Calcuate number of shares purchased and weekly assets
    exp1.populate_owned_coins()

    # Plot the result and save to figures folder as "asset_amount".jpg
    exp1.plot_result()
