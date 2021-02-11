
# AUTHOR: Matthew Frechette

import os
import requests
import datetime

# Open High Low Close - stores the data of that current stock's day
class OHLC:

    # initiates the OHLC object, these will store the historical data from the stock
    def __init__ (self, open, high, low, close, month, day, year, hour=0, minute=0, volume=None):
        self.open = open
        self.high = high
        self.low = low 
        self.close = close
        self.month = month
        self.day = day
        self.year = year
        self.hour = hour
        self.minute = minute
        self.volume = volume

        self.movingAverage20 = None
        self.movingAverage50 = None

        return


# stores data about a stock's earning, expected, actual, date, etc. 
class EarningsDay:

    def __init__ (self, month, day, year, eps, time, expectedEps=None, revenue=None, expectedRevenue=None):
        self.month = month
        self.day = day
        self.year = year
        self.eps = eps
        self.expectedEps = expectedEps
        self.revenue = revenue
        self.expectedRevenue = expectedRevenue
        self.time = time

    
# returns a list of OHLC objects relative to the stock ticker
def FMPgetStockHistoricalData(stockTicker, apiKey):

    historicalDataUrl = "https://financialmodelingprep.com/api/v3/historical-price-full/" + stockTicker + "?timeseries=10000&apikey=" + apiKey

    try:
        historicalDataJSON = requests.get(historicalDataUrl).json()
        historicalDataJSON = historicalDataJSON["historical"] # gets all of the historical json data from the page
    except:
        return None

    
    historicalData = [] # list of OHLC objects

    for i in range(len(historicalDataJSON)):
        dayData = historicalDataJSON[i]

        date = dayData["date"]
        date = date.replace("-"," ").split()
        year = date[0]
        month = date[1]
        day = date[2]

        open = dayData["open"]
        high = dayData["high"]
        low = dayData["low"]
        close = dayData["close"]
        volume = dayData["volume"]

        # this is the OHLC object that will be inserted into the list
        ohlcData = OHLC(open, high, low, close, month, day, year, volume=volume)

        # checks to see if we can calculate the moving average for this data
        if (len(historicalData) >= 20): # perform 20 period moving average calc on this data piece
            ohlcData.movingAverage20 = getAverageOfClose(historicalData[-20:]) # gets the last 20 objects in the list

        if (len(historicalData) >= 50): # perform 50 period moving average calc on this data piece
            ohlcData.movingAverage50 = getAverageOfClose(historicalData[-50:]) # gets the last 50 objects in the list



        historicalData.insert(0, ohlcData)

    return historicalData # []


# gets the average close price of all data pieces in the list (used for moving average function within the data pull function)
def getAverageOfClose(listOfOHLC):
    total = 0
    average = 0
    lenOfList = len(listOfOHLC)
    for data in listOfOHLC:
        total += data.close

    average = total / lenOfList
    return average

# typically, stocks are looked to be in an uptrend when the price of the equity is currently greater than the 20 and 50 period moving averages. 
# this function will help me get move information of the stocks and use it to compare another variable to the change in price during earnings
def calculateStockMovingAverage (listOfOHLC, period):

    listOfMovingAverages = [] # in the same order as the list of the OHLC history 
    # calculates the moving average of all the days
    currentMovingAverage = 0
    for i in range(period,len(listOfOHLC)):
        for p in range(1,period+1):
            currentMovingAverage += listOfOHLC[i-p].close
        currentMovingAverage /= period
        listOfMovingAverages += [currentMovingAverage]

    return listOfMovingAverages

# finds out whether of not the current stock price is above or below the N period moving average
def aboveMovingAverage (listOfOHLC, period):
    listOfMovingAverages = calculateStockMovingAverage(listOfOHLC, period)

    currentDayClose = listOfOHLC[-1].close
    if (currentDayClose > listOfMovingAverages[-1]):
        return True
    else:
        return False

def belowMovingAverage (listOfOHLC, period):
    if (aboveMovingAverage(listOfOHLC, period)):
        return False
    else:
        return True

