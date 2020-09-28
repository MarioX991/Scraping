#!/user/bin/env/ python

import requests
from bs4 import BeautifulSoup
import pprint

url = 'https://www.humblebundle.com/books/programming-productivity-mercury-books'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

# headers above each book colection

#this is one way to grab information but problem with this method is if in the future ownor deside to put another h2 tag into the current page,
# this culd break our code for this reasone we need to do this with the class selector.
# title_head = soup.find_all('h2')

headline = soup.select('.dd-header-headline')
dataHead = [line.text.strip() for line in headline]

# Products name 
product_name = soup.select('.dd-image-box-caption')
stripped_product_name  = [name.text.strip() for name in product_name]





#for lineName, lineinfo in dataHead.items():
#    print(lineName)
#    print("priced at", lineinfo["price"])
#    print("priduct name: ", lineinfo["priducts"])



 
# headline 1 name and price 
#  - product 1
#  - product 2
#  - product 4
#headline 2 name and price 
#  - product 1
#  - product 2
#  - product 4






