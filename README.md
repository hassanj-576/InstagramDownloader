# Instagram Image Downloader v2.0
This is a small script I wrote that can be used to download images from Instagram. It has two main modes

* Profile Mode
* Search Mode

### Profile Mode
In Profile mode, the script download images from a public Instagram profile. You provide the script with a URL to a public Instagram profile and it downloads the images for the given profile

### Search Mode
In search mode, the script download the images returned by Instagram for a given search tag. The user provides a search tag and the script downloads the images for the given tag.

## Input Parameters
The script takes a number of input parameters in form of flags. They are mentioned below

### -p
Use this flag to run the script in profile mode
### -s
Use this flag to run the script in search mode
### -u <url>
When in profile mode, use this flag to specify the url of the user you want images of
### -t <tag>
When in search mode, use this flag to specify the search tag you want the images for
### -o
Use this flag to specify the output folder to save the images to. Please make sure the folder already exist as the script does not create it and will throw an error if the folder is not found
### -n <number>
This flag is used to specify the the quantity of images that are downloaded. In Profile Mode this specify how many images to download from the profile. In search mode this specifies how many pages of search result should the script extract images from. If this parameter is not passed or is set to 0, the script will download all images. WARNING for search mode, the number of images can be in tens of thousands if -n is not specified. 

## Usage 
This a python script and uses the library "Beautiful Soup" (https://www.crummy.com/software/BeautifulSoup/bs4/doc/). To run the script the users needs to have python installed on their computer. BeautifulSoup also needs to be installed for the script to run.

Pip can be used to install beautiful soup

`pip install beautifulsoup4`

Once the library has been installed, the script can be run like any other python script using the python command.

For example, to run the code in Profile Mode use the following command

`python mainClass.py -p -u "https://www.instagram.com/hassantest/" -o images`

This will download all the images from the given profile URL to the images folder. 

To run the code in Search Mode following command can be used 

`python mainClass.py -s -t "travel" -n 2 -o images`

This will download images from two search pages for the tag "travel" and store it in the images folder

## Purpose
The first version of this Instagram Image downloader only downloaded images from public Instagram profiles. I created that script out of curiosity when working on parsing data from Instagram for my job. One of my friend suggested that downloading images based on a search tag might be more useful. Data scientist often need large amount of data and being able to download images for a certain tag could be useful for their research. So I started working on this version. Turns out its equally as simple to download images from search results. I created this script out of curiosity and it should be used for academic or testing purpose. Downloading some ones images though legal if posted publicly, is unethical if done for the wrong reasons. I urge anyone using this library to use it for educational purposes or for testing and learning about extracting data from social networks

## Future Works
* I am open to suggestions to anything else that can be added
* Error Handling 
* Adding comments and improving code quality 