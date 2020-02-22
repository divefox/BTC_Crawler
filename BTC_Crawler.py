import re
import requests
# import urllib
from selenium import webdriver
import cmath
import time
import xlwt
import random
import tushare as ts
import talib as ta
import numpy as np
import pandas as pd
# url = 'https://a.aicoin.cn/matomo.php?e_c=%2Fsymbols%2Fethbtc%3Aokex&e_a=setSubIndicators%3ABRAR&e_n=setSubIndicators&idsite=2&rec=1&r=266751&h=0&m=51&s=31&url=https%3A%2F%2Fwww.aicoin.cn%2Fchart%2Fokex_ethbtc&urlref=https%3A%2F%2Fwww.aicoin.cn%2F&_id=c655d421ff7cf409&_idts=1572534468&_idvc=9&_idn=0&_refts=0&_viewts=1575736989&send_image=1&cookie=1&res=1024x1366&gt_ms=168&pv_id=0cw27F'
# headers={
#     'Host': 'a.aicoin.cn',
#     'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
#     'Referer':'https://www.aicoin.cn/chart/binance_ethbtc',
#     'Cookie':'_ga=GA1.2.1028438516.1572534468; XSRF-TOKEN=eyJpdiI6IkdEa2tOYUtLVUJNb3RQd3ZwUVg4MHc9PSIsInZhbHVlIjoielBMRk9Cb2NqRHRZYVdXMTE2bURFRWJBakJ5dloyXC8zR1prRlp1YndOK25SU01IM0ZVKzdTa2UybkVRVDFJQ2dLSlJFeUtcL2syNFp1eFh4OHhUanpIZz09IiwibWFjIjoiOGZlOTNmMTQ3OWZhZWIzZmIyZjdlY2RiNjhhNWZjNGRjYWJmMjI3ZTUzYzc5NDVjYmM5MzIwNWMyYTdiOWM5OCJ9; _gid=GA1.2.1434410357.1575736989; aicoin_session=eyJpdiI6Imoxa2d1dlZWZ0kwKzl3VVY1TGk3Nnc9PSIsInZhbHVlIjoibFhBU1VQME41U1lxNVpNTkdTZ0NWdVN3N2JSZ211d0RhN2k2ZVwva3pyVTQwNWxwT21hZmZUN2dEajA5QThZbFJBcjRZNys2KzVxdkxmb0lPU1d3Z293PT0iLCJtYWMiOiIzNGNhZmZjYmIxYjZlNmUwMzIwNDlmNDVmYzE4ZTQwMTljZTM0Y2QzMGJiNjg1YWMzOWFhODkyMDNhYjVkZWU3In0%3D',
#     'X-Requested-With':'XMLHttpRequest',
#     # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
# }
# , headers=headers
# res = requests.get(url=url)
# res = urllib.request.urlopen(req)
# html = res.read()
# .decode()
# res.encoding = res.apparent_encoding
# print (res.apparent_encoding)
# print (res.status_code)
# print (res.text)



#设置url
# url = '''https://www.aicoin.cn/api/chart/kline/data/period'''
# # 获取响应
# response = requests.post(url,headers=headers,data=data)
# res=response.json()



# print (res)
# print(res['data']['kline_data'][496])
# print(res['data']['kline_data'][497])
# print(res['data']['kline_data'][498])
# print(res['data']['kline_data'][499])
#
#
# lastTwo=res['data']['kline_data'][498]
# lastThree=res['data']['kline_data'][497]

# data=res['data']['kline_data']

