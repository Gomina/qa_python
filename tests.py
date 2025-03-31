import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
@@ -18,7 +19,136 @@ def test_add_new_book_add_two_books(self):

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #тесты на количество символов
    @pytest.mark.parametrize('name, expected_result',
                            [
                                ('', False),
                                ('1', True),
                                ('Мастер и Маргарита18', True),
                                ('Лев, колдунья и платяной шкаф: Хроник39', True),
                                ('Сквозь лабиринты времени: путь к себе-40', True),
                                ('Эхо забытых голосов: шепоты из прошлого41', False),
                                ('Тайны бескрайних горизонтов: Путешествие в мечту-51', False)
                            ])

    def test_add_new_book_with_different_title(self,name, expected_result):
        collector = BooksCollector()
        collector.add_new_book(name)
        actual_result = len(collector.books_genre) > 0
        assert actual_result == expected_result

    # невозможно добавить книгу, если она уже есть в books_genre
    def test_add_new_book_if_already_addad(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    #установить жанр книги
    @pytest.mark.parametrize('name, genre, expected_result',
                             [
                                 ('1+1','Комедии', True),
                                 ('1+1', 'Мелодрама', False),
                                 ('Кто, если не я', 'Фантастика', False),
                                 ('Кто, если не я', 'Мелодрама', False),
                             ])

    def test_appropriation_of_genre(self, name, genre, expected_result):
        collector = BooksCollector()
        collector.books_genre = {'1+1': None}
        collector.set_book_genre(name, genre)
        actual_result = name in collector.books_genre and collector.books_genre[name] == genre
        assert actual_result == expected_result

    #вывод жанра книги по её имени
    @pytest.mark.parametrize('name, genre, expected_result',
                             [
                                 ('Чемодан', 'Комедии', True),
                                 ('Война миров', 'Фантастика', True),
                                 ('Книга белой смерти', 'Ужасы', True),
                                 ('Ходячий замок', 'Мультфильмы', True),
                                 ('Легенды ночных стражей', None, True),
                                 ('Трое в лодке, не считая собаки', 'Комедии', False),
                                 ('«Гордость и предубеждение', 'Драма', False)
                             ])

    def test_name_book_deduce_genre(self, modified_books_genre, name, genre, expected_result):
        collector = modified_books_genre
        collector.set_book_genre(name, genre)
        actual_result = name in collector.books_genre and collector.books_genre[name] == genre
        assert actual_result == expected_result

    #вывод списка книг с определенным жанром
    def test_name_book_deduce_genre(self, modified_books_genre):
        collector = modified_books_genre
        result = collector.get_books_with_specific_genre('Фантастика')
        assert len(result) == 2
        assert set(result) == {'Война миров', 'Ходячий замок'}

    #вывод текущего словаря
    def test_dictionary_contents(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        books_genre = collector.get_books_genre()
        book_name = set(books_genre.keys())
        assert book_name == {'Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'}

    #возвращает книги, которые подходят детям
    def test_books_for_children(self, modified_books_genre):
        collector = modified_books_genre
        result = collector.get_books_for_children()
        assert len(result) == 3
        assert set(result) == {'Чемодан', 'Война миров', 'Ходячий замок'}

    # добавление книг в избранное
    def test_add_to_favorites(self, modified_books_genre):
        collector = modified_books_genre
        collector.add_book_in_favorites('Чемодан')
        collector.add_book_in_favorites('Война миров')
        collector.add_book_in_favorites('Война миров')
        collector.add_book_in_favorites('123123123123')
        favorites = collector.favorites
        assert len(favorites) == 2
        assert set(favorites) == {'Чемодан', 'Война миров'}

    #удаление книг из избранного
    def test_remove_from_favorites(self):
        collector = BooksCollector()
        collector.favorites = ['Чемодан', 'Война миров', 'Книга белой смерти']

        collector.delete_book_from_favorites('Чемодан')
        collector.delete_book_from_favorites('Война миров')
        collector.delete_book_from_favorites('Война миров')
        collector.delete_book_from_favorites('Ходячий замок')

        favorites = collector.favorites
        assert len(favorites) == 1
        assert favorites == ['Книга белой смерти']

    #получить список избранных книг
    def test_list_of_favorites_books(self, modified_books_genre):
        collector = modified_books_genre
        collector.favorites = []
        favorites = collector.favorites
        collector.get_list_of_favorites_books()
        assert len(favorites) == 0

        collector.add_book_in_favorites('Чемодан')
        collector.get_list_of_favorites_books()
        assert len(favorites) == 1
        assert favorites == ['Чемодан']

        collector.add_book_in_favorites('Ходячий замок')
        collector.delete_book_from_favorites('Чемодан')
        assert len(favorites) == 1
        assert favorites == ['Ходячий замок']

        collector.delete_book_from_favorites('Ходячий замок')
        assert len(favorites) == 0
