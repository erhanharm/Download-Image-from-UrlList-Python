import urllib
import distutils.dir_util
import sys, os
from bs4 import BeautifulSoup 
import requests

pathname = os.path.dirname(sys.argv[0])#get current script path

with open("file.txt", "r") as ins:  #read file for imagelinks
    for line in ins: # each line is a URL --sample URL https://venderfirm.theircdn.com/productimages/i/b2342arco34234de/[img][5][1].jpg
        urlsplit = line.split("/") 
        #print distutils.dir_util.mkpath(urlsplit[5]) #create a path for nonexisting barcode
        #print os.path.abspath(pathname)
        destPath = os.path.abspath(pathname)+'/'+urlsplit[5]+'/'+urlsplit[6]
        #print destPath
        #urllib.urlretrieve(line, os.path.abspath(pathname)+urlsplit[5]+"deneme.jpg")
        try:
            print line
            page = requests.get(line.replace("\r","").replace("\n","")) # line ending chars throws 404 issue 
            #page = requests.get('https://img-morhipo.mncdn.com/productimages/i/MH114006038318/[img][5][1].jpg')
            print page.status_code
            if page.status_code != 200:
    			print 'url not found'
            else:
                print 'URL FOUND AND DIRECTORY CREATED'
                print distutils.dir_util.mkpath(urlsplit[5])
                urllib.urlretrieve(line,destPath)
        except Exception,e:
    		print e
