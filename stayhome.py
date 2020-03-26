#!/usr/bin/python3

import bs4 as bs
import re, sys
from urllib.request import Request, urlopen

#Name of list you want to save the output to
list_name = 'list.txt'
full_list = open(list_name, 'w') 

# This is the https://www.pornhub.com portion
domain = 'https://www.pornhub.com'

# Everything AFTER the pornhub.com url
search_criteria = '/video?c=8'

page_number_cat = '&page='

# Number of pages to scroll through
max_pages_to_crawl = 10

sub_url = domain + search_criteria + page_number_cat

page_range = range(1,max_pages_to_crawl + 1)

for current_page in page_range:
    url = sub_url + str(current_page)

    req = Request(url, headers = {"User-Agent": "Mozilla/5.0"})
    response = urlopen(req)

    soup = bs.BeautifulSoup(response,'lxml')

    found_links = soup.find_all("div", {"class":"thumbnail-info-wrapper clearfix"})

    for current_link in found_links:
        for video_found in current_link.find_all('a', {"class":""}):
            vids = video_found.get('href')
            usable_url = re.match("\/view_video.*", vids)
            if usable_url:
                print(domain + vids, file = full_list)

full_list.close()
