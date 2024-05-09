import pandas as pd
import streamlit as st
from datetime import datetime,timedelta
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px
from bs4 import BeautifulSoup
import requests
import re

st.set_page_config(page_title="Stocks")

st.sidebar.markdown("<h1 style='color:#FB607F;text-align:center;'>Welcome to the Stock App!</h1>",unsafe_allow_html=True)

st.sidebar.markdown("<br/>",unsafe_allow_html=True)

st.sidebar.write('<h3>Input the stock code</h3>',unsafe_allow_html=True)

ticker = st.sidebar.text_input(label='Ticker Symbol',placeholder='Enter the Ticker Symbol')

ticker = ticker.upper()

start = st.sidebar.date_input(label='Start Date',value=None)

end = st.sidebar.date_input(label='End Date',value='today')

indicators = st.sidebar.multiselect(label='Select Indicators',options=['Open','High','Low','Close'],default=['Close'],placeholder='Select indicators')


submit = st.sidebar.button(label='Submit')

def company_name(ticker):
    try:
        company = yf.Ticker(ticker)
        return company.info['longName']
    except Exception as e:
        print("Error:", e)
        return None

start_time = datetime.now()

if submit:

    company = company_name(ticker)

    if (company==None):
        st.error('Company not found. Please try again!')

    elif (start==None):
        st.error('Please enter the starting date!')

    elif (end==None):
        st.error('Please enter the ending date!')

    elif (indicators==None):
        st.error('Please select the indicators!')
    
    else:
        response = requests.get(url=f'https://en.wikipedia.org/wiki/{company}')

        soup = BeautifulSoup(response.content,'html.parser')

        rows = soup.find_all('div',class_='mw-content-ltr mw-parser-output')

        para = rows[0].find_all('p')

        content = str(para[1]) + str(para[2]) + str(para[3]) + str(para[4])

        pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*?)"(?:[^>]*?\s+)?title="([^"]*?)"(?:[^>]*?)>(.*?)<\/a>'

        cleaned_content = re.sub(pattern, r'\3', content)

        pattern = r'\[\d+\]'

        cleaned_content = re.sub(pattern, '', cleaned_content)


        st.markdown(f"<h2 style='text-align:center'>{company}</h2>",unsafe_allow_html=True)

        code = f"""
        <div style="line-height:2;padding:20px;background-color:#FFF0F5;border-radius:10px;color:black;border-bottom:10px;">
        {cleaned_content}
        </div>
        """
        st.markdown(code,unsafe_allow_html=True)

        data = yf.download(tickers=ticker,start=start.isoformat(),end=end.isoformat())

        plt.style.use('dark_background')

        fig = px.line(data_frame=data,x=data.index,y=indicators,markers=True,labels={'variable':'Variable','value':'Value'})

        st.write('<br />',unsafe_allow_html=True)

        st.write(f'<h4 style="text-align:center">Line chart of Indicators of {company}</h4>',unsafe_allow_html=True)

        st.write(fig)