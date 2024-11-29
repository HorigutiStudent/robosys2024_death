#!/usr/bin/python3

import requests
from get_datetime import GetDateTime

if __name__ == "__main__":
    getdatetime = GetDateTime()
    
    month = getdatetime.get_month()
    week = getdatetime.get_week()
    #print(month,week)
    url = f"https://www.cit-s.com/wp/wp-content/themes/cit/menu/sd1_2024{month}_{week}.png"
    file_name = "pictures/menue.jpg"

    response = requests.get(url)
    image = response.content
    
    with open(file_name,"wb") as p:
      p.write(image)