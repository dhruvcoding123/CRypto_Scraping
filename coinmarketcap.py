# scraper/coinmarketcap.py
import requests
from bs4 import BeautifulSoup

class CoinMarketCap:
    BASE_URL = "https://coinmarketcap.com/currencies/"

    def __init__(self, coin_name):
        self.coin_name = coin_name
        self.url = f"{self.BASE_URL}{coin_name}/"

    def scrape_data(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        
        data = {}
        try:
            data['price'] = self.extract_price(soup)
            data['price_change'] = self.extract_price_change(soup)
            data['market_cap'] = self.extract_market_cap(soup)
            data['volume'] = self.extract_volume(soup)
            data['volume_market_cap'] = self.extract_volume_market_cap(soup)
            data['circulating_supply'] = self.extract_circulating_supply(soup)
            data['total_supply'] = self.extract_total_supply(soup)
            data['diluted_market_cap'] = self.extract_diluted_market_cap(soup)
            data['contracts'] = self.extract_contracts(soup)
            data['official_links'] = self.extract_official_links(soup)
            data['socials'] = self.extract_socials(soup)
        except Exception as e:
            print(f"Error scraping {self.coin_name}: {e}")
        
        return data

    def extract_price(self, soup):
        return soup.select_one('.priceValue').text

    def extract_price_change(self, soup):
        return soup.select_one('.sc-15yy2pl-0.gEePkg').text

    def extract_market_cap(self, soup):
        return soup.select_one('.statsValue').text

    def extract_volume(self, soup):
        return soup.select('.statsValue')[1].text

    def extract_volume_market_cap(self, soup):
        return soup.select('.statsValue')[2].text

    def extract_circulating_supply(self, soup):
        return soup.select('.statsValue')[3].text

    def extract_total_supply(self, soup):
        return soup.select('.statsValue')[4].text

    def extract_diluted_market_cap(self, soup):
        return soup.select('.statsValue')[5].text

    def extract_contracts(self, soup):
        contracts = []
        for contract in soup.select('.contract-row'):
            contracts.append({
                'name': contract.select_one('.name').text,
                'address': contract.select_one('.address').text
            })
        return contracts

    def extract_official_links(self, soup):
        links = []
        for link in soup.select('.cmc-link'):
            links.append({
                'name': link.text,
                'link': link['href']
            })
        return links

    def extract_socials(self, soup):
        socials = []
        for social in soup.select('.sc-16r8icm-0.fQcuXD'):
            socials.append({
                'name': social.select_one('.icon').text,
                'url': social['href']
            })
        return socials
