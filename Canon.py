
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import csv
import re
import json
from os import path
import urllib3
from collections import OrderedDict
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
import datetime
from time import gmtime, strftime
import time
allz=[]
dic={}
import pandas as pd
import html5lib
def fuv(teph):
    from bs4 import BeautifulSoup
    import requests
    import csv
    import re
    from os import path
    import urllib3
    import time
    from collections import OrderedDict
    def replace_all(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text
    ph2=str(teph).split('/')
    po=str(ph2).split('|')
    ph23=str(po).split(';')
    ph3=str(ph23).split(',')
    pi=[]
    mi=[]
    sc=[]
    tf=[]
    std=" "
    for i in range(len(ph3)):
        ph41=str(ph3[i]).split('-')
        try:
            od = OrderedDict([('[',''),(']',''),('\"',''),('\'',''),('/',''),('\\',''),('xa0',''),(' ','')])
            ph190=replace_all(str(ph41),od)
            ph112=ph190.split(',')
            if len(ph112)==2:
                std=ph112[0]
                sc.append(std)
                pi.append(ph112[1])
            elif len(ph112)==3:
                uij=ph112[0]+"-"+ph112[1]+"/"+ph112[2]
                std,pi,mi,tf=fuv(uij)
            else:
                ph19=ph190
                if len(ph19)==11:

                    if ph19[0]=="1":
                        print(ph19[0])
                        tf.append(ph19)
                    else:
                        ph1=ph19[1:11]
                        if ((ph1[0]=="9") or (ph1[0]=="8") or (ph1[0]=="7")):
                            mi.append(ph1)
                        elif (ph1[0]=="6"):
                            urll="https://fonnambar.info/in-number/0"+str(ph1)
                            head={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'Connection': 'keep-alive',
                            'Referer': 'https://fonnambar.info/in-number/08832429500',
                            'Upgrade-Insecure-Requests': '1'}
                            rew=requests.get(urll,headers=head)
                            sou=BeautifulSoup(rew.text,'html.parser')
                            s1=sou.find(attrs={'class':'col-xs-12 maininfo'})
                            s2=s1.find(attrs={'style':'text-align: center;'}).text
                            if s2=="प्रकार: लैंडलाइन और आईडीडी लाइन टेलीफोन के लिए नंबर।":
                                mob=" "
                                pi.append(ph1)
                            else:
                                mi.append(ph1)
                        elif len(ph1)==10:
                            pi.append(ph1)
                        else:
                            pi.append(ph1)
                elif len(ph19)==10:
                    ph1=ph19
                    if ((ph1[0]=="9") or (ph1[0]=="8") or (ph1[0]=="7")):
                        mi.append(ph1)
                    elif (ph1[0]=="6"):
                        urll="https://fonnambar.info/in-number/0"+str(ph1)
                        head={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Connection': 'keep-alive',
                        'Referer': 'https://fonnambar.info/in-number/08832429500',
                        'Upgrade-Insecure-Requests': '1'}
                        rew=requests.get(urll,headers=head)
                        sou=BeautifulSoup(rew.text,'html.parser')
                        s1=sou.find(attrs={'class':'col-xs-12 maininfo'})
                        s2=s1.find(attrs={'style':'text-align: center;'}).text
                        if s2=="प्रकार: लैंडलाइन और आईडीडी लाइन टेलीफोन के लिए नंबर।":
                            mob=" "
                            pi.append(ph1[4:])
                            std=ph1[0:4]
                        else:
                            mi.append(ph1)
                    elif len(ph1)==10:
                        pi.append(ph1[4:])
                        std=ph1[0:4]
                    else:
                        pi.append(ph1)
                else:
                    ph1=ph19
                    pi.append(ph1)
        except:
            std=" "
            pi.append('no')
            mi.append('no')
    if len(sc)>=1:
        std=sc[0]
        return std,pi,mi,tf

    else:
        return std,pi,mi,tf
url="https://edge.canon.co.in/all_products_serviced"
responce=requests.get(url)
soup=responce.json()
al=soup['data']
for cl in al:
    prod=cl
    print(prod)
    url5="https://edge.canon.co.in/service-networks-by-filters?product="+str(prod)+"&state=&city="
    responce5=requests.get(url5)
    soup5=responce5.json()
    soup6=soup5['data'] 
    for soup7 in soup6:
        try:
            nam=soup7['service_center_name']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Tile Size:',''),('Tile Size',''),(':','')])
            name=replace_all(str(nam),od)
            print(name)
        except:
            name=""
        try:
            add=soup7['address']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Tile Size:',''),('Tile Size',''),(':','')])
            address=replace_all(str(add),od)
            print(address)
        except:
            address=""
        try:
            cod=soup7['state']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Email',''),('Tile Size',''),(':',''),('  ','')])
            state=replace_all(str(cod),od)
            print(state)
        except:
            state=""
        try:
            cod=soup7['city']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Email',''),('Tile Size',''),(':',''),('  ','')])
            city=replace_all(str(cod),od)
            print(city)
        except:
            city=""
        try:
            cod=soup7['zipcode']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Postal Code',''),('Tile Size',''),(':',''),('  ','')])
            pincode=replace_all(str(cod),od)
            print(pincode)
        except:
            pincode=""
        try:
            cod=soup7['email']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Email',''),('Tile Size',''),(':',''),('  ','')])
            email=replace_all(str(cod),od)
            print(email)
        except:
            email=""
        try:
            cod=soup7['latitude']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Email',''),('Tile Size',''),(':',''),('  ','')])
            lati=replace_all(str(cod),od)
            print(lati)
        except:
            lati=""
        try:
            cod=soup7['longitude']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Email',''),('Tile Size',''),(':',''),('  ','')])
            long=replace_all(str(cod),od)
            print(long)
        except:
            long=""
        try:
            nam=soup7['contact_person']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('NULL',''),('Tile Size',''),(':','')])
            dname=replace_all(str(nam),od)
            print(dname)
        except:
            dname=""
        try:
            nam=soup7['mobile']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('NULL',''),('null',''),('None',''),(':','')])
            mobiled=replace_all(str(nam),od)
            print(mobiled)
        except:
            mobiled=""
        try:
            nam=soup7['phone']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('NULL',''),('null',''),('None',''),(':','')])
            phoneddd=replace_all(str(nam),od)
            print(phoneddd)
        except:
            phoneddd=""
        try:
            nam=soup7['dealer_category']
            od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('NULL',''),('Tile Size',''),(':','')])
            cat=replace_all(str(nam),od)
            print(cat)
        except:
            cat=""
        try:
            if mobiled==phoneddd:
                phone=""
                std_code,teliphone,mobile,tollfree=fuv(phone)
            else:
                cod=mobiled+"/"+phoneddd
                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Telephone',''),('Tile Size',''),(':',''),('  ',''),('</b>',' '),('<br/>','/'),('</div>',''),('\\xa0','')])
                cod1=replace_all(str(cod),od)
                od = OrderedDict([('\n',' '),('\r',' '),('\t',' '),('Mobile',''),('~',''),('>',''),('[',''),(']',''),('\'',''),('&amp;','&'),('; ','/'),('',''),(' +91',''),('+91',''),('  ','')])
                phone=replace_all(str(cod1),od)
                print(phone)
                std_code,teliphone,mobile,tollfree=fuv(phone)
                print(std_code)
                print(teliphone)
                print(mobile)
        except:
            phone=" "
            std_code,teliphone,mobile,tollfree=fuv(phone)
            print(std_code)
            print(teliphone)
            print(mobile)
        brand="Canon"
        website=""
        link="https://edge.canon.co.in/service-networks"
        row=[link,prod,cat,brand,name,dname,address,pincode,email,website,state,city,lati,long,phone,std_code]
        k=str(row)
        if k not in allz:
            allz.append(k)
            with open('CanonSer.csv','a',encoding='utf-8',newline='') as writeFile:
                writer = csv.writer(writeFile,delimiter='|')
                writer.writerow(row+teliphone)
            row=[cat]
            with open('CanonSer1.csv','a',encoding='utf-8',newline='') as writeFile:
                writer = csv.writer(writeFile,delimiter='|')
                writer.writerow(row+mobile)
