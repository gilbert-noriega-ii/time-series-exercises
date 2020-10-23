import requests
import pandas as pd



#creating a function to retrieve items
def get_items():
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
    for number in range(1, data['payload']['max_page']):
        #moving into the next page of items
        response = requests.get(base_url + data['payload']['next_page'])
        #saving the as a json script
        data = response.json()
        #adding the next page of items onto the original dataframe
        df = pd.concat([df, pd.DataFrame(data['payload']['items'])], ignore_index=True)
    return df


def get_stores():
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
    return df



def get_sales():
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
    for number in range(1, data['payload']['max_page']):
        #moving into the next page of items
        response = requests.get(base_url + data['payload']['next_page'])
        #saving the as a json script
        data = response.json()
        #adding the next page of items onto the original dataframe
        df = pd.concat([df, pd.DataFrame(data['payload']['sales'])], ignore_index=True)
    return df