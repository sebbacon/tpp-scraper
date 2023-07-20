from bs4 import BeautifulSoup
import glob
import subprocess
import sqlite3
import datetime
import os

try:
    os.remove("records.db")
except FileNotFoundError:
    pass
con = sqlite3.connect("records.db")
cur = con.cursor()
# Create table
cur.execute(
    """CREATE TABLE entries
               (record_id int, date text, who text, org text, event_type text, event_text text, event_other text)"""
)
record_id = 0
for fpath in glob.glob("html/*.html"):
    with open(fpath, "r") as f:
        html = f.read()
        soup = BeautifulSoup(html, "html.parser")

        for consultation in soup.find_all(id="patientRecordCon"):
            record_id += 1
            date, who, org = [x.text for x in consultation.find_all("td")]
            # events = []
            # 29 Oct 2020
            date = datetime.datetime.strptime(date, "%d %b %Y").isoformat()
            entry = consultation
            while entry := entry.find_next_sibling():
                if entry.get("id") == "patientRecordCon":
                    # breakpoint()
                    break
                event_type, event_text, event_other = [
                    x.get_text("\n") for x in entry.find_all("td")
                ]
                cur.execute(
                    "INSERT INTO entries VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (
                        record_id,
                        date,
                        who,
                        org,
                        event_type,
                        event_text,
                        event_other,
                    ),
                )
                # events.append((event_type, event_text, event_other))
            # print(date, name, org)
            # print(events)
            # print()
            # breakpoint()
con.commit()
con.close()
subprocess.check_call(
    ["sqlite-utils", "enable-fts", "records.db", "entries", "event_text"]
)
