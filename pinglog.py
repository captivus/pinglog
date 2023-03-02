'''
TODO:
* Wrap all of this in functions
* Add start and end date parameters as filters
* Calculate uptime in between outages
* Add webserver target as parameter
* Create python command line utility
* Add dates for min and max outage
'''

import datetime
import os

# CONFIG
INPUT_LOGFILE = "./logs/output_pinglog.txt"
MIN_OUTAGE_THRESHOLD = 90
OUTPUT_SUMMARY_FILE = 'pinglog_summary.txt'
OUTPUT_OUTAGES_FILE = 'pinglog_outages.csv'

# initialize variables
MIN_OUTAGE_THRESHOLD = datetime.timedelta(seconds=MIN_OUTAGE_THRESHOLD)
total_time = datetime.timedelta(0)
start_time = None
last_time = None
outage_time = 0
outages = {}
line_counter = 0
begin_time = datetime.datetime.now()
FILE_SIZE = 0.0

# read file and split into lines
with open(INPUT_LOGFILE, "r") as f:
    lines = f.readlines()

FILE_SIZE = round(os.path.getsize(INPUT_LOGFILE) / (1024 * 1024), 2)

# loop through lines
for line in lines:
    line_counter += 1
    if "Request timeout" in line:
        # if this is the first request timeout line in a block, record the start time
        if start_time is None:
            start_time = datetime.datetime.strptime(line[:28], "%a %b %d %H:%M:%S %Z %Y")
        last_time = datetime.datetime.strptime(line[:28], "%a %b %d %H:%M:%S %Z %Y")
    elif "64 bytes from" in line:
        # we're back online, so calculate outage time and reset start_time
        if start_time is not None:
            outage_time = last_time - start_time
            outages[start_time] = outage_time
            #print(f'Outage from {start_time} to {last_time} ({outage_time}')
            start_time = None

# if we reached the end of the file while still in a block of request timeouts,
# add the time difference to the total time
if start_time is not None:
    outage_time = last_time - start_time
    outages[start_time] = outage_time

# calculate summary data
start_date = datetime.datetime.strptime(lines[0][:28], "%a %b %d %H:%M:%S %Z %Y")
end_date = datetime.datetime.strptime(lines[-1][:28], "%a %b %d %H:%M:%S %Z %Y")
outages = { k: v for k, v in outages.items() if v > MIN_OUTAGE_THRESHOLD }

num_outages = len(outages)
min_outage = min(outages.values())
max_outage = max(outages.values())
most_recent_outage_date = sorted(outages.keys())[-1]
most_recent_outage_duration = outages[most_recent_outage_date]
end_time = datetime.datetime.now()
processing_time = end_time - begin_time

# create summary of outages
summary = f'''Start Date:     {start_date}
End Date:       {end_date}
Days:           {(end_date - start_date).days}
# of Outages:   {num_outages}
Min Outage:     {min_outage}
Max Outage:     {max_outage}
Recent Outage:  {most_recent_outage_date}: {most_recent_outage_duration}
Threshold:      {MIN_OUTAGE_THRESHOLD}
Processed {line_counter:,} records ({FILE_SIZE:,} MB) in {processing_time}
'''


# print the total time for request timeouts
print(f'\n{summary}')
# write summary to file
with open(OUTPUT_SUMMARY_FILE, "w") as f:
    f.write(summary)
print(f'Summary written to {OUTPUT_SUMMARY_FILE}')

# write outages to CSV
with open(OUTPUT_OUTAGES_FILE, "w") as f:
    f.write("Start Time,Outage Duration\n")
    for time, duration in outages.items():
        f.write(f"{time},{duration}\n")
print(f'Outages written to {OUTPUT_OUTAGES_FILE}')