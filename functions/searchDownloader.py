import json
import requests
from bs4 import BeautifulSoup
import re
import sys
import urllib
import getopt
class InstagramSearchDownloader(object):
	def __init__(self):
		pass


	def downloadImage(self,imageList,outputFolder,num):
		for val in imageList:
			if(not val["node"]["is_video"]):
				urllib.urlretrieve(val["node"]["display_url"], str(outputFolder)+"/image"+str(num)+".jpg")
				num=num+1
		return num
	def downloadHighQualityImage(self,imageList,outputFolder,num):
		for val in imageList:
			if(not val["node"]["is_video"]):
				
				url="https://www.instagram.com/p/"+str(val["node"]["shortcode"])+"/?__a=1"
				r = requests.get(
					url=url,
					headers={
					'X-Requested-With': 'XMLHttpRequest'
					}
				)
				jsonData=json.loads(r.text)["graphql"]["shortcode_media"]
				urllib.urlretrieve(jsonData["display_url"], str(outputFolder)+"/image"+str(num)+".jpg")
				num=num+1
		return num

	

	def download(self,tag,outputFolder,maxPage):
		url = "https://www.instagram.com/graphql/query/?query_id=17875800862117404&variables={\"tag_name\":\""+str(tag)+"\",\"first\":10}"
		r = requests.get(
		url=url,
		headers={
			'X-Requested-With': 'XMLHttpRequest'
			}
		)
		jsonData= json.loads(r.text)["data"]["hashtag"]

		hasNext = jsonData["edge_hashtag_to_media"]["page_info"]["has_next_page"]
		cursor =  jsonData["edge_hashtag_to_media"]["page_info"]["end_cursor"]

		num=1
		page=1
		
		num=self.downloadImage(jsonData["edge_hashtag_to_media"]["edges"],outputFolder,num)
		while(hasNext):
			url = " https://www.instagram.com/graphql/query/?query_id=17875800862117404&variables={\"tag_name\":\""+tag+"\",\"first\":10,\"after\":\""+cursor+"\"}"
			r = requests.get(
				url=url,
				headers={
					'X-Requested-With': 'XMLHttpRequest'
				}
				)
			jsonData= json.loads(r.text)["data"]["hashtag"]
			hasNext = jsonData["edge_hashtag_to_media"]["page_info"]["has_next_page"]
			cursor =  jsonData["edge_hashtag_to_media"]["page_info"]["end_cursor"]
			num=self.downloadImage(jsonData["edge_hashtag_to_media"]["edges"],outputFolder,num)
			page=page+1
			if(maxPage==0):
				continue
			elif(page>=maxPage):
				break




# if __name__ == '__main__':
# 	downloadType=0
# 	highQuality=False
# 	number=0
# 	url=""
# 	tag=""
# 	try:
# 		opts, args = getopt.getopt(sys.argv[1:], 'pshln:u:t:', [])
# 	except getopt.GetoptError:
# 		print "Error "
# 		sys.exit(2)
# 	for opt, arg in opts:
# 		if opt in ('-q', '--help'):
# 			print "Help"
# 			sys.exit(2)
# 		elif opt in ('-p'):
# 			downloadType=0
# 		elif opt in ('-s'):
# 			downloadType=1
# 		elif opt in ('-h'):
# 			highQuality=True
# 		elif opt in ('-l'):
# 			highQuality=False
# 		elif opt in ('-n'):
# 			number = int(arg)
# 		elif opt in ('-u'):
# 			url = str(arg)
# 		elif opt in ('-t'):
# 			tag = str(arg)
# 		else:
# 			print "error"
# 			sys.exit(2)

# 	print "Type: "+str(downloadType)+" High Quality: "+str(highQuality)+ " URL: "+str(url)+" Tag: "+str(tag)+" Number: "+str(number)
# 	if(downloadType==0 and url==""):
# 		print "URL Not given"
# 		sys.exit(2)
# 	if(downloadType==1 and tag==""):
# 		print "Tag Not given"
# 		sys.exit(2)
	# print len(sys.argv)
	# if(len(sys.argv)<3 or len(sys.argv)>3):
	# 	print "Incorrect Parameters\n please provide the following two parameters in order\nProfile URL\nOutput Foldername"
	# try:
	# 	tag = str(sys.argv[1])
	# 	outputFolder=str(sys.argv[2])
	# 	maxPage = int(sys.argv[3])
	# except Exception as e:
	# 	print "Input Not provided Properly : "+ str(e) 

	# downloader = InstagramDownloader()
	# downloader.download(tag,outputFolder,maxPage)
	

	


	




#