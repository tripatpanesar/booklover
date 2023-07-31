
import pandas as pd

class BookLover:
        
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        
        if book_list is None:
            book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        self.book_list = book_list

    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].values:
            print('This book has already been read.')
        else:
            new = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new], ignore_index = True)
            self.num_books += 1

    def has_read(self, book_name):
        read = book_name in self.book_list['book_name'].values
        return read

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        favs = self.book_list[self.book_list['book_rating'] > 3]
        return favs
