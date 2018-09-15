import json, urllib2, time, datetime, requests
import poloniex, bittrex, bitstamp.client
import socket 


API_KEYS = {'TREX': {'public': '',
					 'private': ''}}

trex = bittrex.Bittrex(API_KEYS['TREX']['public'], API_KEYS['TREX']['private'])

orders = trex.get_open_orders(market=None)

for order in orders['result']:
	market = order['Exchange']
	otype = order['OrderType']
	price = order['Limit']
	amount = order['Quantity']

	print "Refreshing order %s %s @ %s for %s" % (market, otype, price, amount)

	trex.cancel(order['OrderUuid'])

	if otype == 'LIMIT_BUY':
		refreshed_order = trex.buy_limit(market, amount, price)

	elif otype == 'LIMIT_SELL':
		refreshed_order = trex.sell_limit(market, amount, price)

	time.sleep(2)

	print "Done."