def FMPfindStockEarningsData (stockTicker, apiKey):
    
    earningsURL = "https://financialmodelingprep.com/api/v3/historical/earning_calendar/" + stockTicker + "?limit=1000&apikey=" + apiKey

    try:
        earningsDataJSON = requests.get(earningsURL).json()
    except:
        return None
      
    allEarningsDays = [] # list holds all of the earningsday objects and returns them to the user
    for earningsData in earningsDataJSON:

        date = earningsData["date"]
        date = date.split("-")
        month = date[1]
        day = date[2]
        year = date[0]

        symbol = earningsData["symbol"] # this isn't used yet but as the program progresses I will also store the ticker name within these objects
        eps = earningsData["eps"] # earnings per share
        epsEstimate = earningsData["epsEstimated"]
        time = earningsData["time"] # either AMC (after market close) or BMO (before market open)
        revenue = earningsData["revenue"]
        revenueEstimated = earningsData["revenueEstimated"]

        allEarningsDays.insert(0, EarningsDay(month, day, year, eps, time, epsEstimate, revenue, revenueEstimated))

    return allEarningsDays

def getSPYcompanies (apiKey):
    
    url = "https://financialmodelingprep.com/api/v3/sp500_constituent?apikey=" + apiKey
    stockTickerList = []
    try:
        spyStockDataJSON = requests.get(url).json()
    except:
        return None

    for stockdata in spyStockDataJSON:
        stockTickerList += [stockdata["symbol"]]

    return stockTickerList


def earningsCalculations (stockHistory, earningsHistory):

    earningsAndPriceChanges = []

    for earning in earningsHistory: # runs through all the earnings objects that the stock has
        for i in range(len(stockHistory)): # runs through all the stock days in order to find the day that the earning occured
            dayData = stockHistory[i]
            if (earning.day == dayData.day
                and earning.month == dayData.month
                and earning.year == dayData.year): # finding the earning day 
                if (earning.time == "bmo"): # before market open
                    # compare the past days close with the current day's open and close price
                    previousEarningsDayOHLC = stockHistory[i-1]
                    earningDayOHLC = dayData
                elif (earning.time == "amc"): # after market close
                    # compare the current days close with the next day's open and close prices
                    previousEarningsDayOHLC = dayData
                    earningDayOHLC = stockHistory[i+1] # if the earnings happens after the market closes then we want to see how the next day responds
                else: # DMH --> during market hours, treat this the same as amc
                    previousEarningsDayOHLC = dayData
                    earningDayOHLC = stockHistory[i+1] # if the earnings happens after the market closes then we want to see how the next day responds
                # here are the stats from the earning day
                changeFromPastClose = earningDayOHLC.close - previousEarningsDayOHLC.close
                changeFromOpen = earningDayOHLC.close - earningDayOHLC.open
                earningsAndPriceChanges += [[earning, dayData, changeFromPastClose, changeFromOpen]] 
                break

    # returns [[earningobj, OHLC from earning day, changeFromPastClose, changeFromOpen], ...]
    return earningsAndPriceChanges


    

    return None



