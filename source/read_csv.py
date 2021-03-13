import csv

def main(csv_list):
    files = []
    for path in csv_list:
        lines = []
        # print("path: " + str(path))
        start = False
        counter_start = 0
        with open(path, encoding="utf-8") as csvfile:
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
        # print("nb lines: " + str(len(lines)))
    # print("nb files: " + str(len(files)))
    return files