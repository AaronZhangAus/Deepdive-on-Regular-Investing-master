import random
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas_datareader.data as web
import datetime


class RegularInvest:
    # class-level list to store regular investing records
    ri_records = []

    def __init__(self, weeks, stock, invest_amount, beta):
        # initial coin price on day 1 is 30000
        self.weeks = weeks
        self.stock = stock
        self.invest_amount = invest_amount
        self.beta = beta
        self.coin_price = []
        self.investment = []
        self.owned_coins = []
        self.assets = []

    def reset(self):
        self.coin_price.clear()
        self.investment.clear()
        self.owned_coins.clear()
        self.assets.clear()

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

        x_values = np.arange(0, 3.14 * 2+0.001, 3.14 * 2 / (self.weeks-1))
        templist = np.sin(x_values)
        self.coin_price = [30000 - abs(i) * 15000 for i in templist]
        akk = np.arange(start=0, stop=10, step=0.5)
        print(akk)
        # plt.plot(x_values,self.coin_price)
        # plt.show()

    def populate_stock_price(self):

        good_stock = True
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

        # if the stock price has less than 20 records, skip to next stock
        if len(self.coin_price) <= 20:
            print("Stock has less than 20 prices. Move to next one.")
            good_stock = False
            return good_stock

        # if stock price is less than self.weeks old, re-set self.weeks
        # to be earliest weeks available
        if len(self.coin_price) < self.weeks:
            self.weeks = len(self.coin_price)

        print("Weekly Price for " + self.stock)
        print(self.coin_price)
        return good_stock

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
        plt.savefig('figures2/' + my_file + ".png")
        plt.show()
        # clear the figure
        plt.cla()

    def plot_stock_and_result(self):

        title = self.stock + " Total Assets:" + str(round(self.assets[-1], 2)) + \
                "  Total Investment:" + str(round(self.investment[-1], 2)) + \
                "  Gain:" + str(round((self.assets[-1] - self.investment[-1]) / self.investment[-1] * 100, 2)) + "%"

        # 1st plot to show stock price
        plt.figure(figsize=(6, 9))
        plt.subplot(3, 1, 1)
        plt.title(title)
        plt.plot(range(0, self.weeks), self.coin_price)
        plt.grid()

        # 2nd plot to show regular investment
        plt.subplot(3, 1, 2)
        plt.title("Actual Investment vs. Assets")
        plt.plot(range(0, self.weeks), self.investment)
        plt.plot(range(0, self.weeks), self.assets)
        plt.grid()

        # 3rd plot to show number of shares owned
        plt.subplot(3, 1, 3)
        plt.title("Number of Shares Owned")
        plt.plot(range(0, self.weeks), self.owned_coins)
        plt.grid()

        # save the figures as stock_name.png in stocks folder
        plt.savefig('ETF_stocks/' + self.stock + ".png")
        plt.tight_layout()
        # plt.show()

        # clear the figured
        plt.cla()

    def create_ri_records(self):
        stock_rec = {
            "ticker": self.stock,
            "price": list(self.coin_price),
            "assets": list(self.assets),
            "shares": list(self.owned_coins),
            "growth_rate": round((self.assets[-1] - self.investment[-1]) / self.investment[-1] * 100, 2)
        }
        RegularInvest.ri_records.append(stock_rec)

        # write stock_rec to a file
        with open('ETF_records/' + self.stock + ".txt", 'w') as f:
            for key, value in stock_rec.items():
                f.write('%s:%s\n' % (key, value))
        pass

    @staticmethod
    def sort_growth_rate():
        print("sorting all stocks by growth rate...")
        print("This is all records:")
        print(RegularInvest.ri_records)
        sorted_ri_records = sorted(RegularInvest.ri_records, key=lambda k: k['growth_rate'],
                                   reverse=True)
        return sorted_ri_records
        pass
