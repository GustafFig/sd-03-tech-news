from tech_news.database import find_news


def top_5_news():
    news = find_news()
    return news


def top_5_categories():
    """Seu código deve vir aqui"""
