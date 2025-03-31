# qa_python
Для проверки функциональности BooksCollector созданы следующие тесты:

1. test_add_new_book_add_two_books - тест проверяет, что в словарь books_genre книги добавляются.
2. test_add_new_book_with_different_title -тест проверяет, что в словарь books_genre можно добавить книги с названием 1, 18, 39 и 40 символов. А название книги с 0, 41 и 51 символом добавить нельзя.
3. test_add_new_book_if_already_addad - тест, проверяет, что нельзя в словарь books_genre добавить дубликат книги (т.е. с таким же названием, как книга уже находящаяся в словаре).
4. test_appropriation_of_genre - тест проверяет, что книге находящейся в  словаре books_genre можно присвоить жанр, если он есть в списке genre. Если жанра в списке genre нет, жанр к книге не присваивается.
5. test_name_book_deduce_genre - тест проверяет, что указав название книги можно вывести её жанр.
6. test_name_book_deduce_genre - тест проверяет, что можно вывести все книги определенного жанра, находящиеся в словаре books_genre.
7. test_dictionary_contents - тест проверяет, что можно вывести актуальный список книг, находящихся в словаре books_genre
8. test_books_for_children - тест проверяет, что можно вывести список книг, подходящих детям. Т.е. книги всех жанров, кроме жанров 'Ужасы' и 'Детективы'.
9. test_add_to_favorites - в список избранное favorites можно добавлять книги из словаря. Дубликат добавленный книги добавить нельзя. Книги не из словаря не добавляются.
10. test_remove_from_favorites - из списка избранное favorites можно удалять книги.
11. test_list_of_favorites_books - список избарнных книг выводиться, как после удаления, так и после добавления книг. А также в случае если книг в избранном нет. 