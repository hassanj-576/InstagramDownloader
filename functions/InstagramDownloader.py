import json
import requests
from bs4 import BeautifulSoup
import re
import sys
import urllib

class InstagramProfileDownloader(object):
	def __init__(self):
		pass

	def download(self,URL,outputFolder,max):
		#print "In get User Detail"
		r = requests.get(
		url=URL,
		headers={
			'X-Requested-With': 'XMLHttpRequest'
			}
		)
		soup = BeautifulSoup(r.text,"html.parser")
		num=1
		for script in soup.findAll('script')[1]:
			userDetails ={}
			data = re.search(r"window._sharedData = (.*?);$", script.string).group(1)
			jsonData= json.loads(data)["entry_data"]["ProfilePage"][0]["user"]["media"]

		
			for val in jsonData["nodes"]:
				try:
					urllib.urlretrieve(val["display_src"], str(outputFolder)+"/image"+str(num)+".jpg")
				except Exception as e:
					print "Error while saving file - Error Message : "+str(e)
					return 
				id=val["owner"]["id"]
				num=num+1
			hasNext=jsonData["page_info"]["has_next_page"]
			cursor =jsonData["page_info"]["end_cursor"]
			if (max==0):
				pass
			elif (num>=max):
				return
			while (hasNext):
				url= "https://www.instagram.com/graphql/query/?query_id=17888483320059182&variables={\"id\":\""+id+"\",\"first\":12,\"after\":\""+str(cursor)+"\"}"
				r = requests.get(
					url=url,
					headers={
					'X-Requested-With': 'XMLHttpRequest'
					}
				)
				
				jsonData=json.loads(str(r.text))["data"]["user"]["edge_owner_to_timeline_media"]
				hasNext=jsonData["page_info"]["has_next_page"]
				cursor =jsonData["page_info"]["end_cursor"]
				for val in jsonData["edges"]:
					try:
						urllib.urlretrieve(val["node"]["display_url"], str(outputFolder)+"/image"+str(num)+".jpg")
					except Exception as e:
						print "Error while saving file - Error Message : "+str(e)
						return 
					num=num+1
				if(not num==0 and num>=max):
					break


			
	



	


	




#