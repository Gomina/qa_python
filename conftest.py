import pytest
from main import BooksCollector

# словарь books_genre с книгами
@pytest.fixture
def modified_books_genre():
    collector = BooksCollector()  # Создаем экземпляр класса BooksCollector
    collector.books_genre = {
        'Чемодан': 'Комедии',
        'Война миров': 'Фантастика',
        'Книга белой смерти': 'Ужасы',
        'Ходячий замок': 'Фантастика',
        'Легенды ночных стражей': None
    }
    return collector
