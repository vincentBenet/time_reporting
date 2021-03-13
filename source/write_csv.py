import os
import csv
import datetime

def main(dir, datas):
    path = os.path.join(dir, "{0} - consolidate_team_timekeepings.csv".format(datetime.datetime.today().strftime('%d-%m-%Y')))
    lines = []
    with open(path, 'w') as myfile:
        wr = csv.writer(myfile)
        for data in datas:
            print(data)
            wr.writerow(data)

