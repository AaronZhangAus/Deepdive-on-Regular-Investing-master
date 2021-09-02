from RegularInvest import RegularInvest
import pandas_datareader.data as web

# random generate 50 stock prices and emulate the regular investment strategy
for i in range(1,60):
    # Regular Investing $100 for 52 weeks, beta:fluctuation rate
    exp1 = RegularInvest(weeks=26, stock="", invest_amount=100, beta=3000)

    # Random generate stock price
    # exp1.random_populate_coin_price()
    cycles = i  # default calculating 2 cycles
    exp1.populate_coin_price_with_sin(cycles)
    # exp1.populate_stock_price()

    # Populate the actual investment amount each week
    exp1.populate_investment()

    # Calcuate number of shares purchased and weekly assets
    exp1.populate_owned_coins()

    # Plot the result and save to figures folder as "asset_amount".jpg
    exp1.plot_result(cycles)
