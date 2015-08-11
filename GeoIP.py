#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import html

r = requests.get(r'http://jsonip.com')
ip = r.json()['ip']
resp = requests.get("http://whatismyipaddress.com/ip/" + ip)
doc = html.fromstring(resp.text)
country_xp = '//*[@id="section_left_3rd"]/table/tr[1]/td[1]/text()[1]'
region_xp = '//*[@id="section_left_3rd"]/table/tr[2]/td[1]/text()[1]'
city_xp = '//*[@id="section_left_3rd"]/table/tr[3]/td[1]/text()[1]'
print ip
print doc.xpath(country_xp)[0]
print doc.xpath(region_xp)[0]
print doc.xpath(city_xp)[0]
