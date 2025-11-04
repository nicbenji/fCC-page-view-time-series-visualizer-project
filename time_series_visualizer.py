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
    parse_dates=True,
)

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

long_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def draw_line_plot():
    df_line = df.copy()

    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.plot(df_line.index, df_line["value"])
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    df_bar = df.copy()
    # Copy and modify data for monthly bar plot
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    mean = df_bar.groupby(["year", "month"])["value"].mean().unstack()
    mean.columns = long_months

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 10))
    mean.plot(kind="bar", ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")
    ax.legend()

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
    fig, axd = plt.subplots(ncols=2, figsize=(12, 6))

    sns.boxplot(x="year", y="value", data=df_box, ax=axd[0])
    axd[0].set_title("Year-wise Box Plot (Trend)")
    axd[0].set_ylabel("Page Views")
    axd[0].set_xlabel("Year")

    sns.boxplot(x="month", y="value", data=df_box, order=months, ax=axd[1])
    axd[1].set_title("Month-wise Box Plot (Seasonality)")
    axd[1].set_ylabel("Page Views")
    axd[1].set_xlabel("Month")

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
