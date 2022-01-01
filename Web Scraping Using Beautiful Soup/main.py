from bs4 import BeautifulSoup
import requests

website = 'https://www.airbnb.co.in/rooms/24837621?category_tag=Tag%3A8047&adults=1&check_in=2022-01-09&check_out=2022-01-16&federated_search_id=7611af2d-ad3a-4d83-91e3-72ceca17aa84&source_impression_id=p3_1640893452_QZsNMSrtLd29VexQ&guests=1&translate_ugc=true'

result = requests.get(website)
content = result.text

#parser
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())


# Printing the title of the homestay
box_1 = soup.find('span', class_ = '_1n81at5')
homestay_title = box_1.find('h1').get_text()

print("HomeStay Name:", homestay_title)

# Printing the about the homestay

price = soup.find('span', class_ = 'a8jt5op dir dir-ltr').get_text()

print(price)

with open(f'{homestay_title}'+' OnAirBnBWishlistPriceChecker.txt','w') as file:
    file.write(homestay_title)
    file.write('\n')
    file.write(price)


