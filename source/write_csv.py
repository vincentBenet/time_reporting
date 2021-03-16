import os
import csv
import datetime

def main(dir, datas):
    print("_" * 50)
    print("Start script 'write_csv.py'")
    path = os.path.join(dir, "{0} - consolidate_team_timekeepings.csv".format(datetime.datetime.today().strftime('%d-%m-%Y')))
    lines = []
    with open(path, 'w') as myfile:
        wr = csv.writer(myfile, lineterminator='\n', delimiter=';')
        wr.writerow(["Category", "Date", "Name", "Client", "Task", "Offer", "Hours"])
        for data in datas:
            wr.writerow(data)
            print("data: " + str(data))
    print("Finish script 'write_csv.py'")
