# pinglog - a dumb Internet connectivity logging utility
This shell script pings a web server and logs responses to determine local Internet downtime.\
The Python program analyzes these logs to identify outages and provide summary data.

## Instructions
* Run pinglog.sh on your local machine and let it keep running in the background
* Run pinglog.py on your logfile at any time to generate summary data on local Internet outages.

## Example Summary Output
Start Date:     2022-08-15 11:19:14\
End Date:       2023-02-23 10:08:40\
Days:           191\
\# of Outages:   65\
Min Outage:     0:01:33\
Max Outage:     11:00:42\
Threshold:      0:01:30


## Example Outage Log
Start Time,Outage Duration\
2022-08-29 13:13:51,0:01:45\
2022-08-31 17:18:22,0:01:42\
2022-09-01 21:16:04,0:01:42\
2022-09-05 09:41:46,0:01:40\
2022-09-05 11:24:27,0:01:45\
2022-09-20 17:36:54,6:43:18\
2022-09-21 00:20:48,0:06:32\
2022-09-21 00:27:24,0:06:05\
2022-09-21 00:33:33,0:02:42\
2022-09-21 00:38:06,0:55:57\
2022-09-21 03:36:12,0:01:43\
2022-09-22 14:52:50,0:01:45\
2022-09-22 16:52:50,0:01:41\
2022-10-01 01:05:16,0:02:25\