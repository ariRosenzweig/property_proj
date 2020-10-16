def make_dict(table, cols): 
         keys_temp=[i.text.replace('?','').replace('-','').strip() for i in table.select('th')]
         keys=[' '.join(i.split()).replace(' ','_') for i in keys_temp] 
         vals=[i.text.strip().replace('\n','') for i in table.select('tr td')]
         rows=[vals[i:i+cols] for i in range(0,len(vals),cols)] 
         data=[dict(zip(keys, i)) for i in rows ] 
         return data 

def convert_soup(soup):
 num_tables=soup.select('table') 
 if len(num_tables) > 1: 
         sold=num_tables[0] 
         sold_dict=make_dict(sold,6) 
         deli=num_tables[1] 
         deli_dict=make_dict(deli,7)
         total=list(deli_dict[-1].values())
         tots={'Totals':{'1st_Installment_Total':total[2], '2nd_Installment_Total':total[3]}}
         deli_dict={'Delinquent_Amounts':deli_dict[:5]}
	 deli_dict.update(tots)              
         dtax={'Taxes_Sold':sold_dict}
	 dtax.update(deli_dict)
 else: 
         if len(num_tables) == 1: 
          sold=num_tables[0] 
          sold_dict=make_dict(sold,6) 
          dtax={'Taxes_Sold':sold_dict}
         else: 
          dtax={'message':'error'} 
 return dtax
	 