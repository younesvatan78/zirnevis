#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 00:30:07 2019

@author: kia


site: kiahamedi.ir
instagram: kia.hamediii

"""

import requests
from bs4 import BeautifulSoup
from os import system
from os import path

movie = str(input('Enter Movie (Example Avengers Endgame):'))
formatt = str(input('Enter Format (Example WEB-DL):'))
res = str(input('Enter Res (Example 720):'))



baseUrl = "http://subf2m.ir"
nameMovie = movie.replace(" ","+")

searchurl = baseUrl+"/subtitles/زیرنویس-فارسی-searchbytitle?query="+str(nameMovie)
searchPage = requests.get(searchurl)
soup = BeautifulSoup(searchPage.content,'html5lib')
div = soup.find('div',{"class":"title"})

namesArray = nameMovie.split("+")
searchNameFound = div.text.strip()
#print(searchNameFound)
#print(namesArray)

for check in namesArray:
    if check not in searchNameFound:
        print("not exist this movie")
        exit(0)
        
urlMovie = baseUrl + div.find('a')['href']
moviePage = requests.get(urlMovie)


counter = 1
soup = BeautifulSoup(moviePage.content,'html5lib')
for item in soup.find_all('li',{"class":"item"}):
    for name in item.find_all('ul',{"class":"scrolllist"}):
        if formatt in name.text.strip() and res in name.text.strip():
            urlDownloadPage = baseUrl + item.find('a',{"class":"download icon-download"})['href']
            #print(urlDownloadPage)
            downloadPage = requests.get(urlDownloadPage)
            soup = BeautifulSoup(downloadPage.content,'html5lib')
            aURLDOWNLOAD = soup.find('a',{"id":"downloadButton"})['href']
            print(aURLDOWNLOAD)
            system("wget -O "+str(counter)+".zip '"+baseUrl+""+aURLDOWNLOAD+"'")
            system("unzip "+str(counter)+".zip && rm "+str(counter)+".zip")
            counter += 1
            
        else:
            continue
        
# Move to Folder
MovieDirectory = movie + ' subtitles'
#if not path.isdir(MovieDirectory):

system("mkdir '" + MovieDirectory + "' && mv *.srt '" + MovieDirectory + "'")
#else:
 #   system("mv *.srt '" + MovieDirectory + "'")