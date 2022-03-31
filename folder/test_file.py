import os
import requests
import json
 
model_ip = "nlp.p"
file = "grange_data/AllTrain - Copy.csv"
url = "http://127.0.0.1:8000/skense/text_Classification"
#result1 = requests.post('https://wns-mtro-dev-imgcnvrsnapi-fc.azurewebsites.net/skense/docToImage', data={​​​​"filename":"skense/"+file, "doc_id":100, "dec_id":2001}​​​​, files=dict(doc=file_byte))
result1 = requests.post(url, data={​​​​"model" : model_ip}​​​​, files ={​​​​'doc': open(file,'rb')}​​​​)  
 
print(result1.json())