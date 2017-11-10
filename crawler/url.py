# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 11:02:22 2017

@author: caibo
"""

import urllib.request
def getpagesource(url):
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "cookie":"",
        "Referer":"",
    }
    response=urllib.request.Request(url,headers=headers)
    pagesource=urllib.request.urlopen(response).read().decode("utf8")
    return pagesource
if __name__=="__main__":
    s=input()
    pagesource=getpagesource("https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=86c5e41600007bdd&ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=12&tn=98012088_5_dg&wd="+str(s)+"&oq="+str(s)+"&rsv_pq=86c5e41600007bdd&rsv_t=d9d53xaIG%2B42cHbP3Io%2FUh5qzxnyOj75CU%2BBb8U0OV2F%2BJ1%2B2OKpKS%2BZ0326FF4r5v3VUA&rqlang=cn&rsv_enter=0&bs="+str(s)+"&rsv_sid=1456_19036_21087_24880&_ss=1&clist=&hsug=&f4s=1&csor=3&_cr1=25072")
    print(pagesource)