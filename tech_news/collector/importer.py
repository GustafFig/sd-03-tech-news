import csv
from tech_news.collector.csv_helpers import validate_filepath, EXP_HEADERS


def csv_importer(filepath):
    filename = validate_filepath(filepath)
    try:
        with open(filepath, "r") as file:
            data = csv.DictReader(file, delimiter=";")
            if data.fieldnames != EXP_HEADERS:
                raise ValueError("Headers invalidos")
            info = [
                {key: value for key, value in line.items()} for line in data
            ]

    except FileNotFoundError:
        raise ValueError(f"Arquivo {filename} não encontrado")
    else:
        return info


if __name__ == "__main__":
    csv_importer("correct.csv")