if __name__ == "__main__":
    # main function
    
    apiKey = None
    # if there is an apikey file/data read from the file
    if (os.path.exists("apiKey.dat")): 
        file = open("apiKey.dat","r")
        apiKey = file.readline()
        file.close()
    # if there is no apikey file, ask the user and write to file
    else:
        apiKey = input("Enter your FMP API key:") 
        file = open("apiKey.dat","w")
        file.write(apiKey)
        file.close()
        
    

    # THESE VARIABLES STORE ALL OF THE DATA FROM ALL OF THE STOCKS COMBINDED
    totaldataPieces = 0 # total of all ohlc data objects scanned
    totalinUptrend = 0 # all the earnings days when the stock is in an uptrend
    totalinDowntrend = 0 # all the earning days when the stock is in a downtrend

    totalgoodEarnings = 0 # the earnings where the actual EPS is higher than the expected EPS
    totalgoodEarningsPriceIncreaseFromOpen = 0 # if we have good earnings, and the price of the stock increases from market open
    totalgoodEarningsPriceIncreaseFromPastClose = 0 # if we have good earnings, and the price of the stock increases from the last market days close
    totalgoodEarningsPriceDecreaseFromOpen = 0 # if we have good earnings, and the price of the stock decreases from the market open
    totalgoodEarningsPriceDecreaseFromPastClose = 0 # if we have good earnings, and the price of the stock decreases from the last market day close

    totalgoodEarningsPriceIncreaseFromOpenUptrend = 0 # if we have good earnings, price increase from open, and stock is in an uptrend
    totalgoodEarningsPriceIncreaseFromPastCloseUptrend = 0 # if we have good earnings, price increased from close, and stock is in an uptrend
    totalgoodEarningsPriceIncreaseFromOpenDowntrend = 0 # if we have good earnings, price increased from open, and stock is in a downtrend
    totalgoodEarningsPriceIncreaseFromPastCloseDowntrend = 0 # if we have good earnings, price increased from the past close, and the stock is in a downtrend
    totalgoodEarningsPriceDecreaseFromOpenUptrend = 0 # if we have good earnings, price decreases from open, and the stock is in an uptrend 
    totalgoodEarningsPriceDecreaseFromPastCloseUptrend = 0 # if we have good earnings, price decreases from past close, and the stock is in an uptrend
    totalgoodEarningsPriceDecreaseFromOpenDowntrend = 0 # if we have good earnings, price decreses from open, and the stock is in a downtrend
    totalgoodEarningsPriceDecreaseFromPastCloseDowntrend = 0 # if we have good earnings, price decreased from the past close, and the stock is in a downtrend

    totalgoodEarningsUptrend = 0
    totalgoodEarningsDowntrend = 0

    totalbadEarnings = 0 # earnings where actual EPS is lower than the expected EPS
    totalbadEarningsPriceIncreaseFromOpen = 0 # SEE DESCRIPTIONS ABOVE. 
    totalbadEarningsPriceIncreaseFromPastClose = 0 # ALL THESE FOR BAD EARNINGS
    totalbadEarningsPriceDecreaseFromOpen = 0
    totalbadEarningsPriceDecreaseFromPastClose = 0
    
    totalbadEarningsPriceIncreaseFromOpenUptrend = 0
    totalbadEarningsPriceIncreaseFromPastCloseUptrend = 0
    totalbadEarningsPriceIncreaseFromOpenDowntrend = 0
    totalbadEarningsPriceIncreaseFromPastCloseDowntrend = 0
    totalbadEarningsPriceDecreaseFromOpenUptrend = 0
    totalbadEarningsPriceDecreaseFromPastCloseUptrend = 0
    totalbadEarningsPriceDecreaseFromOpenDowntrend = 0
    totalbadEarningsPriceDecreaseFromPastCloseDowntrend = 0

    totalbadEarningsUptrend = 0
    totalbadEarningsDowntrend = 0


    stockList = ["AAPL","MSFT","TWLO","AAL","AA","AB","BA","BMO"]
    stockList = getSPYcompanies(apiKey) # gets all of the SPY stock list
    print("LEN:", len(stockList))
    stockList = ["AAPL"]

    startTime = datetime.datetime.now()

    for stockTicker in stockList:

        # GATHERS THE STOCK DATA
        stockHistoricalData = FMPgetStockHistoricalData(stockTicker, apiKey) # gets all of the historical stock data
        
        if (stockHistoricalData == None):
            continue

        # this doesn't go back all the way, while doing the full project we will pull data from the begining of the stock IPO
        totaldataPieces += len(stockHistoricalData)

        print(len(stockHistoricalData), "data pieces found for", stockTicker) # returns the # of data points


        # EARNINGS DATA... CALCULATIONS
        # gives a list of the most recent earnings from the stock that you picked
        allEarningsData = FMPfindStockEarningsData(stockTicker, apiKey)
        if (len(allEarningsData) == 0): # if there is no stock earnings data found for the company
            continue

        mostRecentEarningsData = allEarningsData[-1]
        earningsCalcs = earningsCalculations(stockHistoricalData, allEarningsData)


        inUptrend = [] # all the earnings days when the stock is in an uptrend
        inDowntrend = [] # all the earning days when the stock is in a downtrend

        goodEarnings = [] # the earnings where the actual EPS is higher than the expected EPS
        goodEarningsPriceIncreaseFromOpen = [] # if we have good earnings, and the price of the stock increases from market open
        goodEarningsPriceIncreaseFromPastClose = [] # if we have good earnings, and the price of the stock increases from the last market days close
        goodEarningsPriceDecreaseFromOpen = [] # if we have good earnings, and the price of the stock decreases from the market open
        goodEarningsPriceDecreaseFromPastClose = [] # if we have good earnings, and the price of the stock decreases from the last market day close

        goodEarningsPriceIncreaseFromOpenUptrend = [] # if we have good earnings, price increase from open, and stock is in an uptrend
        goodEarningsPriceIncreaseFromPastCloseUptrend = [] # if we have good earnings, price increased from close, and stock is in an uptrend
        goodEarningsPriceIncreaseFromOpenDowntrend = [] # if we have good earnings, price increased from open, and stock is in a downtrend
        goodEarningsPriceIncreaseFromPastCloseDowntrend = [] # if we have good earnings, price increased from the past close, and the stock is in a downtrend
        goodEarningsPriceDecreaseFromOpenUptrend = [] # if we have good earnings, price decreases from open, and the stock is in an uptrend 
        goodEarningsPriceDecreaseFromPastCloseUptrend = [] # if we have good earnings, price decreases from past close, and the stock is in an uptrend
        goodEarningsPriceDecreaseFromOpenDowntrend = [] # if we have good earnings, price decreses from open, and the stock is in a downtrend
        goodEarningsPriceDecreaseFromPastCloseDowntrend = [] # if we have good earnings, price decreased from the past close, and the stock is in a downtrend

        goodEarningsUptrend = []
        goodEarningsDowntrend = []

        badEarnings = [] # earnings where actual EPS is lower than the expected EPS
        badEarningsPriceIncreaseFromOpen = [] # SEE DESCRIPTIONS ABOVE. 
        badEarningsPriceIncreaseFromPastClose = [] # ALL THESE FOR BAD EARNINGS
        badEarningsPriceDecreaseFromOpen = []
        badEarningsPriceDecreaseFromPastClose = []
    
        badEarningsPriceIncreaseFromOpenUptrend = []
        badEarningsPriceIncreaseFromPastCloseUptrend = []
        badEarningsPriceIncreaseFromOpenDowntrend = []
        badEarningsPriceIncreaseFromPastCloseDowntrend = []
        badEarningsPriceDecreaseFromOpenUptrend = []
        badEarningsPriceDecreaseFromPastCloseUptrend = []
        badEarningsPriceDecreaseFromOpenDowntrend = []
        badEarningsPriceDecreaseFromPastCloseDowntrend = []

        badEarningsUptrend = []
        badEarningsDowntrend = []

        # runs through all calculations of earnings days of the stock
        for earningData in earningsCalcs:

            earningDay = earningData[0] # returns the earnings days object, stores the day, time, expected eps etc
            ohlcData = earningData[1]
            changeFromPastClose = earningData[2] # gets the price change from the past close. This is useful becasue sometimes a stock will gap up during premarket trading
            changeFromOpen = earningData[3] # change during the open market hours

            # TYPICALLY, PRICES WILL MOVE UP WITH GOOD EARNINGS... HOWEVER THIS IS NOT ALWAYS THE CASE

            if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                inUptrend += [earningData]
                totalinUptrend += 1
            else: # downtrend
                inDowntrend += [earningData]
                totalinDowntrend += 1

            # GOOD EARNINGS! --- EPS is more than expected EPS 
            if (earningDay.eps == None or earningDay.expectedEps == None): # if there is an error with the eps or expected eps data
                continue

            if (earningDay.eps > earningDay.expectedEps):
                goodEarnings += [earningData]
                totalgoodEarnings += 1

                if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                    and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                    goodEarningsUptrend += [earningData]
                    totalgoodEarningsUptrend += 1
                else: # downtrend
                    goodEarningsDowntrend += [earningData]
                    totalgoodEarningsDowntrend += 1

                if (changeFromPastClose > 0): # (+) positive price change from last close (this includes the afterhours market)
                    goodEarningsPriceIncreaseFromPastClose += [earningData]
                    totalgoodEarningsPriceIncreaseFromPastClose += 1

                    if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                        and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                        goodEarningsPriceIncreaseFromPastCloseUptrend += [earningData]
                        totalgoodEarningsPriceIncreaseFromPastCloseUptrend += 1
                    else: # downtrend
                        goodEarningsPriceIncreaseFromPastCloseDowntrend += [earningData]
                        totalgoodEarningsPriceIncreaseFromPastCloseDowntrend += 1
                else: # (-) negative price movement from the last close (this includes the afterhours market)
                    goodEarningsPriceDecreaseFromPastClose += [earningData]
                    totalgoodEarningsPriceDecreaseFromPastClose += 1

                    if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                        and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                        goodEarningsPriceDecreaseFromPastCloseUptrend += [earningData]
                        totalgoodEarningsPriceDecreaseFromPastCloseUptrend += 1
                    else: # downtrend
                        goodEarningsPriceDecreaseFromPastCloseDowntrend += [earningData]
                        totalgoodEarningsPriceDecreaseFromPastCloseDowntrend += 1

                if (changeFromOpen > 0): # (+) positive price change from the current days open (this does not account from premarket activity / price gaps at open)
                    goodEarningsPriceIncreaseFromOpen += [earningData]
                    totalgoodEarningsPriceIncreaseFromOpen += 1
                    if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                        and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                        goodEarningsPriceIncreaseFromOpenUptrend += [earningData]
                        totalgoodEarningsPriceIncreaseFromOpenUptrend += 1
                    else: # downtrend
                        goodEarningsPriceIncreaseFromOpenDowntrend += [earningData]
                        totalgoodEarningsPriceIncreaseFromOpenDowntrend += 1
                else:
                    goodEarningsPriceDecreaseFromOpen += [earningData]
                    totalgoodEarningsPriceDecreaseFromOpen += 1

                    if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                        and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                        goodEarningsPriceDecreaseFromOpenUptrend += [earningData]
                        totalgoodEarningsPriceDecreaseFromOpenUptrend += 1
                    else: # downtrend
                        goodEarningsPriceDecreaseFromOpenDowntrend += [earningData]
                        totalgoodEarningsPriceDecreaseFromOpenDowntrend += 1

            # BAD EARNINGS! --- EPS is less than expected EPS 
            else: 
                badEarnings += [earningData]
                totalbadEarnings += 1

                if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                    and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                    badEarningsUptrend += [earningData]
                    totalbadEarningsUptrend += 1
                else: # downtrend
                    badEarningsDowntrend += [earningData]
                    totalbadEarningsDowntrend += 1

                if (changeFromPastClose > 0): # (+) positive price change from last close (this includes the afterhours market)
                    badEarningsPriceIncreaseFromPastClose += [earningData]
                    totalbadEarningsPriceIncreaseFromPastClose += 1

                    if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                        and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                        badEarningsPriceIncreaseFromPastCloseUptrend += [earningData]
                        totalbadEarningsPriceIncreaseFromPastCloseUptrend += 1
                    else: # downtrend
                        badEarningsPriceIncreaseFromPastCloseDowntrend += [earningData]
                        totalbadEarningsPriceIncreaseFromPastCloseDowntrend += 1
                else: # (-) negative price movement from the last close (this includes the afterhours market)
                    badEarningsPriceDecreaseFromPastClose += [earningData]
                    totalbadEarningsPriceDecreaseFromPastClose += 1
                    if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                        and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                        badEarningsPriceDecreaseFromPastCloseUptrend += [earningData]
                        totalbadEarningsPriceDecreaseFromPastCloseUptrend += 1
                    else: # downtrend
                        badEarningsPriceDecreaseFromPastCloseDowntrend += [earningData]
                        totalbadEarningsPriceDecreaseFromPastCloseDowntrend += 1
                if (changeFromOpen > 0): # (+) positive price change from the current days open (this does not account from premarket activity / price gaps at open)
                    badEarningsPriceIncreaseFromOpen += [earningData]
                    totalbadEarningsPriceIncreaseFromOpen += 1
                    if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                        and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                        badEarningsPriceIncreaseFromOpenUptrend += [earningData]
                        totalbadEarningsPriceIncreaseFromOpenUptrend += 1
                    else: # downtrend
                        badEarningsPriceIncreaseFromOpenDowntrend += [earningData]
                        totalbadEarningsPriceIncreaseFromOpenDowntrend += 1
                else:
                    badEarningsPriceDecreaseFromOpen += [earningData]
                    totalbadEarningsPriceDecreaseFromOpen += 1
                    if (ohlcData.movingAverage20 != None and ohlcData.movingAverage20 > ohlcData.open
                        and ohlcData.movingAverage50 != None and ohlcData.movingAverage50 > ohlcData.open): # the stock is above the 20 and 50 moving average and is said to be in an uptrend
                        badEarningsPriceDecreaseFromOpenUptrend += [earningData]
                        totalbadEarningsPriceDecreaseFromOpenUptrend += 1
                    else: # downtrend
                        badEarningsPriceDecreaseFromOpenDowntrend += [earningData]
                        totalbadEarningsPriceDecreaseFromOpenDowntrend += 1

    
        # prints out the percentage of price increases/decrease to positive/negative earnings... 
        # STOCK CALCS STOCK CALCS STOCK CALCS STOCK CALCS STOCK CALCS STOCK CALCS STOCK CALCS STOCK CALCS STOCK CALCS 
        
        '''
        print("\n\n")
        
        # MOVING AVERAGES 
        # if the currentPriceIsAbove N periods of moving averages 
        if (aboveMovingAverage(stockHistoricalData, 20)): # 20 period MA
            print ("20 MA: ▲")
        else:
            print("20 MA: ▼")

        if (aboveMovingAverage(stockHistoricalData, 50)): # 20 period MA
            print ("50 MA: ▲")
        else:
            print("50 MA: ▼")

        print("\n")

        print("\n")
        print("Total Earnings Data Found:", len(allEarningsData))
        print("Earnings Calculations Completed:", len(earningsCalcs)) # should result the same number as len(allEarningsData)


        print("Total Good Earnings:", len(goodEarnings))
        print("Total Bad Earnings:", len(badEarnings))
    
        # checks all to make sure there is no /0 error
        # Finds the likelihood of a company beating earnings solely on what the trend of the stock is doing.
        if (len(inUptrend) == 0):
            percGoodEarningsUptrend = 0
        else:
            percGoodEarningsUptrend = len(goodEarningsUptrend) / len(inUptrend) * 100
        print("% of beat earnings while stock is in an uptrend:", str(percGoodEarningsUptrend) + "%")
        if (len(inDowntrend) == 0):
            percBadEarningsDowntrend = 0
        else:
            percBadEarningsDowntrend = len(badEarningsDowntrend) / len(inDowntrend) * 100
        print("% of missed earnings while stock is in a downtrend:", str(percBadEarningsDowntrend) + "%")

        print("\n\n")

        # Finds the likelihood of a stock’s price movement based on earnings results
        if (len(goodEarnings) == 0):
            percGoodEarningsPriceIncreaseOpen = 0
            percGoodEarningsPriceIncreasePreviousClose = 0
        else:
            percGoodEarningsPriceIncreaseOpen = len(goodEarningsPriceIncreaseFromOpen) / len(goodEarnings) * 100
            percGoodEarningsPriceIncreasePreviousClose = len(goodEarningsPriceIncreaseFromPastClose) / len(goodEarnings) * 100
        print("% of beat earnings where price increases from open:", str(percGoodEarningsPriceIncreaseOpen) + "%")
        print("% of beat earnings where price increases from previous close:", str(percGoodEarningsPriceIncreasePreviousClose) + "%")
        if (len(badEarnings) == 0):
            percBadEarningsPriceDecreaseOpen = 0
            percBadEarningsPriceDecreasePreviousClose = 0
        else:
            percBadEarningsPriceDecreaseOpen = len(badEarningsPriceDecreaseFromOpen) / len(badEarnings) * 100
            percBadEarningsPriceDecreasePreviousClose = len(badEarningsPriceDecreaseFromPastClose) / len(badEarnings) * 100
        print("% of missed earnings where price decreases from open:", str(percBadEarningsPriceDecreaseOpen) + "%")
        print("% of missed earnings where price decreases from previous close:", str(percBadEarningsPriceDecreasePreviousClose) + "%")

        print("\n\n")

        # Finds the likelihood of a stock’s price movement based on earnings results and stock trend
        if (len(goodEarningsUptrend) == 0):
            percGoodEarningsPriceIncreaseOpenUptrend = 0
            percGoodEarningsPriceIncreasePreviousCLoseUptrend = 0
        else:
            percGoodEarningsPriceIncreaseOpenUptrend = len(goodEarningsPriceIncreaseFromOpenUptrend) / len(goodEarningsUptrend) * 100
            percGoodEarningsPriceIncreasePreviousCLoseUptrend = len(goodEarningsPriceIncreaseFromPastCloseUptrend) / len(goodEarningsUptrend) * 100
        print("% of beat earnings where price increases from open and is in uptrend:", str(percGoodEarningsPriceIncreaseOpenUptrend) + "%")
        print("% of beat earnings where price increases from previous close and is in uptrend:", str(percGoodEarningsPriceIncreasePreviousCLoseUptrend) + "%")
        if (len(badEarningsDowntrend) == 0):
            percBadEarningsPriceDecreaseOpenDowntrend = 0
            percBadEarningsPriceDecreasePreviousCloseDowntrend = 0
        else:
            percBadEarningsPriceDecreaseOpenDowntrend = len(badEarningsPriceDecreaseFromOpenDowntrend) / len(badEarningsDowntrend) * 100 
            percBadEarningsPriceDecreasePreviousCloseDowntrend = len(badEarningsPriceDecreaseFromPastCloseDowntrend) / len(badEarningsDowntrend) * 100
        print("% of missed earnings where price decreases from open and is in downtrend:", str(percBadEarningsPriceDecreaseOpenDowntrend) + "%")
        print("% of missed earnings where price decreases from previous close and is in downtrend:", str(percBadEarningsPriceDecreasePreviousCloseDowntrend) + "%")
        '''


    # TOTAL CALC TOTAL CALC TOTAL CALC TOTAL CALC TOTAL CALC TOTAL CALC TOTAL CALC TOTAL CALC TOTAL CALC TOTAL CALC 
    print("\n\n")
    print("Total Data Points Evaluated:", totaldataPieces)
    print("Total Good Earnings:", totalgoodEarnings)
    print("Total Bad Earnings:", totalbadEarnings)
    
    # checks all to make sure there is no /0 error
    # Finds the likelihood of a company beating earnings solely on what the trend of the stock is doing.
    if (totalinUptrend == 0):
        percGoodEarningsUptrend = 0
    else:
        percGoodEarningsUptrend = totalgoodEarningsUptrend / totalinUptrend * 100
    print("% of beat earnings while stock is in an uptrend:", str(percGoodEarningsUptrend) + "%")
    if (totalinDowntrend == 0):
        percBadEarningsDowntrend = 0
    else:
        percBadEarningsDowntrend = totalbadEarningsDowntrend / totalinDowntrend * 100
    print("% of missed earnings while stock is in a downtrend:", str(percBadEarningsDowntrend) + "%")

    print("\n\n")

    # Finds the likelihood of a stock’s price movement based on earnings results
    if (totalgoodEarnings == 0):
        percGoodEarningsPriceIncreaseOpen = 0
        percGoodEarningsPriceIncreasePreviousClose = 0
    else:
        percGoodEarningsPriceIncreaseOpen = totalgoodEarningsPriceIncreaseFromOpen / totalgoodEarnings * 100
        percGoodEarningsPriceIncreasePreviousClose = totalgoodEarningsPriceIncreaseFromPastClose / totalgoodEarnings * 100
    print("% of beat earnings where price increases from open:", str(percGoodEarningsPriceIncreaseOpen) + "%")
    print("% of beat earnings where price increases from previous close:", str(percGoodEarningsPriceIncreasePreviousClose) + "%")
    if (totalbadEarnings == 0):
        percBadEarningsPriceDecreaseOpen = 0
        percBadEarningsPriceDecreasePreviousClose = 0
    else:
        percBadEarningsPriceDecreaseOpen = totalbadEarningsPriceDecreaseFromOpen / totalbadEarnings * 100
        percBadEarningsPriceDecreasePreviousClose = totalbadEarningsPriceDecreaseFromPastClose / totalbadEarnings * 100
    print("% of missed earnings where price decreases from open:", str(percBadEarningsPriceDecreaseOpen) + "%")
    print("% of missed earnings where price decreases from previous close:", str(percBadEarningsPriceDecreasePreviousClose) + "%")

    print("\n\n")

    # Finds the likelihood of a stock’s price movement based on earnings results and stock trend
    if (totalgoodEarningsUptrend == 0):
        percGoodEarningsPriceIncreaseOpenUptrend = 0
        percGoodEarningsPriceIncreasePreviousCLoseUptrend = 0
    else:
        percGoodEarningsPriceIncreaseOpenUptrend = totalgoodEarningsPriceIncreaseFromOpenUptrend / totalgoodEarningsUptrend * 100
        percGoodEarningsPriceIncreasePreviousCLoseUptrend = totalgoodEarningsPriceIncreaseFromPastCloseUptrend / totalgoodEarningsUptrend * 100
    print("% of beat earnings where price increases from open and is in uptrend:", str(percGoodEarningsPriceIncreaseOpenUptrend) + "%")
    print("% of beat earnings where price increases from previous close and is in uptrend:", str(percGoodEarningsPriceIncreasePreviousCLoseUptrend) + "%")
    if (totalbadEarningsDowntrend == 0):
        percBadEarningsPriceDecreaseOpenDowntrend = 0
        percBadEarningsPriceDecreasePreviousCloseDowntrend = 0
    else:
        percBadEarningsPriceDecreaseOpenDowntrend = totalbadEarningsPriceDecreaseFromOpenDowntrend / totalbadEarningsDowntrend * 100 
        percBadEarningsPriceDecreasePreviousCloseDowntrend = totalbadEarningsPriceDecreaseFromPastCloseDowntrend / totalbadEarningsDowntrend * 100
    print("% of missed earnings where price decreases from open and is in downtrend:", str(percBadEarningsPriceDecreaseOpenDowntrend) + "%")
    print("% of missed earnings where price decreases from previous close and is in downtrend:", str(percBadEarningsPriceDecreasePreviousCloseDowntrend) + "%")

    endTime = datetime.datetime.now()

    totalTime = endTime - startTime
    print("Time to completion:", totalTime.seconds)



    