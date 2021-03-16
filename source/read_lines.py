import os

def main(files, csv_list):
    print("_" * 50)
    print("Start script 'read_lines.py'")
    datas = []
    for i, file in enumerate(files):
        print("file: " + str(file))
        for row in file:
            filename_list = os.path.basename(csv_list[i]).split(" - ")
            data = {
                "year": filename_list[0],
                "month": filename_list[1],
                "name": "".join(filename_list[2:])[:-len(".csv")],
                "category": row[0],
                "theme": row[1],
                "tache": row[2],
                "offre": row[3],
                "dates": row[4:35]
            }
            print("data: " + str(data))
            datas.append(data)
    print("Finish script 'read_lines.py'")
    print("datas: " + str(datas))
    return datas