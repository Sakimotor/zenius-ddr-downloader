import requests
from bs4 import BeautifulSoup
import urllib.request

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
                url = url_download + str(option['value'])
                print(url)
                #Save the file locally
                data = urllib.request.urlopen(url).read()
                file = open(option.text + ".zip", 'wb')
                file.write(data)