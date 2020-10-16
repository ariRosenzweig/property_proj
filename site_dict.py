import requests
from dataclasses import dataclass

@dataclass
class Dtax:
 headers: dict
 data: dict
 url: str = 'https://taxdelinquent.cookcountyclerkil.gov/'
 def get_url(self, pin):
   self.data['Pin']=pin
   resp=requests.post(self.url, headers=self.headers, data=self.data)
   return resp
   
headers = {
    'authority': 'taxdelinquent.cookcountyclerkil.gov',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://taxdelinquent.cookcountyclerkil.gov',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://taxdelinquent.cookcountyclerkil.gov/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d19c0aa08e7f689c5c531034f20a149b01599085401; __RequestVerificationToken=Fmt01uPU7ISP_j8bxtCVoZZmxEBMOypCEtPYKTBVAWtkk7oAaqZlyafn7xQFOMUMEGQMDvdijktqxxUI0UifNla8Atuk6lXTGqFQBhOkMcM1; AWSALB=V96DCQ3Rxf5b4EZI6LAZZcnMkKcyPEwZ/r+8e6jLltTd/LZaYB69/zFApAJ4xTnp85IK8pcqh88g0nxzDzh5xMvyu910vtZJD3RWfILKcnnUIpLWT6Ne6mCMft7R; AWSALBCORS=V96DCQ3Rxf5b4EZI6LAZZcnMkKcyPEwZ/r+8e6jLltTd/LZaYB69/zFApAJ4xTnp85IK8pcqh88g0nxzDzh5xMvyu910vtZJD3RWfILKcnnUIpLWT6Ne6mCMft7R',
    'dnt': '1',
}

data = {
  '__RequestVerificationToken': '0oInWjqjFORsA13Av6JK1HKSZkBha7MdUyqdqT0eUwiD-8QvzIC59V51ksOGuwmx6eK4n0KQm_XeV5z72xmsj_zrdlZMtK_A2vwx89iPUAY1',
  'Pin': '13-28-304-034-0000'
}
@dataclass
class Recorder:
 url: str = 'https://ccrecorder.org/'
 def get_url(self, pin):
    p=pin.replace('-','')
    url='{}recordings/get_docs_by_pin/{}'.format(self.url,p)
    g=requests.get(url, verify=False)
    return g


@dataclass
class Assesor:
 resp: str = ''
 url: str ='https://www.cookcountyassessor.com/'
 def get_url(self, pin):
    p=pin.replace('-','')
    url='{}pin/{}'.format(self.url,p)
    g=requests.get(url, verify=False)
    self.resp=g
    return self.resp
 


"""@dataclass
class Portal:
  
@dataclass
class Clerk:

@dataclass
class Treasurer:"""

