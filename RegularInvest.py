import random
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas_datareader.data as web
import datetime


class RegularInvest:

    def __init__(self, weeks, stock, invest_amount, beta):
        # initial coin price on day 1 is 30000
        self.coin_price = [30000]
        self.weeks = weeks
        self.stock = stock
        self.invest_amount = invest_amount
        self.beta = beta
        self.investment = []
        self.owned_coins = []
        self.assets = []

    def random_populate_coin_price(self):

        for w in range(1, self.weeks):
            # random up or down
            up_down = np.random.choice([1, -1], p=[0.5, 0.5])
            # random fluctuate each day
            daily = self.coin_price[w - 1] \
                    + up_down * random.randrange(0, self.beta)
            self.coin_price.append(daily)
        print("Weekly Coin Price:")
        print(self.coin_price)

        pass

    def populate_coin_price_with_sin(self):

        x_values = np.arange(0, 3.14, 3.14 / self.weeks)
        templist = np.sin(x_values)
        self.coin_price = [30000 + i * 15000 for i in templist]
        # plt.plot(x_values,self.coin_price)
        # plt.show()

    def populate_stock_price(self):
        # retrieve weekly stock price for the last n weeks
        print("stock to extract:" + str(self.stock))
        print("number of weeks to extract:" + str(self.weeks))

        tod = datetime.datetime.now()
        delta = datetime.timedelta(days=self.weeks * 7)
        start_date = tod - delta
        start_date_str = start_date.strftime("%m/%d/%Y")
        print("Extract weekly price from:" + start_date_str)

        # extract weekly stock price from start_date_str
        data = web.get_data_yahoo(self.stock, start_date_str, interval='w')
        weekly_price = data["Close"].tolist()
        # only read the 1st self.weeks price
        self.coin_price = weekly_price[0:self.weeks]
        print("Weekly Price for " + self.stock)
        print(self.coin_price)
        pass

    def populate_investment(self):

        self.investment = [0]
        for w in range(1, self.weeks):
            self.investment.append(self.investment[w - 1] + self.invest_amount)

        print("Total Investment:")
        print(self.investment)

    def populate_owned_coins(self):

        self.owned_coins = [0]
        self.assets = [0]
        for w in range(1, self.weeks):
            daily_earned_coin = self.invest_amount / self.coin_price[w]

            self.owned_coins.append(
                round(self.owned_coins[w - 1] + daily_earned_coin, 4))
            self.assets.append(
                round(self.owned_coins[w - 1] + daily_earned_coin, 4)
                * self.coin_price[w])

        print("Total Owned Coins:")
        print(self.owned_coins)

        print("Total Assets:")
        print(self.assets)

    def plot_result(self):
        plt.plot(range(0, self.weeks), self.coin_price)
        plt.plot(range(0, self.weeks), self.investment)
        plt.plot(range(0, self.weeks), self.assets)

        title = self.stock + " Total Assets:" + str(round(self.assets[-1], 2)) + \
                "  Total Investment:" + str(round(self.investment[-1], 2)) + \
                "  Gain:" + str(round((self.assets[-1] - self.investment[-1]) / self.investment[-1] * 100, 2)) + "%"
        plt.title(title)
        my_file = str(str(round(self.assets[-1], 2)))
        plt.savefig('figures/' + my_file + ".png")
        # plt.show()
        # clear the figure
        plt.cla()

    def plot_stock_and_result(self):

        title = self.stock + " Total Assets:" + str(round(self.assets[-1], 2)) + \
                "  Total Investment:" + str(round(self.investment[-1], 2)) + \
                "  Gain:" + str(round((self.assets[-1] - self.investment[-1]) / self.investment[-1] * 100, 2)) + "%"

        # 1st plot to show stock price
        plt.subplot(2, 1, 1)
        plt.title(title)
        plt.plot(range(0, self.weeks), self.coin_price)

        # 2nd plot to show regular investment
        plt.subplot(2, 1, 2)
        plt.plot(range(0, self.weeks), self.investment)
        plt.plot(range(0, self.weeks), self.assets)

        # save the figures as stock_name.png in stocks folder
        plt.savefig('stocks/' + self.stock + ".png")
        plt.show()

        # clear the figure
        plt.cla()
