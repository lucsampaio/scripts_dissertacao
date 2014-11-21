# -*- coding: utf-8 -*-
"""
Created on Wed May  7 18:38:20 2014

This script was designed to facilitate the downloading of a large number of files (images, initially) based on a CSV file with the following fields:
column 1: ID (how the file should be named after download)
column 2: link (the http address to the file you want to download)

@author: Luciano de Sampaio Soares
"""

#modules used
import os
import urllib
import csv

#variables
#download folder
folder = #"Add your download path within these quotes and remove the # comment marking"
filelist = #"add the name of the download list (a .csv file) within the quotes and remove the # comment marking"

#helper functions

def directory():
    """
    Sets working PATH to csv file
    """
    global folder
    os.chdir(folder)
    os.getcwd()


def readfile():
    """
    Finds file link to download, and saves image to proper folder, already
    named according to csv
    """
    global filelist, folder
    with open(filelist,"rb") as f:
        read = csv.reader(f) 
        for row in read:
            url = row[1]
            location = os.path.join(folder,"img/")
            filename = str(row[1])
            extension = filename[-4:] #keeps the proper extension to the downloaded file
            target = str(row[0])+ extension
            os.chdir(location)
            if target == os.path.isfile(target): #prevents downloading duplicate files
                print "o arquivo " + str(target) + " já existe neste diretório"
            else:
                urllib.urlretrieve(url,target)
                print target

#call functions
directory()
readfile()
