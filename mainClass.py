import json
import requests
from bs4 import BeautifulSoup
import re
import sys
import urllib
import getopt
from functions.searchDownloader import InstagramSearchDownloader
from functions.InstagramDownloader import InstagramProfileDownloader

def help():
	print "To Get Images from a Profile please pass the flag \"-p\". If You want Images from a search tag please pass the flag \"-s\""
	print "Provide the output folder the images need to be saved to using the flag \"-o\""
	print "For Profile images, please specify the URL using the flag \"u\""
	print "For Search Images please pass the search tag using the flag \"-t\""
	print "Please Use the -n tag to specify the number of images to be downloaded for a given profile or number of pages of search result to be parsed"
	print "If -n is not specified, the program will download all images (can be in hundreds of thousands for a search tag)"
	print "So To download all images from a profile call the function using the following command"
	print"python mainClass.py -p -u \"https://www.instagram.com/hassantest/\" -o images"
	print "To download images from 2 search pages for a given search tag, use the following command"
	print "python mainClass.py -s -t \"travel\" -n 2 -o images"

if __name__ == '__main__':
	typeCheck= False
	outputCheck = False
	downloadType=0
	number=0
	url=""
	outputFolder=""
	tag=""
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'hpsn:u:t:o:', [])
	except getopt.GetoptError:
		print "Error "
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			help()
			sys.exit(2)
		elif opt in ('-p'):
			downloadType=0
			typeCheck=True
		elif opt in ('-s'):
			downloadType=1
			typeCheck=True
		elif opt in ('-n'):
			number = int(arg)
		elif opt in ('-u'):
			url = str(arg)
		elif opt in ('-t'):
			tag = str(arg)
		elif opt in ('-o'):
			outputFolder=str(arg)
			outputCheck =True
		else:
			print "error"
			sys.exit(2)

	
	if(downloadType==0 and url==""):
		print "URL Not given"
		sys.exit(2)
	if(downloadType==1 and tag==""):
		print "Tag Not given"
		sys.exit(2)
	if(not typeCheck):
		print "Downloader Type not specified"
		sys.exit(2)
	if (not outputCheck):
		print "Output Foler not Specified"
		sys.exit(2)
	if(downloadType==0):
		downloader =InstagramProfileDownloader()
		downloader.download(url,outputFolder,number)
	if(downloadType==1):
		downloader =InstagramSearchDownloader()
		downloader.download(tag,outputFolder,number)





