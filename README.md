# tarpit_log_to_csv
Simple Python script, that converts the .log file from ssh-tarpit to an readable .csv file for further investigation

Just put the tarpit.log file in the same directory as the log_to_csv.py file and run it via
`python3 log_to_csv.py`

Only rows containing "connected" or "disconnected" will be converted. The CSV will look like this:


datetime | ip | port | status
-------- | ---| -----| ------
01.01.1970 | 127.0.0.1 | 22 | connected
