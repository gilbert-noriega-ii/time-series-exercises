import requests
import pandas as pd
import os



################################
def new_items_data():
    '''
    This function retrieves all items of all pages
    from the base url api and saves it as a dataframe
    '''
    #saving the base url
    base_url = 'https://python.zach.lol'
    #opening/visiting the url
    response = requests.get('https://python.zach.lol/api/v1/items')
    #saving the data as a json script
    data = response.json()
    #saving the json script as a dataframe
    df = pd.DataFrame(data['payload']['items'])
    #creating a loop to scan all the items pages
    for pages in range(1, data['payload']['max_page']):
        #moving into the next page of items
        response = requests.get(base_url + data['payload']['next_page'])
        #saving the as a json script
        data = response.json()
        #adding the next page of items onto the original dataframe
        df = pd.concat([df, pd.DataFrame(data['payload']['items'])], ignore_index=True)
    #saves dataframe as a csv for quicker access
    df.to_csv('items_df.csv')
    return df


def get_items_data(cached=False):
    '''
    This function reads in items data from the api if cached == False 
    or if cached == True reads in items df from a csv file, returns df.
    '''
    if cached or os.path.isfile('items_df.csv') == False:
        df = new_items_data()
    else:
        df = pd.read_csv('items_df.csv', index_col=0)
    return df

################################

def new_stores_data():
    '''
    This function retrieves all stores of all pages
    from the base url api and saves it as a dataframe
    '''
    #opening/visiting the url
    response = requests.get('https://python.zach.lol/api/v1/stores')
    #saving the data as a json script
    data = response.json()
    #saving the json script as a dataframe
    df = pd.DataFrame(data['payload']['stores'])
    #saves dataframe as a csv for quicker access
    df.to_csv('stores_df.csv')
    return df


def get_stores_data(cached=False):
    '''
    This function reads in stores data from the api if cached == False 
    or if cached == True reads in stores df from a csv file, returns df.
    '''
    if cached or os.path.isfile('stores_df.csv') == False:
        df = new_stores_data()
    else:
        df = pd.read_csv('stores_df.csv', index_col=0)
    return df



################################


def new_sales_data():
    '''
    This function retrieves all sales of all pages
    from the base url api and saves it as a dataframe
    '''
    #saving the base url
    base_url = 'https://python.zach.lol'
    #opening/visiting the url
    response = requests.get('https://python.zach.lol/api/v1/sales')
    #saving the data as a json script
    data = response.json()
    #saving the json script as a dataframe
    df = pd.DataFrame(data['payload']['sales'])
    #creating a loop to scan all the items pages
    for pages in range(1, data['payload']['max_page']):
        #moving into the next page of items
        response = requests.get(base_url + data['payload']['next_page'])
        #saving the as a json script
        data = response.json()
        #adding the next page of items onto the original dataframe
        df = pd.concat([df, pd.DataFrame(data['payload']['sales'])], ignore_index=True)
    #saves dataframe as a csv for quicker access
    df.to_csv('sales_df.csv')
    return df

def get_sales_data(cached=False):
    '''
    This function reads in sales data from the api if cached == False 
    or if cached == True reads in sales df from a csv file, returns df.
    '''
    if cached or os.path.isfile('sales_df.csv') == False:
        df = new_sales_data()
    else:
        df = pd.read_csv('sales_df.csv', index_col=0)
    return df


################################

def new_total_sales_by_stores_data(cached=True):
    '''
    This function retrieves all sales, items, and stores of all pages
    from the base url api and merges it as a dataframe
    '''
    #retrieving all items
    items = get_items_data(cached)
    #retrieving all stores
    stores = get_stores_data(cached)
    #retrieving all sales
    sales = get_sales_data(cached)
    #merging stores and sales by store id
    df = sales.merge(stores, left_on='store', right_on='store_id')
    #merging previous df and items by item id
    newdf = df.merge(items, left_on = 'item', right_on = 'item_id')
    #writing it to a csv for quicker access
    newdf.to_csv('total_sales_by_store_df.csv')
    return newdf

def get_total_sales_by_stores_data(cached=False):
    '''
    This function reads in items data from the api if cached == False 
    or if cached == True reads in items df from a csv file, returns df.
    '''
    if cached or os.path.isfile('total_sales_by_store_df.csv') == False:
        df = new_total_sales_by_stores_data()
    else:
        df = pd.read_csv('total_sales_by_store_df.csv', index_col=0)
    return df


def get_germany_power_data():
    '''
    This function retrieves the Open Power Systems Data 
    for Germany and saves it as a dataframe
    '''
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    return df