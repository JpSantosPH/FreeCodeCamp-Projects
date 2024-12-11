import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('9-data-analysis-with-python\\sea-level-predictor-main\\epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()

    x_data = df['Year']
    y_data = df['CSIRO Adjusted Sea Level']
    plt.scatter(x_data, y_data)

    # Create first line of best fit
    line1 = linregress(x_data, y_data)
    m1 = line1.slope
    b1 = line1.intercept
    x1 = pd.Series(i for i in range(1880, 2051))
    y1 = m1*x1 + b1
    plt.plot(x1, y1, color='orange')

    # Create second line of best fit
    cond2 = x_data >= 2000
    line2 = linregress(x_data[cond2], y_data[cond2])
    m2 = line2.slope
    b2 = line2.intercept
    x2 = pd.Series(i for i in range(2000, 2051))
    y2 = m2*x2 + b2
    plt.plot(x2, y2, color='red')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('9-data-analysis-with-python\\sea-level-predictor-main\\sea_level_plot.png')
    return plt.gca()

draw_plot()