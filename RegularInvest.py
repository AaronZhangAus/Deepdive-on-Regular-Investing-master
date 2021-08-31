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
        print("Weekly Stock Price:")
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

        # find the daily close price
        weekly_price = data["Close"].tolist()

        # only pick the 1st self.weeks price, e.g. first 52nd weeks
        self.coin_price = weekly_price[0:self.weeks]

        # if stock price is less than self.weeks old, re-set self.weeks
        # to be earliest weeks available
        if len(self.coin_price) < self.weeks:
            self.weeks = len(self.coin_price)

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
            print("~~~~~~i am w:"+str(w))
            daily_earned_coin = self.invest_amount / self.coin_price[w]

            self.owned_coins.append(
                round(self.owned_coins[w - 1] + daily_earned_coin, 4))
            self.assets.append(
                round(self.owned_coins[w - 1] + daily_earned_coin, 4)
                * self.coin_price[w])

        print("Number of Shares Owned:")
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

        # set filename to be assets value and save in figures folder
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
        plt.subplot(3, 1, 1)
        plt.title(title)
        plt.plot(range(0, self.weeks), self.coin_price)

        # 2nd plot to show regular investment
        plt.subplot(3, 1, 2)
        plt.title("Actual Investment vs. Assets")
        plt.plot(range(0, self.weeks), self.investment)
        plt.plot(range(0, self.weeks), self.assets)

        # 3rd plot to show number of shares owned
        plt.subplot(3, 1, 3)
        plt.title("Number of Shares Owned")
        plt.plot(range(0, self.weeks), self.owned_coins)

        # save the figures as stock_name.png in stocks folder
        plt.savefig('stocks/' + self.stock + ".png")
        plt.show()

        # clear the figure
        plt.cla()
