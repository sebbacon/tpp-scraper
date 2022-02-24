"""Gets full patient record, page-by-page, and writes to html/ subfolder

"""
import requests
from bs4 import BeautifulSoup

JSESSIONID = "9BF45DCEBF79F0F61B0AD3B342006E24"
UID = "3be69989ca2665fa6b32855a3f98f20d"
UUID = "NDYzMzT1NDIyMDQ5ODAwMzk2ODQ5MDkx4TczNzkwNjg1Mjk2NjQ="
cookies = {
    "JSESSIONID": JSESSIONID,
    "CookieTest": "CookieTest",
    "UID": UID,
}

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.5",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://systmonline.tpp-uk.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://systmonline.tpp-uk.com/2/PatientRecord",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
}

data = {
    "UUID": UUID,
    "DateFrom": "01/08/2009",
    "DateTo": "24/02/2022",
    "StaffMember": "",
    "DataType": "",
    "TextSearch": "",
    "Search": "",
    "Page1": "",
    "Page3": "",
    "Page4": "",
    "Page5": "",
    "Page6": "",
    "Page7": "",
    "Page8": "",
    "Page9": "",
    "Page10": "",
    "Page11": "",
    "Page12": "",
    "Page13": "",
    "Page14": "",
    "Page15": "",
    "Page16": "",
    "Page17": "",
    "Page18": "",
    "Page19": "",
    "Page20": "",
    "Page21": "",
    "Page22": "",
    "Page23": "",
    "Page24": "",
    "Page25": "",
    "Page26": "",
    "Page27": "",
    "Page28": "",
    "Page29": "",
    "Page30": "",
    "Page31": "",
    "Page32": "",
    "Page33": "",
    "Page34": "",
}

for n in range(1, 51):
    d = data.copy()
    d[f"Page{n}"] = f"Page{n}"
    response = requests.post(
        "https://systmonline.tpp-uk.com/2/PatientRecord",
        headers=headers,
        cookies=cookies,
        data=d,
    )
    with open(f"html/page{n}.html", "w") as f:
        f.write(response.text)
