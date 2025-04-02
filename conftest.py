import pytest
from main import BooksCollector

#создание объекта BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

# словарь books_genre с книгами
@pytest.fixture
def modified_books_genre(collector):
    collector.books_genre = {
        'Чемодан': 'Комедии',
        'Война миров': 'Фантастика',
        'Книга белой смерти': 'Ужасы',
        'Ходячий замок': 'Фантастика',
        'Легенды ночных стражей': None
    }
    return collector