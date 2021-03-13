import os

def main(files, csv_list):
    datas = []
    
    for i, file in enumerate(files):
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
            datas.append(data)
    # print(datas)
    return datas