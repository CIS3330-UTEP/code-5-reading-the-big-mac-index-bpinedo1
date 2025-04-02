import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    df = pd.read_csv(big_mac_file)
    df['date'] = pd.to_datetime(df['date']) #change date column into datetime or else we'll get keyerror #written with help of AI how to implement datetime shift
    price_year_df = df[(df['date'].dt.year == year) & (df['iso_a3'].str.lower() == country_code.lower())] #AI generated, filtering method
    mean_price = price_year_df['dollar_price'].mean()
    rounded_price = round(mean_price, 2)
    return rounded_price
    #why does & and and produce different results???

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv(big_mac_file)
    price_by_country_df = df[df['iso_a3'].str.lower() == country_code] #AI generated, method to filter
    mean_price = price_by_country_df['dollar_price'].mean()
    return round(mean_price, 2)
    #nan??? adding .str.lower fixed the nan issue
    

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    year_date = df[df['year'] == year] 
    cheap = year_date.loc[year_date['dollar_price'].idxmin()] #Written with the help of AI, how to implement .loc
    country_name = cheap['name']
    country_code = cheap['iso_a3']
    dollar_price = cheap['dollar_price']
    return f"{country_name}({country_code}): ${dollar_price:.1f}"

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv(big_mac_file)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year #AI generated, method to filter information
    year_date = df[df['year'] == year] #AI generated, method to filter information just broken into two parts opposed to 1 like above
    expensive = year_date.loc[year_date['dollar_price'].idxmax()] #Written with the help of AI, how to implement .loc
    country_name = expensive['name']
    country_code = expensive['iso_a3']
    dollar_price = expensive['dollar_price']
    return f"{country_name}({country_code}): ${dollar_price:.1f}"
    #just copy and paste from prior one and change idxmin to idxmax
    #Chat-GPT(4). Date of query (2025/3/2).Generated using
    #OpenAI Chat-GPT. https://chat.openai.com/

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010, "arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)
    
    #Chat-GPT(4). Date of query (2025/3/2).Generated using
    #OpenAI Chat-GPT. https://chat.openai.com/