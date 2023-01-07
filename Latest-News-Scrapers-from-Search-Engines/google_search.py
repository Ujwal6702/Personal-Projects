from bs4 import BeautifulSoup
from urllib.request import Request as rs, urlopen
import pandas as pd
import time
from datetime import datetime
from datetime import timedelta


def google_search():
    try:
        keywords = ["ipo", "listing", "published"]

        site = "https://www.google.com/search?q="
        for i in range(len(keywords)):
            if i == 0:
                site += "%22"+keywords[i]+"%22"
            else:
                site += "+%22"+keywords[i]+"%22"

        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = rs(site, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, "html.parser")

        x = soup.find("div", class_="Pg70bf Uv67qb").a.get("href")

        time.sleep(0.5)

        site = "https://www.google.com"+x

        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = rs(site, headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')

        for i in soup.find_all("li", class_="yNFsl"):
            try:
                if i.a.text == "Past 24 hours":
                    y = i.a.get("href")
                    break
            except:
                continue

        site = "https://www.google.com"+y

        time.sleep(0.5)

        err_logs = []
        list_of_titles = []
        list_of_text = []
        list_of_links = []
        list_of_published_dates = []
        scraped_time = []

        while (True):
            try:
                hdr = {'User-Agent': 'Mozilla/5.0'}
                req = rs(site, headers=hdr)
                page = urlopen(req)
                soup = BeautifulSoup(page, "html.parser")

                for i in soup.find_all("div", class_="Gx5Zad fP1Qef xpd EtOod pkphOe"):
                    try:
                        current_time = datetime.now()
                        link = i.a.get("href").replace("/url?q=", "")
                        name = i.find(
                            "div", class_="BNeawe vvjwJb AP7Wnd").text
                        text = i.find(
                            "div", class_="BNeawe s3v9rd AP7Wnd").text
                        m = -1
                        x = i.find(
                            "div", class_="BNeawe s3v9rd AP7Wnd").span.text
                        a = ""
                        while (True):
                            r = str(x)
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

                m = soup.find("div", class_="nMymef MUxGbd lyLwlc").a

                if m.get("aria-label") == "Next page":
                    site = "https://www.google.com"+str(m.get("href"))
                else:
                    break

                time.sleep(0.6)
            except:
                break

        scrapedData = {}

        scrapedData["title"] = list_of_titles
        scrapedData["link"] = list_of_links
        scrapedData["publish_date"] = list_of_published_dates
        scrapedData["scraped_date"] = scraped_time
        scrapedData["text"] = list_of_text

        google_search = pd.DataFrame(scrapedData)

        if google_search.empty:
            err = "Google News: err: Empty dataframe"
            err_logs.append(err)

        df = FilterFunction(google_search)
        emptydataframe("Google_search", df)
        # df  = link_correction(df)
        return df

    except:
        not_working_functions.append("IPO Google_search")
        print("Google Search not working")
        df1 = pd.DataFrame(
            columns=['title', 'link', 'publish_date', 'scraped_date'])
        return df1
