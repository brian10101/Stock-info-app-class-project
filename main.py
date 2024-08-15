import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import functions as fn 


#In the function below we are calling the ticker function
tickers = fn.user_ticker()

#in this line of code we are calling the function get_gene_stk_data and passing tickers  as an argument
fn.get_gene_stk_data(tickers)

#In the following four lines of code we are calling the get_hist_data fuctions and passing tickers as an argument
data_1mon = fn.get_hist_data_1mon(tickers)
data_6mon = fn.get_hist_data_6mon(tickers)
data_1year = fn.get_hist_data_1year(tickers)
data_5year = fn.get_hist_data_5year(tickers)


#In the following four lines of code we are calling the get closing function and passing dataframes as an argument
print(fn.bold_txt('\n\nClosing information for previous month:\n'))
fn.closing_info(data_1mon)
print(fn.bold_txt('\n\nClosing information for previous six months:\n'))
fn.closing_info(data_6mon)
print(fn.bold_txt('\n\nClosing information for previous year:\n'))
fn.closing_info(data_1year)
print(fn.bold_txt('\n\nClosing information for previous five years:\n'))
fn.closing_info(data_5year)


#In the following four lines of code we are calling the line_plot_data function and passing tickers and data_5year as arguments
fn.line_plot_data(tickers, data_5year)
