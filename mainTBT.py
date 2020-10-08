import json
import os
import time

from tbt import tbt
from tbt.nrd_code import nrd

cwd = os.getcwd()
inputJsonFile = cwd + "\\Input\\input.json"

try:
    file = open(inputJsonFile)
    data = json.load(file)
    inputExcelFileName = data["inputFileName"]
    is_cmg = data["type_cmg"]
    excel_file_path = cwd + "\\Input\\" + inputExcelFileName
    print("Input Excel file is: " + excel_file_path)
    if is_cmg:
        tbt.read_excel_file(excel_file_path)
        time.sleep(5)
    else:
        if excel_file_path.lower().__contains__("nrd"):
            nrd.read_excel_file(excel_file_path)
            time.sleep(5)
        else:
            print("Please provide valid input for NRD")
except:
    print("Please enter valid input file name")
    time.sleep(5)

"""date_time_str = '2020-09-22 01:15:59.081538'
start = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
expire = datetime.datetime.now()

if expire > start and expire.month - start.month <= 1:
    try:
        file = open(inputJsonFile)
        data = json.load(file)
        inputExcelFileName = data["inputFileName"]
        is_cmg = data["type_cmg"]
        excel_file_path = cwd + "\\Input\\" + inputExcelFileName
        print("Input Excel file is: " + excel_file_path)
        if is_cmg:
            tbt.read_excel_file(excel_file_path)
            time.sleep(5)
        else:
            if excel_file_path.lower().__contains__("nrd"):
                nrd.read_excel_file(excel_file_path)
                time.sleep(5)
            else:
                print("Please provide valid input for NRD")
    except:
        print("Please enter valid input file name")
        time.sleep(5)
else:
    print("Your license has expired.")
    time.sleep(5)
    sys.exit()"""
