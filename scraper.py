# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import requests
import os
from bs4 import BeautifulSoup

os.environ['SCRAPERWIKI_DATABASE_NAME'] = 'sqlite:///data.sqlite'
import scraperwiki

postcode = 2193
urltemplate = "https://electorate.aec.gov.au/LocalitySearchResults.aspx?filter={}&filterby=Postcode"
url = str.format(urltemplate, postcode)

page = requests.get(url).content
bs4 = BeautifulSoup(page, "html.parser")

results = bs4.find(id='ContentPlaceHolderBody_gridViewLocalities')

rows = results.find_all('tr')
for row in rows:
    tds = row.find_all('td')
    if tds:
        rowdata = {'state': tds[0].text, 'suburb': tds[1].text, 'postcode': tds[2].text, 'electorate': tds[3].text, 'redistributed': tds[4].text, 'other': tds[5].text}
        scraperwiki.sqlite.save(unique_keys=('state', 'suburb', 'postcode', 'electorate'), data=rowdata, table_name='data')
