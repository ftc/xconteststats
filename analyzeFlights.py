import json
import argparse

def forEachFlight(files, functionToApply):
    for file in files:
        f = open(file,'r')
        file_lines = f.read()
        parsed = json.loads(file_lines)
        for flight in parsed['items']:
            functionToApply(flight)

def getFlyingDays(files):
    daySet = set()

    def toApply(flight):
        time_claim = flight['timeClaim']
        date_string = time_claim.split('T')[0]
        daySet.add(date_string)
    forEachFlight(files,toApply)
    return len(daySet)

def getFlightsAtEachSite(files):
    sites = {}
    flightIds = set()
    def toApply(flight):
        if(flight['id'] in flightIds):
            return # don't double count flights
        flightIds.add(flight['id'])
        siteName = flight['takeoff']['name']
        if(siteName not in sites):
            sites[siteName] = 0
        sites[siteName] = sites[siteName] + 1
    forEachFlight(files,toApply)
    return sites



def main():
    parser = argparse.ArgumentParser(description="A utility to extract statistics from XContest " \
    "flight logs")
    parser.add_argument("-f", "--input_file", help="""Path to the json flight logs downloaded
    "from XContest.  Separate files with spaces and surround with quotes (e.g. python3 analyzeFlights.py
                         -f "flights.ShawnKM.world2025.json flights.ShawnKM.world2024.json")""",
                         type=str, required=True)
    args = parser.parse_args()
    inputFiles = args.input_file.split(' ')
    print(f"Input file: {args.input_file}")
    print(f"Flying days: {getFlyingDays(inputFiles)}")
    siteFlightCount = getFlightsAtEachSite(inputFiles)
    print("Flights at each flying site:")
    for site in siteFlightCount:
        print(f"  {site}:{siteFlightCount[site]}")


if __name__ == "__main__":
    main()
