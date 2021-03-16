def main(datas):
    print("_" * 50)
    print("Start script 'processing.py'")
    datas_transformed = []
    for data in datas:
        for i, date in enumerate(data["dates"]):
            if date == "":
                continue
            row = [
                data["category"],                
                "{0}/{1}/{2}".format(("00" + str(i + 1))[-2:], data["month"], data["year"]),
                data["name"],
                data["theme"],
                data["tache"],
                data["offre"],
                date
            ]
            print("row: " + str(row))
            datas_transformed.append(row)
    print("Finish script 'processing.py'")
    print("datas_transformed: " + str(datas_transformed))
    return datas_transformed