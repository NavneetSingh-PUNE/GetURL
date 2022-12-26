#!/usr/bin/python3
import os,requests

def url():
    f=open("target.txt","r+")
    a=f.readlines()
    for i in a:
        b=os.popen("getallurls {}".format(i)).read()
        try:
            os.system("rm -f allurls.txt")
        except IOError as a:
            print("No file named allurls.txt found",a)
        e=open("allurls.txt","w+")
        e.writelines(b)
        e.close()
    f.close()

def statcode():
    g=open("allurls.txt","r+")
    p=g.readlines()
    for i in p:
        r=i.strip("\n")
        yum=str(requests.get(r))
        yum2=requests.get(r)
        try:
            fullurl=r+"\t"+str(yum2.status_code)+"\t"+str(yum2.headers['Server']+"\t"+str(yum2.is_redirect))
            print(fullurl)
        except Exception as ex:
            print("No server, dead website", ex)
        else:
            fullurl=r+"\t"+str(yum2.status_code)+"\t"+"NULL"
            print(fullurl)
       # f=open("statcodeurl.txt","w+")
       # f.writelines(fullurl)
       # f.close()
    g.close()

url()
statcode()
