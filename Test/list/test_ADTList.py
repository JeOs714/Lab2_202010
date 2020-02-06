"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """


import unittest 
import config 
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from App import app as apl


class insertionSortTest (unittest.TestCase):

    def setUp (self):
        
        self.movie1 = {'movie_id':'2', 'original_title':'Ariel', 'vote_count':'40', 'vote_average':'7.1'}
        self.movie2 = {'movie_id':'3', 'original_title':'Varjoja paratiisissa', 'vote_count':'32','vote_average':'7.0'}
        self.movie3 = {'movie_id':'5', 'original_title':'Four Rooms', 'vote_count':'485', 'vote_average':'6.5'}
        self.movie4 = {'movie_id':'6', 'original_title':'Judgment Night', 'vote_count':'69', 'vote_average':'6.5'}
        self.movie5 = {'movie_id':'8', 'original_title':'Life in Loops (A Megacities RMX)', 'vote_count':'4', 'vote_average':'6.4'}
        self.movie6 = {'movie_id':'9', 'original_title':'Sonntag im August', 'vote_count':'2', 'vote_average':'5.3'}

    def tearDown (self):
        pass

    def test_arrayAddFirst (self):
        """
         Lista con elementos en orden aleatorio
        """
        self.lst = lt.newList('ARRAY_LIST')
        lt.addFirst (self.lst, self.movie1)
        self.assertEqual (lt.size(self.lst), 1)
        lt.addFirst (self.lst, self.movie2)
        self.assertEqual (lt.size(self.lst), 2)
        book = lt.firstElement(self.lst)
        self.assertDictEqual (book, self.movie2)

    def test_listAddFirst (self):
        """
         Lista con elementos en orden aleatorio
        """
        self.lst = lt.newList()
        lt.addFirst (self.lst, self.movie1)
        self.assertEqual (lt.size(self.lst), 1)
        lt.addFirst (self.lst, self.movie2)
        self.assertEqual (lt.size(self.lst), 2)
        book = lt.firstElement(self.lst)
        self.assertDictEqual (book, self.movie2)


if __name__ == "__main__":
    unittest.main()
