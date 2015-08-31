__author__ = 'vishnu'

import datetime
import numpy as np
import pandas as pd



from pandas.io.data import DataReader
from sklearn.linear_model import LogisticRegression
from sklearn.lda import LDA
from sklearn.qda import QDA

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt



def create_lagged_series(symbol, start_date, end_date, lags=5):
    """
    This create a pandas DataFrame that stores the percentage return of adjusted closing value
    of a stock obtained from yahoo finance , along with a number of lagged returns from prior trading
    days (this defaults to Trading Volume , as well as Direction from previous day, are also.

    """

    # Obtain Stock information from yahoo finance
    #ts = pd.read_csv("BSE.csv", index_col="Date", parse_dates=True)
    ts = DataReader(symbol, "yahoo", start_date-datetime.timedelta(days=365), end_date)






    # Write that into a file
    """file = open("stock.txt", "w")
    file.write(str(ts))
    file.close()
    """
    # Logging the fetched data
    print " Stock Information : "
    print ts
    print "\n\n"

    # Create the new Lagged Dataframe
    tslag = pd.DataFrame(index=ts.index)


    tslag['Today'] = ts["Adj Close"]
    tslag['Volume'] = ts["Volume"]


    # Create the shifted lag series of prior trading period Close values
    for i in xrange(0, lags):
        tslag["Lag%s"%str(i+1)] = ts["Adj Close"].shift(i+1)


    # Print Outcome of Lagged DataFrame
    print " Lagged Dataframe : "
    print tslag
    print "\n\n"


    # Create the returns DataFrame
    tsret = pd.DataFrame(index=tslag.index)
    tsret['Volume'] = tslag["Volume"]
    tsret["Today"] = tslag["Today"].pct_change()*100.0


    # if any of the values of percentage return equals zero
    # set them to a small number (stops issue with QDA model in sckit-learn)
    for i ,x in enumerate(tsret['Today']):
        if (abs(x) < 0.0001):
            tsret["Today"][i] = 0.0001


    # Create the lagged percentage return columns
    for i in xrange(0, lags):
        tsret['Lag%s'%str(i+1)] = tslag["Lag%s"%str(i+1)].pct_change() * 100.0


    # Create the "Direction" column (+1 or -1) indicating an up/down day
    tsret["Direction"] = np.sign(tsret["Today"])

    print "Tsret Value at the end :"
    print tsret
    tsret = tsret[tsret.index >= start_date]

    return tsret

def fit_model(name, model, X_train, y_train, X_test,  pred):
    """
    Fits a classification model (for our purpose this LR, LDA , QDA)
    using the training data, then makes a prediction and subsequent
    for the test data.

    """

    # fit and model predict the model on the training , and then test , data
    model.fit(X_train, y_train)
    pred[name] = model.predict(X_test)

    print "Printing Graph   : "
    x = [ mdates.date2num(d) for d in pred.index ]
    plt.plot_date(x=x, y=pred['Actual'], fmt="ro")
    plt.grid(True)
    plt.show()

    print "Prediction Matrix"
    print pred

    plt.show()

    # and then calculate the hit rare based on the actual direction
    pred["%s_Correct"%name] = (1.0+pred[name]*pred["Actual"])/2.0
    hit_rate = np.mean(pred["%s_Correct" % name])
    print "%s: %3.f"%(name, hit_rate)






if __name__ == "__main__" :

    snpret = create_lagged_series("^GSPC", datetime.datetime(2001, 1, 10), datetime.datetime(2005, 12, 13),
                                  lags=5)

    # Use the prior two days of return as predictor values , with direction as response
    X = snpret[["Lag1", "Lag3"]]
    y = snpret["Direction"]


    # The test data is split into two parts: Before and after 1st jan 2005
    start_test = datetime.datetime(2005, 1, 1)

    # Create training and test sets
    X_train = X[X.index < start_test]
    X_test = X[X.index >= start_test]
    y_train = y[y.index < start_test]
    y_test = y[y.index >= start_test]


    # Create prediction DataFrame
    pred = pd.DataFrame(index=y_test.index)
    pred["Actual"] = y_test


    # Create and fit the three models
    print "Hit Rates: "
    models = [("QDA", QDA())]

    for m in models:
        fit_model(m[0], m[1], X_train, y_train, X_test, pred)







