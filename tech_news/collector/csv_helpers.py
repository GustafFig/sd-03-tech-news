EXP_HEADERS = [
    "url",
    "title",
    "timestamp",
    "writer",
    "shares_count",
    "comments_count",
    "summary",
    "sources",
    "categories",
]


def validate_filepath(filepath):
    if not filepath.endswith(".csv"):
        raise ValueError("Formato invalido")
    return filepath.split("/")[-1]
