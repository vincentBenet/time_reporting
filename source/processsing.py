

def main(datas):
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
            datas_transformed.append(row)
    return datas_transformed