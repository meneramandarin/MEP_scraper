import requests
from lxml import html
from MEPscraper import MEPscraper
import xlwt


meps = 1 #starts at 2 goes till 752
mep_found = 0
page = requests.get("http://www.europarl.europa.eu/meps/en/full-list.html?filter=all&leg=")
tree = html.fromstring(page.content)

UKMEPscraper = True

wb = xlwt.Workbook()
ws = wb.add_sheet("UK_MEPs", cell_overwrite_ok=True)

while UKMEPscraper:
    meps = meps + 1
    DefineXpath = ('''//*[@id="content_left"]/div[%s]/div[1]/ul/li[3]/text()''' % meps)
    MEPxpath = tree.xpath(DefineXpath)
    # other method MEPxpath = ('//*[@id="content_left"]/div[{}]/div[1]/ul/li[3]/text()'.format(meps))
    #print MEPxpath
    MEPxpath = str(MEPxpath)
    if "United Kingdom" in MEPxpath:
        print
        print MEPxpath
        MEPhref = tree.xpath('''//*[@id="content_left"]/div[%s]/div[1]/ul/li[1]/a/@href''' % meps) [0]
        MEPurl =  ("http://www.europarl.europa.eu") + MEPhref
        print MEPurl
        try:
            MEPscraper(MEPurl, mep_found, ws) #puts url into scraper, counter for number of meps, ws-> for xml file
        except Exception as ex:
            print(ex.message)
        mep_found+=1
    if meps >= 753:
        UKMEPscraper = False  # makes script stop

wb.save ("MEPs.xls")
