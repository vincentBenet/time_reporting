

def main(datas):
    datas_transformed = []
    for data in datas:
        for i, date in enumerate(data["dates"]):
            if date == "":
                continue
            row = [
                data["category"],
                data["offre"],
                data["theme"],
                data["name"],
                "{0}/{1}/{2}".format(("00" + str(i + 1))[-2:], data["month"], data["year"]),
                data["tache"],
                date
            ]
            # for i, cell in enumerate(row):
                # row[i] = str(row[i]).encode("utf-8")
            datas_transformed.append(row)
    return datas_transformed