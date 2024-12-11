import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
dir_df = '9-data-analysis-with-python\\page-view-time-series-visualizer-main\\fcc-forum-pageviews.csv'
df = pd.read_csv(dir_df, parse_dates=['date'])

# Clean data
cond1 = df['value'] >= df['value'].quantile(0.025)
cond2 = df['value'] <= df['value'].quantile(0.975)
df = df[cond1 & cond2]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('9-data-analysis-with-python\\page-view-time-series-visualizer-main\\line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar['date'].apply(lambda date: date.year)
    df_bar['month'] = df_bar['date'].apply(lambda date: date.month)
    df_bar = df_bar.groupby(['year', 'month'])
    df_bar = df_bar['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(8, 7), ylabel='Average Page Views', xlabel='Years').figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('9-data-analysis-with-python\\page-view-time-series-visualizer-main\\bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['Year'] = df_box['date'].apply(lambda date: date.year)
    df_box['month'] = df_box['date'].apply(lambda date: date.strftime('%b'))
    df_box['month_num'] = df_box['date'].apply(lambda date: date.month)
    df_box = df_box.sort_values('month_num')

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14,5))

    sns.boxplot(x=df_box['Year'], y=df_box['value'], ax=axs[0], palette=sns.color_palette('deep'))
    sns.boxplot(x=df_box['month'], y=df_box['value'], ax=axs[1], palette=sns.color_palette('pastel', n_colors=12))

    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')

    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('9-data-analysis-with-python\\page-view-time-series-visualizer-main\\box_plot.png')
    return fig
draw_box_plot()