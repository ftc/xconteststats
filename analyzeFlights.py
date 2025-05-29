import json
import argparse

def getFlyingDays(files):
    daySet = set()
    for file in files:
        f = open(file,'r')
        file_lines = f.read()
        parsed = json.loads(file_lines)
        for flight in parsed['items']:
            time_claim = flight['timeClaim']
            date_string = time_claim.split('T')[0]
            daySet.add(date_string)
        return len(daySet)

def main():
    parser = argparse.ArgumentParser(description="A utility to extract statistics from XContest " \
    "flight logs")
    parser.add_argument("-f", "--input_file", help="""Path to the json flight logs downloaded
    "from XContest.  Separate files with spaces and surround with quotes (e.g. python3 analyzeFlights.py
                         -f "flights.ShawnKM.world2025.json flights.ShawnKM.world2024.json")""",
                         type=str, required=True)
    args = parser.parse_args()
    print(f"Input file: {args.input_file}")
    print(f"Flying days: {getFlyingDays(args.input_file.split(' '))}")
if __name__ == "__main__":
    main()
