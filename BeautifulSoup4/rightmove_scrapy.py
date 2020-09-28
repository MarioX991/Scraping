#package
# Beautifulsout ill be use for parcing data
from bs4 import BeautifulSoup
# this get  request from the specific URl 
import requests

import urllib
import json
import csv




#propertyCard-title


class RightmoveScraper():

    results = []

    def fetch(self, url):
        print('HTTP GET request to URL: %s' %url, end='')
        response = requests.get(url)
        print('  |  Status code: %s' %response.status_code)

        return response

    def parse(self, html):
        #print(html)
        content = BeautifulSoup(html, "lxml")
        # Title of ad
        titles = [title.text.strip() for title in content.findAll('h2',{'class' : 'propertyCard-title'})]
        #print(title)
        # Grab adress for current property
        addresses = [address['content'] for address in content.findAll('meta', {'itemprop' : 'streetAddress'})]
        #print(address)

        #property description
        descriptions = [description.text for description in content.findAll('span',{'data-test' : 'property-description'})]
        #print(descriptions)

        #extracting the price
        prices = [price.text.strip() for price in content.findAll('div',{'class' : 'propertyCard-priceValue'})]
        #print(prices)

        #Data when property added on the site
        date = [date.text.split(" ")[2] for date in content.findAll('span', {'class' : 'propertyCard-branchSummary-addedOrReduced'})]
        #print(date)

        #sellers name
        sellers = [seler.text.split('by ')[1] for seler in content.findAll('span',{'class' : 'propertyCard-branchSummary-branchName'})]
        #print(sellers)

        # get images URLitemprop="image"
        images = [image['src'] for image in content.findAll('img',{'itemprop' : 'image'})]
        
        for index in range(0, len(titles)):
            self.results.append({
                'title': titles[index],
                'address':addresses[index],
                'description': descriptions[index],
                'date': date[index],
                'prince':prices[index],
                'seller':sellers[index],
                'images': images[index]
                })
            #print(json.dumps(item, indent=2))


    def to_csv(self):
        with open('rightmove.csv','w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
            writer.writeheader()


            for row in self.results:
                writer.writerow(row)
            print('Stored results to "rightmove.csv"')


    def run(self):
        #response = self.fetch('https://www.rightmove.co.uk/property-for-sale/London.html')

        html =''
        with open('res.html',"r") as html_file:
            for line in html_file:
                html += html_file.read()
        self.parse(html)
        self.to_csv()


if __name__=='__main__':
    scraper = RightmoveScraper()
    scraper.run()
