
Good-enough extraction of TPP EHR records to a local sqlite database, for inspection in datasette

Totally not very usable for anyone else in current state, so these notes are just to remind me:


- Log into systmone online. Inspect network headers. Extract JSESSIONID and UID to variables at the top of get_record.py
- Try browsing your record, and extract UUID from a request header there
- in the `data` dict, change DateFrom and DateTo as required. Also the `for n in range(1, 51)` line; the second number is the page index of the oldest record, you might need to change that too if you have a lot of records
- Run `get_record.py` to grab entire get_record
- Run `parse_html.py` to write it to a sqlite table and set up datasette (see the final lines)
- datasette records.db -o
