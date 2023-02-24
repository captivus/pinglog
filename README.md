# pinglog -- an internet connectivity logging utility
This shell script pings a web server and logs responses to determine local Internet downtime.
The Python program analyzes these logs to identify outages and provide summary data.

## Instructions
* Run pinglog.sh on your local machine and let it keep running in the background
* Run pinglog.py on your logfile at any time to generate summary data on local Internet outages.

## Example Summary Output
Start Date:     2022-08-15 11:19:14
End Date:       2023-02-23 10:08:40
Days:           191
\# of Outages:   65
Min Outage:     0:01:33
Max Outage:     11:00:42
Threshold:      0:01:30

## Example Outage Log
Start Time	Outage Duration
8/29/2022 13:13	00:01:45
8/31/2022 17:18	00:01:42
9/1/2022 21:16	00:01:42
9/5/2022 09:41	00:01:40
9/5/2022 11:24	00:01:45
9/20/2022 17:36	06:43:18
9/21/2022 00:20	00:06:32
9/21/2022 00:27	00:06:05
9/21/2022 00:33	00:02:42
9/21/2022 00:38	00:55:57
9/21/2022 03:36	00:01:43
9/22/2022 14:52	00:01:45