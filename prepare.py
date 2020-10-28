import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import strftime

from acquire import get_total_sales_by_stores_data, get_germany_power_data



def prepare_store_data():
    '''
    This function reads in the stores total sales data
    and preps it for exploration
    '''
    #reads in the data and saves it as a dataframe
    df = get_total_sales_by_stores_data()
    #changes sales_date from object to date_time
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
    #creates a histogram of 'sale_amount'
    plot_hist(df, 'sale_amount', 'Total Items')
    #creates a histogram of 'item_price'
    plot_hist(df, 'item_price', 'Item Price')
    #sets the index as 'sale_date'
    df = df.set_index("sale_date").sort_index()
    #creates a 'month' column using the index
    df['month'] = df.index.month
    #creates a 'day_of_the_week' column using the index
    df['day_of_the_week'] = df.index.day_name()
    #creates a 'sales_total' by multiplying 'sale_amount' and 'item_price'
    df['sales_total'] = df.sale_amount * df.item_price
    return df

def prepare_power_data():
    '''
    This function read in the germany power data
    and preps it for exploration
    '''
    #reads in the data and saves it as a datframe
    df = get_germany_power_data()
    #lowercase all of the columns in the dataframe
    df.columns = [column.lower() for column in df]
    #changes 'Date' from object to date_time
    df.date = pd.to_datetime(df.date, format='%Y %m %d')
    #plots all the numeric columns in the dataframe
    plot_hist_num(df)
    #sets 'Date' as the Index
    df = df.set_index("date").sort_index()
    #creates a 'month' column using the index
    df['month'] = df.index.month
    #creates a 'year' column using the index
    df['year'] = df.index.year
    #fills all the nulls with zeros
    df = df.fillna(0)
    #adding addition of wind and solar
    df['wind_and_solar'] = df.wind + df.solar
    return df

def plot_hist(df, col, label):
    '''
    This function takes in a dataframe, 
    columns and label and creates 
    a distribution graph for that column
    '''
    plt.hist(df[col], ec='black')
    plt.title('Distribution for ' + label)
    plt.xlabel(label)
    plt.show()


def plot_hist_num(df):
    '''
    Function to take in a DataFrame,
    select only numeric dtypes and
    display histograms for each numeric column
    '''
    num_df = df.select_dtypes(include=np.number)
    num_df.hist(ec='black')
    plt.tight_layout()
    plt.show()