import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from numpy import quantile
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
    "./fcc-forum-pageviews.csv",
    index_col="date",
    names=["date", "views"],
    parse_dates=True,
    header=0,
)
print(df)

# Clean data
df = df[
    (df["views"] >= df["views"].quantile(0.025))
    & (df["views"] <= df["views"].quantile(0.975))
]


def draw_line_plot():
    df_line = df.copy()
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    df_bar = df.copy()
    # Copy and modify data for monthly bar plot

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax1 = plt.subplots(figsize=(12, 10))

    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_ylabel("Page Views")
    ax1.set_xlabel("Year")

    ax2 = fig.subplots()
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_ylabel("Page Views")
    ax2.set_xlabel("Month")

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