def main():
    okex_path="okex.txt"
    binance_path="币安.txt"
    huobi_path="火币.txt"

    okex_reader = open(okex_path, encoding='utf-8')
    okex_data = okex_reader.readlines()
    okex_data = okex_data[0:5]
    binance_reader=open(binance_path,encoding='utf-8')
    binance_data=binance_reader.readlines()

    huobi_reader=open(huobi_path,encoding='utf-8')
    huobi_data=huobi_reader.readlines()
    # print (okex_data)

    symbol=[]

    # 在中间加入下划线
    for i in range(len(okex_data)):
        temp=okex_data[i][0:32]+'_'+okex_data[i][32:]
        okex_data[i]=temp
        # print (okex_data[i])
        okex_data[i]= okex_data[i].replace("\n","")
        symbol_temp = str(okex_data[i][33:])+":okex"
        symbol.append(symbol_temp)
        # print (symbol_temp)
    #
    for i in range(len(binance_data)):
        temp=binance_data[i][0:35]+'_'+binance_data[i][35:]
        binance_data[i]=temp
        binance_data[i]=binance_data[i].replace("\n","")
        symbol_temp = str(binance_data[i][36:])+":binance"
        symbol.append(symbol_temp)
        # print (binance_data[i])

    for i in range(len(huobi_data)):
        temp = huobi_data[i][0:36]+'_'+huobi_data[i][36:]
        huobi_data[i] = temp
        huobi_data[i] = huobi_data[i].replace("\n","")
        symbol_temp = str(huobi_data[i][37:]+":huobipro")
        symbol.append(symbol_temp)
        # print (huobi_data[i])

    # print (symbol)
    referer=okex_data
    referer+=binance_data
    referer+=huobi_data

    # print (referer[2])
    # symbol=['ethbtc:okex','btcquarter:okcoinfutures']
    # referer=['https://www.aicoin.cn/chart/okex_ethbtc','https://www.aicoin.cn/chart/okcoinfutures_btcquarter']
    period=[1440,10080]
    #
    requestData = {
        'symbol': 'ethbtc:okex',
        'period': '720',
        'open_time': '24',
        'type': '1'
    }
    headers = {
        'Host': 'www.aicoin.cn',
        'Referer': 'https://www.aicoin.cn/chart/binance_ethbtc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'HWWAFSESID=8d50c82122d3821ec9; HWWAFSESTIME=1573278977994; _pk_testcookie..undefined=1; _pk_testcookie.2.57ea=1; Hm_lvt_3c606e4c5bc6e9ff490f59ae4106beb4=1573278983; _ga=GA1.2.1081593487.1573278984; _gid=GA1.2.577820120.1573278984; _pk_id.2.57ea=8c87cf6d15aeea90.1573278983.1.1573279030.1573278983.; Hm_lpvt_3c606e4c5bc6e9ff490f59ae4106beb4=1573279030; aicoin_session=eyJpdiI6ImdkR0NRbHZicXNsNW43aE16bjVGRFE9PSIsInZhbHVlIjoiMFRiNGhObGFXY0VqRkR4K2REV2RMT1ZZZzZkSzg4N0czT0RIeVdaaWFGRHQwSytOODJ1UVBTTndJK1V4bitPWkUxblp0TnJuTkxcL1wvT1wvamNRZmlITUE9PSIsIm1hYyI6IjlkYTYyOTIwZWU5N2M5YTE4YmEwZGM0NDVmNDgwY2M5ODYzZjkxNmM4ZmQwMWE1Mjc2ZGU3NmQ0YzI2ODNhNzcifQ%3D%3D'
        # 需要登陆后捕获cookie并调用
    }
    periodName=['1日','1周']
    #
    todayTime=time.strftime('%Y-%m-%d', time.localtime(time.time()))
    dataToExcel = []
    for j in range(len(symbol)):
        for i in range(len(period)):
            dataTemp=[]
            dataTemp.append(todayTime)
            dataTemp.append(periodName[i])
            dataTemp.append(symbol[j])

            requestData['period'] = period[i]
            requestData['symbol'] = symbol[j]
            headers['Referer'] = referer[j]
            url = '''https://www.aicoin.cn/api/chart/kline/data/period'''
            time.sleep(random.random() * 3)
            # 获取响应
            try:
                response = requests.post(url, headers=headers, data=requestData)
                res = response.json()
            except Exception:
                print ("error")
                # print (requestData['symbol'])
                # print (headers['Referer'])
            else:
                data = res['data']['kline_data']
                # print (data)
                # print (type(data))
                # print ("--------------")
                data=np.array(data)
                # print (data[:,2])
                try:
                    dataHigh = pd.Series(data[:, 2])
                    dataLow = pd.Series(data[:, 3])
                    dataClose = pd.Series(data[:, 4])
                    # print (dataHigh)
                    CCI = ta.CCI(dataHigh, dataLow, dataClose, timeperiod=20)
                    # print (CCI[490:])
                    #
                    # print(len(data))
                    IndexSecondToLast = len(data) - 2
                    # if(i==3):
                    #     IndexSecondToLast=113
                    raiseRate = getRaiseRate(data, IndexSecondToLast)
                    dataTemp.append(raiseRate)
                    dataTemp.append(getVR(data, IndexSecondToLast))
                    dataTemp.append(getVR(data, IndexSecondToLast - 1))
                    VRRaiseRate = ((getVR(data, IndexSecondToLast) - getVR(data, IndexSecondToLast - 1)) / getVR(data,
                                                                                                                 IndexSecondToLast - 1)) * 100
                    dataTemp.append(VRRaiseRate)
                    # dataTemp.append(getCCI(data, IndexSecondToLast))
                    # dataTemp.append(getCCI(data, IndexSecondToLast - 1))
                    # CCIRaiseRate = getCCI(data, IndexSecondToLast) - getCCI(data, IndexSecondToLast - 1)
                    dataTemp.append(CCI[len(CCI) - 2])
                    dataTemp.append(CCI[len(CCI) - 3])
                    CCIRaiseRate = CCI[len(CCI) - 2] - CCI[len(CCI) - 3]
                    dataTemp.append(CCIRaiseRate)
                    print (dataTemp)
                    dataToExcel.append(dataTemp)
                except Exception:
                    print ("error")

    # print (dataToExcel)
