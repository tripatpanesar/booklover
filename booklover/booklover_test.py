#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:15:52 2023

@author: tripatpanesar
"""

import unittest
from booklover import BookLover


import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        person = BookLover('Trip','tp6mt@virginia.edu','Comedy')
        person.add_book('Diary of a Wimpy Kid 1', 5)
        self.assertTrue(person.has_read('Diary of a Wimpy Kid 1'))
    def test_2_add_book(self):
        person = BookLover('Trip','tp6mt@virginia.edu','Comedy')
        person.add_book('Diary of a Wimpy Kid 1', 5)  
        person.add_book('Diary of a Wimpy Kid 1', 5)                
        book_count = len(person.book_list['book_name'])  
        self.assertEqual(book_count, 1)            
    def test_3_has_read(self): 
        person = BookLover('Trip','tp6mt@virginia.edu','Comedy')
        person.add_book('Magic Tree House', 4)
        self.assertTrue(person.has_read('Magic Tree House'))
    def test_4_has_read(self): 
        person = BookLover('Trip','tp6mt@virginia.edu','Comedy')
        self.assertFalse(person.has_read('Romeo and Juliet'))
    def test_5_num_books_read(self): 
        person = BookLover('Trip','tp6mt@virginia.edu','Comedy')
        person.add_book('Diary of a Wimpy Kid 2', 5)
        person.add_book('Captain Underpants', 5)
        person.add_book('Othello', 1)
        self.assertEqual(person.num_books_read(), 3)
    def test_6_fav_books(self):
        person = BookLover('Trip','tp6mt@virginia.edu','Comedy')
        person.add_book('Diary of a Wimpy Kid 2', 5)
        person.add_book('Captain Underpants', 5)
        person.add_book('Othello', 1)
        person.add_book('Judy Bloom', 1) 
        fav_books = person.fav_books()
        self.assertTrue((fav_books['book_rating'] > 3).all())
                
if __name__ == '__main__':
    unittest.main(verbosity=3)
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(BookLoverTestSuite))

    with open('booklover_results.txt', 'w') as file:
        runner = unittest.TextTestRunner(stream=file, verbosity=2)
        test_results = runner.run(test_suite)
    
