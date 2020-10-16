from bs4 import BeautifulSoup as BS
res=requests.get('https://www.ccrecorder.org/recordings/get_docs_by_pin/16093170020000/', 'html5lib', verify=False)
page=res.text
def to_dict(page):
 soup=BS(page,'html5lib')
 rows=soup.select('#docs_body > tr')                                                   
 def extract_row(dd): 
       date=dd.select('td:nth-child(2)')[0].text  
       docno=dd.select('td:nth-child(3)')[0].text  
       doctype=dd.select('td:nth-child(4)')[0].text   
       parties=[i.text for i in dd.select('#docs1_body td')]      
       prior_docs=[i.text for i in dd.select('#docs3_body td')]  
       partial_dic={'Date_Recorded':date,'Doc_Num':docno,'Doc_Type':doctype} 
       parties={'Parties':[{parties[i]:parties[i+1]} for i in range(0,len(parties),2)]} 
       priors={'Prior_Docs':[{'Doc-Num':doc} for doc in prior_docs]}  
       out_dict={**partial_dic, **parties, **priors} 
       return out_dict 
 docs_recorded=[extract_row(i) for i in rows] 
 return docs_recorded





def to_dict(page):
 soup=BS(page,'html5lib')
 rows=soup.select('#docs_body > tr') 
 def datef(ymd): 
      date=dateparser.parse(ymd).date()  
      year=date.year  
      if date.year <= 2016:  
         date=date.strftime("%m")  
      else:  
         date=date.strftime("%Y%m%d")  
      return date 
 def extract_row(dd): 
     ymd=dd.select('td:nth-child(2)')[0].text 
     year=ymd[:4] 
     date=datef(ymd)        
     docno=dd.select('td:nth-child(3)')[0].text  
     doctype=dd.select('td:nth-child(4)')[0].text   
     parties=[i.text for i in dd.select('#docs1_body td')]      
     prior_docs=[i.text for i in dd.select('#docs3_body td')]  
     partial_dic={'Date_Recorded':ymd,'Doc_Num':docno,'Doc_Type':doctype} 
     parties={'Parties':[{'Name':parties[i],'Party_Type': parties[i+1]} for i in range(0,len(parties),2)]}                                                                                
     priors={'Prior_Docs':[{'Doc_Num':doc} for doc in prior_docs]}  
     base='https://www.ccrecorder.org/CCRD-WM/'  
     url={'Doc_Url':'{}{}/{}wm/{}.pdf'.format(base,year,date,docno)}  
     out_dict={**partial_dic, **parties, **priors, **url}  
     return out_dict
 docs_recorded=[extract_row(i) for i in rows] 
 return docs_recorded