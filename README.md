# airflow-log-analyzer
A simple python script to analyze and return ERROR messages within Airflow log files.

## Execution
This script is run via the command line. It will return all of the log errors found within a specified Airflow log directory.  

When executing this script, it takes a single argument, the name of the Airflow DAG directory for which you would like to view ERROR messages within it's logs.   

The DAG's logs I am inspecting is called 'marketvol', so to execute this script and see ERRORs within it's log files, simply type:  

```python3 log_analyzer.py marketvol```


![results](/screenshots/error_logs.png)
