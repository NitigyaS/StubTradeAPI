import requests
import csv
import json
from datetime import  datetime
import sys




def create_pay_load(row):
    json_payload = {
                    "symbol": row[0].lstrip(),
                    "series": row[1].lstrip(),
                    "date": datetime.strptime(row[2].lstrip(),'%d-%b-%Y').strftime('%Y-%m-%d'),             # formats should be: YYYY[-MM[-DD]]
                    "prev_close": row[3].lstrip(),
                    "open_price": row[4].lstrip(),
                    "high_price": row[5].lstrip(),
                    "low_price": row[6].lstrip(),
                    "last_price": row[7].lstrip(),
                    "close_price": row[8].lstrip(),
                    "average_price": row[9].lstrip(),
                    "total_traded_quantity": row[10].lstrip(),
                    "turnover": row[11].lstrip(),
                    "no_trades": row[12].lstrip(),
                    "deliverable_qty": row[13].lstrip(),
                    "percent_del_to_trade": row[14].lstrip()
                    }
    return json.dumps(json_payload)

usage_string = """
Description : The Script is used to upload CSV data of historic trades to the StubAPI
Usage : 
    python load_data.py [csv_file_name.csv]   
How to Get the CSV : 
1) visit the site https://www.nseindia.com/products/content/equities/equities/eq_security.htm
2) Enter the symbol name
3) select period to last 24 months
4) Press Get Data
5) Click on `Download file in csv format`
"""

if len(sys.argv) == 2:
    csv_file = sys.argv[1]
    url = "http://127.0.0.1:8000/tickadd/"
    print "Info : Using the default URL 'http://127.0.0.1:8000/tickadd/' "
elif len(sys.argv) == 3:
    csv_file = sys.argv[1]
    url = sys.argv[2]
else :
    print usage_string
    exit(1)

try :
    with open(csv_file, 'rb') as csvfile:
        tickreader = csv.reader(csvfile, delimiter=',', skipinitialspace=True)
        for row in tickreader:
            payload = create_pay_load(row)
            headers = {
                'content-type': "application/json"
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            print "status"
            print(response.text)

except(requests.exceptions.ConnectionError) :
    print "Error : Ensure that server is running at " +  url
except(IndexError) :
    print "Error : Ensure that CSV file " + csv_file + " has correct format"








