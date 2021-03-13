import extract
import read_csv
import write_csv
import read_lines
import processsing

if __name__ == "__main__":
    dir, csv_list = extract.main()
    files = read_csv.main(csv_list)
    datas = read_lines.main(files, csv_list)
    datas_transformed = processsing.main(datas)
    write_csv.main(dir, datas_transformed)
    