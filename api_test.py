#! /usr/bin/env python
#
# @brief XCoin API-call sample script (for Python 2.x, 3.x)
#
# @author btckorea
# @date 2017-04-14
#
# @details
# First, Build and install pycurl with the following commands::
# (if necessary, become root)
#
# https://pypi.python.org/pypi/pycurl/7.43.0#downloads
#
# tar xvfz pycurl-7.43.0.tar.gz
# cd pycurl-7.43.0
# python setup.py --libcurl-dll=libcurl.so install
# python setup.py --with-openssl install
# python setup.py install
#
# @note
# Make sure current system time is correct.
# If current system time is not correct, API request will not be processed normally.
#
# rdate -s time.nist.gov
#

import sys
from xcoin_api_client import *
import xcoin_api_security as xapi_secu
import pprint



#api_key = ""
#api_secret = ""

api_key,api_secret = xapi_secu.getKey("C:\Users\dongwkim\CryptoSalon\Key\keys.csv")

# Declare Curl Session for pooling, 3X faster than original version
'''
Elapsed: 0.618000030518
Elapsed: 0.223999977112
Elapsed: 0.190999984741
Elapsed: 0.210999965668
Elapsed: 0.1890001297
'''

curl_handle = pycurl.Curl();
api = XCoinAPI(api_key, api_secret, curl_handle);

#Original api
#api = XCoinAPI(api_key, api_secret);

rgParams = {
	"order_currency" : "BTC",
	"payment_currency" : "KRW"
};


#
# Public API
#
# /public/ticker
# /public/recent_ticker
# /public/orderbook
# /public/recent_transactions


start = time.time();
#print("Bithumb Public API URI('/public/ticker') Request...");
result = api.xcoinApiCall("/public/ticker", rgParams);
#print("- Status Code: " + result["status"]);
#print("- Opening Price: " + result["data"]["opening_price"]);
#print("- Closing Price: " + result["data"]["closing_price"]);
#print("- Sell Price: " + result["data"]["sell_price"]);
#print("- Buy Price: " + result["data"]["buy_price"]);
#print("");
end = time.time();
elased = float(end - start)
print("Elapsed: {}").format(elased)


#
# Private API
#
# endpoint => parameters
# /info/current
# /info/account
# /info/balance
# /info/wallet_address

#print("Bithumb Private API URI('/info/account') Request...");
#result = api.xcoinApiCall("/info/account", rgParams);
#print("- Status Code: " + result["status"]);
#print("- Created: " + result["data"]["created"]);
#print("- Account ID: " + result["data"]["account_id"]);
#print("- Trade Fee: " + result["data"]["trade_fee"]);
#print("- Balance: " + result["data"]["balance"]);

sys.exit(0);
