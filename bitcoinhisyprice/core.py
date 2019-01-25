#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bitcoinhisyprice.client import ApiClient
from bs4 import BeautifulSoup as bs
import datetime

class CoinMarketCap(object):

    __CMC_HISTORY_DATA_URL = u'https://coinmarketcap.com/currencies/bitcoin/historical-data/'
    __DEFAULT_REQUEST_TIMEOUT = 60  # seconds
    __DEFAULT_ENABLE_CACHE = True
    __DEFAULT_CACHE_FILENAME = u'coinmarketcap.cache'
    __DEFAULT_CACHE_EXPIRE_AFTER = 60  # seconds

    def __init__(self, enable_cache=__DEFAULT_ENABLE_CACHE, request_timeout=__DEFAULT_REQUEST_TIMEOUT,
                 cache_expire_after=__DEFAULT_CACHE_EXPIRE_AFTER, cache_filename=__DEFAULT_CACHE_FILENAME):
        self.client = ApiClient(request_timeout, enable_cache, cache_filename, cache_expire_after)



    def coin_price(self,**kwargs):
        """
        get currency price info from <start> to <end>

        GET /currencies/<currency>/<start>/<end>/
        GET /currencies/<currency>/

        Optional parameters:
            (int) start - return results starting from the specified timestamp
            (int) end - return results ending with the specified timestamp

        :param currency: 货币名称 必须是字符串
        :param disable_cache: 禁用缓存
        :param start: 开始时间timestamp
        :param end: 结束时间timestamp
        :return:
        """
        params={}
        params.update(kwargs)
        response = self.client.request(self.__CMC_HISTORY_DATA_URL, params, False)
        historyprice=[]
        soup=bs(response, u'html.parser')
        tables=soup.findChildren('table',{'class':'table'})
        historytable=tables[0]
        aAllRows = historytable.findChildren('tr')
        for aOneRow in aAllRows:
            aAllCells = aOneRow.findChildren('td')
            if len(aAllCells)<7:
                continue
            aOneDayPrice={
                'Date': None,
                'Open':0,
                'High':0,
                'Low':0,
                'Close': 0,
                'Volumn': 0,
                'MarketCap': 0
            }
            datestring=aAllCells[0].text
            date=datetime.datetime.strptime(datestring,"%b %d, %Y")
            aOneDayPrice['Date']=str(date)[0:10]
            aOneDayPrice['Open']=aAllCells[1].text
            aOneDayPrice['High'] = aAllCells[2].text
            aOneDayPrice['Low'] = aAllCells[3].text
            aOneDayPrice['Close'] = aAllCells[4].text
            aOneDayPrice['Volumn'] = aAllCells[5].text
            aOneDayPrice['MarketCap'] = aAllCells[6].text
            historyprice.append(aOneDayPrice)
        return historyprice







if __name__=="__main__":
    cap=CoinMarketCap()
    pricetable=cap.coin_price(start=20180101,end=20181231)

    fp = open("/home/chauncey/vendors/historyprice.json", 'w')
    json.dump(pricetable, fp)
    fp.close()



