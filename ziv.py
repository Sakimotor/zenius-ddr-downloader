import requests
from bs4 import BeautifulSoup
import urllib.request
import argparse
import os

#Argument parsing for folder management
parser = argparse.ArgumentParser(description='Program that downloads all the official simfile packs from https://zenius-i-vanisher.com/')
parser.add_argument('-s','--songs', help='The Songs folder for your StepMania setup')
songs_folder = parser.parse_args().songs
if songs_folder == None:
    songs_folder = os.getcwd()
#Prepare the URL we will use at the end
url_download = "https://zenius-i-vanisher.com/v5.2/download.php?type=ddrpack&categoryid="
#Get html page as string
page = requests.get("https://zenius-i-vanisher.com/v5.2/simfiles.php?category=simfiles").text
#Parse it with BS4
soup = BeautifulSoup(page, 'html.parser')
select_list = soup.find_all("select")
for select in select_list:
    #Exclude User-made simfiles
    if select.find_parent().find_previous_sibling("td").text != "User":
        print(select.find_parent().find_previous_sibling("td").text)
        option_list = select.find_all("option")
        for option in option_list:
            #Exclude null values ("Select a category" option )
            if option['value'] != "0":
                if os.path.isdir(songs_folder + "\\" + option.text) == False:
                    url = url_download + str(option['value'])
                    print(url)
                    #Save the file locally
                    data = urllib.request.urlopen(url).read()
                    file = open(songs_folder + "\\" + option.text + ".zip", 'wb')
                    file.write(data)
