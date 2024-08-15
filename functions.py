import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


#Bold and resent are used to change the appearance of text in the terminal(Makes text bold)
def bold_txt(text: str)-> str:
  BOLD = '\033[1m'
  RESET = '\033[0m'
  a = text
  return(f'{BOLD}{a}{RESET}')


#The function below asks for the user to input their own ticker and if tickers are given then they will be returned in a list which will be used in later functions.
#  OR if the user chooses to press enter then the function will return a list of preset tickers for future use.
def user_ticker(user = ['AMZN', 'AAPL', 'GOOG', 'TSLA', 'MSFT'])-> list:
  tick = input(bold_txt('Enter your tickers (each ticker should be separated by a space)\n(If you wish to test this script with preset ticker press enter):'))
  if not tick:
    return user
  else:
    user = list(tick.split(' '))
    return user

#The function below gets some general stock data for the stocks in tickers
def get_gene_stk_data(tickers: list):
  '''This functiion will get the general stock data for the tickers in the tickers list'''
  print(bold_txt('General information about stocks:'))
  gener_stk_data = []
  for ticker in tickers:
    stock = yf.Ticker(ticker)
    info = {
        'Ticker': ticker,
        'Company Name': stock.info.get('longName', 'N/A'),
        'Sector': stock.info.get('sector', 'N/A'),
        'Industry': stock.info.get('industry', 'N/A'),
        'Market Cap': stock.info.get('marketCap', 'N/A'),
        'PE Ratio': stock.info.get('trailingPE', 'N/A'),
    }
    gener_stk_data.append(info)
  gener_stk_data = pd.DataFrame(gener_stk_data)
  print(gener_stk_data)
  
     
#All the functions in this section take ticker as an input and output data frames containing the data of prices for the stocks in tickers and 
#return the data for their respective time frame(1 month, 6 months, 1 year, and 5 years).(Ex. fn.get_hist_data_6mon will get the data for the stocks for the previous 6 months)

def get_hist_data_1mon(tickers: list)-> pd.DataFrame:
  print(bold_txt('\nOne month stock data:'))
  hist_data_1mon = []
  
  for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    hist.insert(loc = 0,
                column = 'Ticker',
                value = ticker)
    hist_data_1mon.append(hist)
  hist_data_1mon = pd.concat(hist_data_1mon, axis= 0)
  hist_data_1mon = hist_data_1mon.reset_index()
  print(hist_data_1mon)
  return hist_data_1mon


def get_hist_data_6mon(tickers: list)-> pd.DataFrame:
  print(bold_txt('\nSix month stock data:'))
  hist_data_1mon = []
  
  for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")
    hist.insert(loc = 0,
      column = 'Ticker',
      value = ticker)   
    hist_data_1mon.append(hist)
  hist_data_1mon = pd.concat(hist_data_1mon, axis= 0)
  hist_data_1mon = hist_data_1mon.reset_index()
  print(hist_data_1mon)
  return hist_data_1mon


def get_hist_data_1year(tickers: list)-> pd.DataFrame:
  print(bold_txt('\nOne year stock data:'))
  hist_data_1mon = []
  
  for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period='1y')
    hist.insert(loc = 0,
      column = 'Ticker',
      value = ticker)    
    hist_data_1mon.append(hist)
  hist_data_1mon = pd.concat(hist_data_1mon, axis= 0)
  hist_data_1mon = hist_data_1mon.reset_index()
  print(hist_data_1mon)
  return hist_data_1mon


def get_hist_data_5year(tickers: list)-> pd.DataFrame:
  print(bold_txt('\nFive years stock data:'))
  hist_data_1mon = []
  
  for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="5y")
    hist.insert(loc = 0,
      column = 'Ticker',
      value = ticker)    
    hist_data_1mon.append(hist)
  hist_data_1mon = pd.concat(hist_data_1mon, axis= 0)
  hist_data_1mon = hist_data_1mon.reset_index()
  print(hist_data_1mon)
  return hist_data_1mon


#The following function takes the dataframes we created using the get_hist_data functions and groups the data by the ticker.
#Then it loops through the groups of tickers and uses the describe and mode functions to get the mean median and mode(s) which are then printed in a Data frame called a
def closing_info(data: pd.DataFrame)-> pd.DataFrame: 
  group = data.groupby('Ticker')

  for ticker, group_data in group:
    print(f'Information for {ticker}:')
    a = group_data['Close'].describe()
    a = a[['mean','50%']].rename({'50%':'Median'})
    mode_values = group_data['Close'].mode()
    if len(mode_values) > 1:
      a['mode'] = ','.join(map(str, mode_values.values))
    else:
      a['mode'] = mode_values.iloc[0]
    print(a)


#The following function takes ticker and data_5year and loops through tickers and for each ticker, it creates variables that have the date and the closing price for the current ticker.
#Then it plots the date and closing price using plt. Then the loop keeps going until all the ticker in tickers have gone through the loop.
def line_plot_data(tickers: list, data_5year: pd.DataFrame):
  for ticker in tickers:
    print(f'\nNow plotting: {ticker}')
    now = data_5year[data_5year['Ticker'] == ticker]
    date = now['Date']
    close_price = now['Close']
    plt.plot(date, close_price)
    plt.title(f'{ticker} closing prices over the last 5 years')
    plt.xlabel('Date')
    plt.ylabel('Closing price')
    plt.grid(True)
    plt.show()
  print(bold_txt('Finished plotting. Thank you, use our service again!'))
