from binance import client

#First get ETH price
eth_price = client.get_symbol_ticker(symbol="ETHUSDT")

#Calculate how much ETH $200 can buy
buy_quantity = round(200 / float(eth_price['price']))

#Create test order
order = client.create_test_order(
    symbol='ETHUSDT'
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=buy_quantity
)

#The 200 in buy_quantity is the amount of money you want to spend on ETH.