import glob
import sys


base_log_dir = '/Users/jackwittbold/airflow/logs'

def analyze_file():
    
    # dag_directory is passed in as first argument when running program via command line, 
    # corresponds to the DAG for which you would like to view logs containing ERRORs 
    dag_directory = sys.argv[1]

    file_list = glob.glob(f'{base_log_dir}/{dag_directory}/*/*/*.log')

    error_count = 0
    error_lines = []

    for file in file_list:

        with open(file, 'r') as log_file:
            for line in log_file:
                if 'ERROR' in line:
                    error_count += 1
                    error_lines.append(line)
                    

    print(f'\nTotal number of errors: {error_count}\n')

    for count, value in enumerate(error_lines):
        print(value)
    
    return error_count, error_lines


if __name__ == '__main__':

    analyze_file()