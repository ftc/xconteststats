Usage:
Install python3

Running:
-------

Show help.

```
python3 analyzeFlights.py -h
```

Get statistics on a flight log:

Download the json file with your flights.  My flights -> Export: JSON

Run on each downloaded file separated with spaces.

```
s@Surface7:~/flightlog_analysis$ python3 analyzeFlights.py -f "flights.ShawnKM.world2025.json flights.ShawnKM.world2024.json"
Input file: flights.ShawnKM.world2025.json flights.ShawnKM.world2024.json
Flying days: 76
```