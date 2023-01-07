
from bs4 import BeautifulSoup
from urllib.request import Request as rs, urlopen
import pandas as pd
import time
from datetime import datetime
from datetime import timedelta


def bing_search():
    try:
        keywords = ["ipo", "listing", "planned"]

        site = "https://www.bing.com/news/search?q="
        for i in range(len(keywords)):
            if i == 0:
                site += "%22"+keywords[i]+"%22"
            else:
                site += "+%22"+keywords[i]+"%22"

        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = rs(site, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")

        x = soup.find("div", id="newsFilterV5")
        x = x.ul.li.ul
        for i in x.find_all("li"):
            if str(i.text) == "Past 24 hours":
                y = i.a.get('href')

        time.sleep(0.4)

        site = "https://www.bing.com"+y
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = rs(site, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")

        err_logs = []
        list_of_titles = []
        list_of_text = []
        list_of_links = []
        list_of_published_dates = []
        scraped_time = []

        for i in soup.find_all("div", class_="news-card newsitem cardcommon b_cards2"):
            try:

                current_time = datetime.now()

                name = i.find("div", class_="t_t").a.text

                text = i.find("div", class_="snippet").text

                link = i.find("div", class_="t_t").a.get('href')

                m = -1
                x = i.find_all("span")
                a = ""
                while (True):
                    r = str(x[m].text)
                    for j in r:
                        if j.isdigit():
                            a += j
                    if len(a) > 0:
                        break
                    else:
                        m -= 1
                n = int(a)
                past_time = current_time - timedelta(hours=n)
                published = past_time.strftime('%d-%m-%Y')

                list_of_titles.append(name)
                list_of_text.append(text)
                list_of_links.append(link)
                list_of_published_dates.append(published)
                scraped_time.append(current_time)

            except:
                err_logs.append(i)

        scrapedData = {}

        scrapedData["title"] = list_of_titles
        scrapedData["link"] = list_of_links
        scrapedData["publish_date"] = list_of_published_dates
        scrapedData["scraped_date"] = scraped_time
        scrapedData["text"] = list_of_text
        bing_search = pd.DataFrame(scrapedData)

        if bing_search.empty:
            err = "Google News: err: Empty dataframe"
            err_logs.append(err)

        """df = FilterFunction(bing_search)
        emptydataframe("bing_search", df)
        # df  = link_correction(df)
        return df"""
    except:
        not_working_functions.append("IPO Bing_search")
        print("Bing Search not working")
        df1 = pd.DataFrame(
            columns=['title', 'link', 'publish_date', 'scraped_date'])
        return df1


bing_search()
