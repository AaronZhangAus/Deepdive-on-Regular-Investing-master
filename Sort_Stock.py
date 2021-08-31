import glob
import os

# read stock records from folder
folder_path = "records"

# store all stock to a list
stock_list = []


def read_stock_record():
    # iterate all .txt files
    for filename in glob.glob(os.path.join(folder_path, "*.txt")):
        with open(filename, 'r') as file:

            stock_dic = {}
            lines = file.readlines()
            for line in lines:
                (key, val) = line.split(":")

                # read in ticker
                if key == "ticker":
                    stock_dic["ticker"] = val.strip()

                # read in growth rate
                if key == "growth_rate":
                    stock_dic["growth_rate"] = float(val)

            stock_list.append(stock_dic)
    print(stock_list)


def main():

    read_stock_record()

    # sort stock records by their growth rate
    sorted_stock_records = sorted(stock_list, key=lambda k: k['growth_rate'],
                                  reverse=True)

    print("TOP 30 HIGHEST GAIN STOCKS FOR REGULAR INVESTING:")
    for i in sorted_stock_records[:30]:
        print("%s returns %s" % (i['ticker'], i['growth_rate']))


if __name__ == "__main__":
    main()