#     导出数据到excel
    book=xlwt.Workbook(encoding='utf-8')
    sheet=book.add_sheet('alcoid')
    head=['时间','周期','币种','涨幅','VRY','VRX','VR涨跌幅','CCIA','CCIB','CCI涨跌幅']
    for h in range(len(head)):
        sheet.write(0, h, head[h])  # 写入表头
    i=1
    for list in dataToExcel:
        j=0
        for x in list:
            sheet.write(i,j,x)
            j=j+1
        i=i+1
    book.save('alcoidData.xls')





# 倒数第二根线的VR指标
# X=
def getRaiseRate(alldata,index):
    raizeRate = (alldata[index][4] - alldata[index-1][4]) /alldata[index-1][4]
    return raizeRate


def getTP(alldata,index):
    TP = (alldata[index][2] + alldata[index][3] + alldata[index][4]) / 3.0
    return TP

# 近20日累计收盘价均值
def getMA(alldata,index):
    sum=0
    for i in range(20):
        sum=sum+alldata[index-i][4]
    MA=sum/20
    # print ("----")
    # print (count)
    return MA

# 计算MD
def getMD(alldata,index):
    sum=0
    for i in range(20):
        # dev=abs(getMA(alldata,index-i)-getTP(alldata,index-i))
        dev = abs(getMA(alldata, index - i) - alldata[index-i][4])
        sum=sum+dev
    MD=sum/20.0
    return MD

def getAvgDev(alldata,index):
    tp_sum=0
    for i in range(20):
        tp_sum += getTP(alldata,index-i)
    tp_avg = tp_sum/20.0
    dev_sum = 0
    for i in range(20):
        diff = abs(tp_avg-getTP(alldata, index-i))
        dev_sum += diff*diff
    # print (dev_sum/20.0)
    return dev_sum/20.0


def getCCI(alldata,index):

    CCI=(getTP(alldata,index)-getMA(alldata,index))/(getAvgDev(alldata,index)*0.015)
    return CCI

def getVR(alldata,index):
    A=0
    B=0
    ping=0
    for i in range(26):
        if(getRaiseRate(alldata,index-i)<0):
            B = B + alldata[index-i][5]
        elif(getRaiseRate(alldata,index-i)>0):
            A = A + alldata[index - i][5]
        else:
            ping=alldata[index - i][5]
    A=A+0.5*ping
    B=B+0.5*ping
    VR=A/B*100
    return VR

# print (getRaiseRate(data,498))
# print (getTP(data,498))
# print (getMA(data,498))
# print (getCCI(data,498))
# print (getCCI(data,497))
# print (getCCI(data,496))
# print (getCCI(data,495))
# print (getCCI(data,494))
# print (getVR(data,498))
# print (getVR(data,497))
# print (getVR(data,496))

if __name__ == "__main__":
    main()