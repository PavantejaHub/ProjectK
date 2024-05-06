import urllib
from flask import Flask
import requests


Stock_P = Flask(__name__)
getstockurl = "/stock/querystock"

@Stock_P.route(getstockurl)
def getstockdetails():
    stock_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=4SS3NYNAEPLEZCQ7"
    response = requests.get(stock_url)
    data = response.json()
    return data


if __name__ == "__main__":
    Stock_P.run(host="0.0.0.0", port=8081, debug=True)

