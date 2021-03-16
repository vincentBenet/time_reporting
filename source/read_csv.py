import csv

def main(csv_list):
    print("_" * 50)
    print("Start script 'read_csv.py'")
    files = []
    for path in csv_list:
        lines = []
        start = False
        counter_start = 0
        print("Open file: " + str(path))
        with open(path, encoding="cp1252") as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for i, row in enumerate(reader):
                if row == []:
                    continue
                if not start:
                    if row[1] != "":
                        counter_start += 1
                    if counter_start > 3:
                        start = True
                    else:
                        continue
                if row[1] == "":
                    continue
                lines.append(row)
        files.append(lines)
        print("nb lines: " + str(len(lines)))
    print("Finish script 'read_csv.py'")
    print("files: " + str(files))
    return files
