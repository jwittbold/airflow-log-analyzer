# airflow-log-analyzer
A simple python script to analyze and return errors within Airflow log files.

## Execution
This script is run via the command line. It will return all of the log errors found within a specified Airflow log directory.
It takes a single argument, the name of the Airflow DAG directory for which you would like to view logs with errors.  

The DAG logs I am inspecting is called 'marketvol', so to execute this script and see ERRORs within it's log files, simply type:  

```python3 log_analyzer.py marketvol```

![results](/screenshots/log_errors.png)
