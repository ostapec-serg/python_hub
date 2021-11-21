#Write a script to concatenate following dictionaries to create a new one.
#Exchange Rates. Currency-UAH

exchange_1 = {'EUR':29.7, 'USD':26.4}
exchange_2 = {'GPB':34.7, 'RUB':0.3}
exchange_3 = {'AUD':19.2, 'CZK':1.1}

exRates = dict(list(exchange_1.items())+
               list(exchange_2.items())+
               list(exchange_3.items()))
print(exRates)
