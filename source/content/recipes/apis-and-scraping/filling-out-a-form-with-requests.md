---
title: Filling out a Web Form with Requests
ordernum: 4000
---



Example: http://wildlife.faa.gov/database.aspx


~~~py
browser = mechanicalsoup.Browser()
page = browser.get("http://wildlife.faa.gov/database.aspx")
form = page.soup.find("#ctl00_ContentPlaceHolder1_UpdatePanel2")
