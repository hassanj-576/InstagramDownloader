# InstagramDownloader
This a simple Instagram downloader script. It downloads all the images for a given Instagram public profile. The profile has to be public. This program does not require an Instagram API key or developer account.

Running the script is quite simple, It takes two arguments 
* Profile URL
* Output Folder Path

It can be run using the following command

`python InstagramDownloader.py "url" "path"`

For example

`python InstagramDownloader.py "https://www.instagram.com/hassantest/" "images"`

This will download all the images from the above given URL to a folder images.

The script uses the library "Beautiful Soup" (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the initial profile page.

Pip can be used to install beautiful soup

`pip install beautifulsoup4`

Once beautiful soup is installed, the script should work fine. 
Currently the script download all images and saves them with the name "imagesxx.jpg" where xx is the image number starting from 1 till the total number of images.


This script is for educational purposes only. The idea came to my mind while writing an Instagram scrapper to extract public user information. I realized its quite easy to download images from Instagram hence wrote this little script. Please use it for learning and testing and use it only for profiles you have permission from owner to download their images. I shall not be held responsible for any misuse of the script


## Future Works
I plan to add following features
* Allow user to specify how many images to download
* Allow users to specify a caption to download only that image