url="https://edge.canon.co.in/where-to-buy"
responce=requests.get(url)
soup=BeautifulSoup(responce.text,'html.parser')
al=soup.find(attrs={'class':'top-pad news'})
bl=re.findall('state.*?\}',str(al))
for cl in bl:
    stateid=cl.replace('state":"','').replace('"}','').replace(' ','%20').replace('states=\'[{"','')
    print(stateid)
    state=str(stateid).replace('%20',' ')
    url1="https://edge.canon.co.in/storelocator/getcity/"+str(stateid)
    responce1=requests.get(url1)
    soup1=responce1.json()
    bl1=soup1['data']
    for cl1 in bl1:
        cityid=cl1['city']
        cityid=cityid.replace(' ','%20')
        city=str(cityid).replace('%20',' ')
        print(cityid)
        url2="https://edge.canon.co.in/storelocator/getcat/"+str(stateid)+"/"+str(cityid)
        responce2=requests.get(url2)
        soup2=responce2.json()
        bl2=soup2['data']
        for cl2 in bl2:
            catid=cl2['id']
            cat=cl2['category_title']
            print(catid)
            print(cat)    
            url3="https://edge.canon.co.in/storelocator/getsubcat/"+str(catid)+"/"+str(stateid)+"/"+str(cityid)
            responce3=requests.get(url3)
            soup3=responce3.json()
            bl3=soup3['data']
            for cl3 in bl3:
                scatid=cl3['id']
                scat=cl3['sub_category_title']
                print(scatid)
                print(scat)  
                url4="https://edge.canon.co.in/storelocator/getdealers/"+str(catid)+"/"+str(stateid)+"/"+str(cityid)+"/"+str(scatid)
                responce4=requests.get(url4)
                soup4=responce4.json()
                bl4=soup4['data']
                for cl4 in bl4:
