import matplotlib.pyplot as plt
import pandas as pd
import os
def plot_timer_chain_with_csv():
        dataSet = pd.read_csv("data/case0/test0.csv")
        x = dataSet['serial']
        y = dataSet['time_chain']
        plt.plot(x, y, linewidth=2)
        plt.legend(loc="upper left")
        plt.show()
def plot_sin_chain_with_csv():
        dataSet = pd.read_csv("data/case1/test0.csv")
        x = dataSet['serial'][:100]
        y = dataSet['sin'][:100]
        plt.plot(x, y, linewidth=2)
        plt.legend(loc="upper left")
        plt.show()
if __name__ == "__main__":
    print(os.getcwd())
    # plt.switch_backend('agg')
#     plot_timer_chain_with_csv()
    plot_sin_chain_with_csv()
    print('end')