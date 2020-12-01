from pymongo import MongoClient
from decouple import config
import re

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def search_by_title(title):
    arr = []
    for document in db.news.find(
        {"title": {"$regex": title, "$options": "-i"}}
    ):
        title = document["title"]
        url = document["url"]
        arr.append((title, url))
    return arr


def search_by_date(date):
    match = re.search(
        "^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$", date
    )
    if not match:
        raise ValueError("Data inválida")
    arr = []
    for document in db.news.aggregate(
        [{"$match": {"timestamp": {"$regex": date}}}]
    ):
        title = document["title"]
        url = document["url"]
        arr.append((title, url))
    return arr


def search_by_source(source):
    arr = []
    for document in db.news.find(
        {"sources": {"$elemMatch": {'$regex': source, "$options": "i"}}}
    ):
        title = document["title"]
        url = document["url"]
        arr.append((title, url))
    return arr


def search_by_category(category):
    arr = []
    for document in db.news.find(
        {"categories": {"$elemMatch": {'$regex': category, "$options": "i"}}}
    ):
        title = document["title"]
        url = document["url"]
        arr.append((title, url))
    return arr
