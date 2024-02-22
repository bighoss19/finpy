import requests
import webbrowser

while True:
    data = input("Enter Data Shortcut: ")
#help command 
    if data.lower() == 'help':
        print("Available Commands:")
        print("'fwt' = CME Fed Watch Tool")
        print("'cpi' = Consumer Price Index")
        print("'gdp' = Gross Domestic Product")
        print("'ffr' = Fed Funds Rate")
        print("'emp' = Unemployment Rates")
        print("'y102' = 10y Minus 2y")
        print("'sec' = SEC Edgar Ticker Search")
        print("'cal' = Macro Economic Calendar investing.com")
        print("'er' = Earnings Calendar Yahoo Finance")
        print("'bio' = Basic Company Bio Yahoo Finance")
        print("'fcf' = Free Cash Flow from YCharts")


    
    allowed_type = [ 'help', 'exit', 'fwt', 'cpi', 'gdp', 'emp', 'ffr', 'y102', 'cal', 'sec', 'er', 'bio', 'fcf']

    if data not in allowed_type:
        print("Invalid input, type 'help' or 'exit'")
    
    elif data == 'fwt': 
        webbrowser.open('https://www.cmegroup.com/trading/interest-rates/countdown-to-fomc.html')
    elif data == 'cpi':
        webbrowser.open("https://fred.stlouisfed.org/graph/?g=rocU")
    elif data == 'gdp':
        webbrowser.open("https://fred.stlouisfed.org/series/GDP")
    elif data == 'emp':
        webbrowser.open("https://fred.stlouisfed.org/series/UNRATE")    
    elif data == 'ffr':
        webbrowser.open("https://fred.stlouisfed.org/series/FEDFUNDS")
    elif data == 'y102':
        webbrowser.open("https://fred.stlouisfed.org/series/T10Y2Y")
    elif data == 'cal':
        webbrowser.open('https://www.investing.com/economic-calendar/')
    elif data.lower() == 'exit':
        print("Exiting the program...")
        break
    
    elif data == 'sec':
        secticker = input("Enter ticker symbol: ")

        if secticker.lower() == 'exit':
            print("Exiting program...")
            break
        
            
        sec_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={secticker}"
        webbrowser.open(sec_url)         
        break        
    elif data == 'er':
        erticker = input("Enter ticker symbol: ")
        if erticker.lower() == 'exit':
            print("Exiting program...")
            break
        
        er_url = f"https://finance.yahoo.com/calendar/earnings/?symbol={erticker}"
        webbrowser.open(er_url)
    elif data == 'bio':
        bioticker = input('Enter ticker symbol: ')
        if bioticker.lower() == 'exit':
            print("Exiting program...")
            break
        
        bio_url = f"https://finance.yahoo.com/quote/{bioticker}/profile?p={bioticker}"
        webbrowser.open(bio_url)
        break
    elif data == 'fcf':
        fcfticker = input("Enter ticker symbol: ").upper() 
        if fcfticker.lower() == 'exit':
            print("Exiting program...")
            break
        
        fcf_url = f"https://ycharts.com/companies/{fcfticker}/free_cash_flow"
        webbrowser.open(fcf_url)
        break



    else:
        print("Invalid input, type 'help'")