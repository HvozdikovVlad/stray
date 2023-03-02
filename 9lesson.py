#import requests
#res_parse_list = []

#response = requests.get("https://coinmarketcap.com/")
#response_text = response.text
#response_parse = response_text.split("<span>")
#for parse_elem_1 in response_parse:
#    if parse_elem_1.startswith("$"):
#        for parse_elem_2 in parse_elem_1.split("</span>"):
#            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                res_parse_list.append(parse_elem_2)
#
#bitcoin_exchange_rate = res_parse_list[0]
#print(bitcoin_exchange_rate)

from bs4 import BeautifulSoup
import requests
response = requests.get("https://oschadbank.ua/currency-rate")


if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td", {"class":"heading-block-currency-rate__table-col"})
    res = soup_list[10]
    print(res.text)
dollar=float(res.text)
grn=float(input("ввидите количество гривен которую хотите обменять "))
class Convert:
    def convert(self,grn, dollar):
        print(round(grn/dollar, 2))
convert = Convert()
convert.convert(grn, dollar)