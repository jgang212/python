# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:52:36 2018

@author: jack.gang
"""

from os import chdir
import pandas as pd
import requests
import random
import csv
import names

#CREATE TABLE WatchUser (
#	UserName varchar(16) PRIMARY KEY,
#    RealName varchar(32),
#    Age int,
#    ZipCode char(5),
#    FavoriteWatch varchar(50)
#    );
#
#CREATE TABLE Watch (
#	WatchName varchar(50) PRIMARY KEY,
#    WatchType varchar(20),
#    Price real,
#    CreationYear char(4),
#    MovementID varchar(20),
#    CompanyName varchar(30)
#    );
#
#CREATE TABLE Sells (
#	StoreName varchar(50),
#    WatchName varchar(50),
#    SoldDate date
#    );

chdir('S:\HQ-FS-Trader\Equity Group\Jack Gang\Impulse Betas')

###############################################################

# 10,001 Watches
Watch = pd.DataFrame(columns=['WatchName', 'WatchType', 'Price', 'CreationYear', 'MovementID', 'CompanyName'])

## list of words for WatchName
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site, auth=('user', 'pass'))
WORDS = response.content.splitlines()

## WatchType
types = ['Digital', 'Automatic', 'Dress', 'Sport', 'Smart', 'Diving', 'Pilot']

## MovementID
movements = ["Calibre 5", "ETA-2824", "Quartz", "JLC 965", "El Primero 400B", "8500", "ML 159", "Valjoux 7750", "Caliber 5000", "Caliber 2121"]

## CompanyName
companies = ["Tag Heuer", "Jaeger-LeCoultre", "Maurice Lacroix", "IWC", "Audemars Piguet", "Omega", "Zenith", "Apple", "Tissot", "Casio"]

## create random Watch entries
for i in range(0, 10001):
    WatchName = random.choice(WORDS)
    WORDS.remove(WatchName)
    WatchName = WatchName.decode("utf-8").capitalize()
        
    WatchType = random.choice(types)    
    Price = float(random.randrange(5, 10000, 5))
    CreationYear = int(random.randint(1850, 2018)) 
    MovementID = random.choice(movements)
    CompanyName = random.choice(companies)    
    
    Watch.loc[i] = [WatchName, WatchType, Price, CreationYear, MovementID, CompanyName]

Watch.to_csv("Watch.csv", header = Watch.columns, index = False, quoting = csv.QUOTE_NONE, quotechar = '', float_format='%.12f')

###############################################################

# 10,001 WatchUsers
WatchUser = pd.DataFrame(columns=['UserName', 'RealName', 'Age', 'ZipCode', 'FavoriteWatch'])

## create random WatchUser entries
for i in range(0, 10001):
    RealName = names.get_full_name()
    
    UserNameString = RealName.split()[0][0].lower() + RealName.split()[1].lower()
    UserNameInt = random.randint(100, 999)
    UserName = UserNameString + str(UserNameInt)
    while UserName in WatchUser.UserName:
        UserNameInt = random.randint(100, 999)
        UserName = UserNameString + str(UserNameInt)
    
    Age = random.randint(13, 100)
    ZipCode = "{0:0=5d}".format(random.randint(0, 99999))
    FavoriteWatch = random.choice(Watch.WatchName)  
    
    WatchUser.loc[i] = [UserName, RealName, Age, ZipCode, FavoriteWatch]

WatchUser.to_csv("WatchUser.csv", header = WatchUser.columns, index = False, quoting = csv.QUOTE_NONE, quotechar = '', float_format='%.12f')

###############################################################

# 50,001 Sells
Sells = pd.DataFrame(index=range(0, 50001), columns=['StoreName', 'WatchName', 'SoldDate'])

## StoreName
stores = ["Princeton Jewelers", "Fine Jewelers's", "Jomashop", "The Times", "Haute Horology", "Fresh Jewelers", "Marcy's", "Biao", "WatchUSeek", "At The Tower"]

## create random Sells entries
for i in range(0, 50001):
    StoreName = random.choice(stores)   
    WatchName = random.choice(Watch.WatchName)  
    
    year = random.randint(1850, 2018)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    SoldDate = str(year) + "-" + "{0:0=2d}".format(month) + "-" + "{0:0=2d}".format(day)
    
    Sells.loc[i] = [StoreName, WatchName, SoldDate]
    
Sells.to_csv("Sells.csv", header = Sells.columns, index = False, quoting = csv.QUOTE_NONE, quotechar = '', float_format='%.12f')