#                     deaid=cl4['id']
                    dea=cl4['dealer_name']
#                     print(deatid)
                    print(dea)   
                    try:
                        url5="https://edge.canon.co.in/storelocatorsearch"
                        data5={
                            "city": str(city),
                            "dealer":  str(dea),
                            "pincode": "",
                            "product_category":  str(catid),
                            "product_sub_category":  str(scatid),
                            "state":  str(state)
                            }
                        head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
                              "Accept": "application/json, text/plain, */*",
                              "Accept-Language": "en-US,en;q=0.5" ,
                              "Referer": "https://edge.canon.co.in/where-to-buy",
                              "X-Requested-With": "XMLHttpRequest",
                              "X-CSRF-TOKEN": "XvMOkCt00pQVELZ84ObczpNWfrrl8z592MxVE6RO",
                              "Content-Type": "application/json;charset=utf-8",
                              "Origin": "https://edge.canon.co.in",
                              "Connection": "keep-alive"}
                        c={
                            "_ga": "GA1.3.49491890.1605074460",
                            "_gid": "GA1.3.177306368.1605074460",
                            "AffinityCookie": "37beeef5422d7c168dddc67d41d9b4393490c131a21c4be8681259f68e2f4369",
                            "AffinityCookieCORS": "37beeef5422d7c168dddc67d41d9b4393490c131a21c4be8681259f68e2f4369",
                            "canon_edge_session": "eyJpdiI6ImxDSG9jSWN5WWk1dWxRb3EwVEJBWFE9PSIsInZhbHVlIjoiMENJbGVyTGNqUTRVWFd6OXI1ZE84OHVsMm1pK3d5bHpJUnNsSkpGVjNRXC9cL1RFaXR0aWRQQ1NMXC9QbEpPSzE1QSIsIm1hYyI6ImU5YzliZDA3MWQ4OTY3M2RjNGU5NTg5MzYxNWRiNWY0NDZmNzYxYzAwOTk0NDdjNGRjZGE4YjEwMDk2Zjk5MzEifQ==",
                            "XSRF-TOKEN": "eyJpdiI6Ilk2XC9YNTUzRlwvQjFzTW5aZmRCWVNxQT09IiwidmFsdWUiOiJTQ2pQSEdWbndaTXZLOEpvYk13bEVcL0JESjI5SzBrUkc2ZlB4SVEybVZJSTJhVHJcL0RxNUk0Q3BpTk9jM1hjelkiLCJtYWMiOiJhZWU2YjE1MzZkMTgwN2M4ZDk5ZWZjMDMxYTA3ZDcwNzlmMmM0MjhmZTViYjFiYWUyNWMxYWY2MmIxNDZmNGNmIn0="
                        }
                        responce5=requests.post(url5,json=data5,headers=head,cookies=c)
                        soup5=responce5.json()
                        soup6=soup5['data'] 
                        for soup7 in soup6:
                            try:
                                nam=soup7['dealer_name']
                                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Tile Size:',''),('Tile Size',''),(':','')])
                                name=replace_all(str(nam),od)
                                print(name)
                            except:
                                name=""
                            try:
                                add=soup7['address']
                                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Tile Size:',''),('Tile Size',''),(':','')])
                                address=replace_all(str(add),od)
                                print(address)
                            except:
                                address=""
                            try:
                                cod=soup7['pincode']
                                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Postal Code',''),('Tile Size',''),(':',''),('  ','')])
                                pincode=replace_all(str(cod),od)
                                print(pincode)
                            except:
                                pincode=""
                            try:
                                cod=soup7['email']
                                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Email',''),('Tile Size',''),(':',''),('  ','')])
                                email=replace_all(str(cod),od)
                                print(email)
                            except:
                                email=""
                            try:
                                cod=soup7['latitude']
                                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Email',''),('Tile Size',''),(':',''),('  ','')])
                                lati=replace_all(str(cod),od)
                                print(lati)
                            except:
                                lati=""
                            try:
                                cod=soup7['longitude']
                                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Email',''),('Tile Size',''),(':',''),('  ','')])
                                long=replace_all(str(cod),od)
                                print(long)
                            except:
                                long=""
                            try:
                                nam=soup7['contact_person']
                                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('NULL',''),('Tile Size',''),(':','')])
                                dname=replace_all(str(nam),od)
                                print(dname)
                            except:
                                dname=""
                            try:
                                nam=soup7['mobile']
                                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('NULL',''),('Tile Size',''),(':','')])
                                mobiled=replace_all(str(nam),od)
                                print(mobiled)
                            except:
                                mobiled=""
                            try:
                                nam=soup7['phone']
                                od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('NULL',''),('Tile Size',''),(':','')])
                                phoneddd=replace_all(str(nam),od)
                                print(phoneddd)
                            except:
                                phoneddd=""
                            try:
                                if mobiled==phoneddd:
                                    phone=""
                                    std_code,teliphone,mobile,tollfree=fuv(phone)
                                else:
                                    cod=soup7['phone']
                                    od = OrderedDict([('\n','~'),('\r',':'),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Telephone',''),('Tile Size',''),(':',''),('  ',''),('</b>',' '),('<br/>','/'),('</div>',''),('\\xa0','')])
                                    cod1=replace_all(str(cod),od)
                                    od = OrderedDict([('\n',' '),('\r',' '),('\t',' '),('Mobile',''),('~',''),('>',''),('[',''),(']',''),('\'',''),('&amp;','&'),('; ','/'),('',''),(' +91',''),('+91',''),('  ','')])
                                    phone=replace_all(str(cod1),od)
                                    print(phone)
                                    std_code,teliphone,mobile,tollfree=fuv(phone)
                                    print(std_code)
                                    print(teliphone)
                                    print(mobile)
                            except:
                                phone=" "
                                std_code,teliphone,mobile,tollfree=fuv(phone)
                                print(std_code)
                                print(teliphone)
                                print(mobile)
                            brand="Canon"
                            website=""
                            link="https://edge.canon.co.in/where-to-buy"
                            row=[link,cat,scat,dea,brand,name,dname,address,pincode,email,website,state,city,lati,long,phoneddd,mobiled,phone,std_code]
                            k=str(row)
                            if k not in allz:
                                allz.append(k)
                                with open('Canon.csv','a',encoding='utf-8',newline='') as writeFile:
                                    writer = csv.writer(writeFile,delimiter='|')
                                    writer.writerow(row+teliphone)
                                row=[cat]
                                with open('Canon1.csv','a',encoding='utf-8',newline='') as writeFile:
                                    writer = csv.writer(writeFile,delimiter='|')
                                    writer.writerow(row+mobile)
                    except:
                        pass

