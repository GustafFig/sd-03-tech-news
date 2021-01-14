import csv
from tech_news.database import find_news
from tech_news.collector.csv_helpers import validate_filepath, EXP_HEADERS


def csv_exporter(filepath):
    validate_filepath(filepath)

    with open(filepath, "w") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(EXP_HEADERS)
        for document in find_news():
            dict = [
                document["url"],
                document["title"],
                document["timestamp"],
                document["writer"],
                str(document["shares_count"]),
                str(document["comments_count"]),
                document["summary"],
                ",".join(document["sources"]),
                ",".join(document["categories"]),
            ]
            writer.writerow(dict)
