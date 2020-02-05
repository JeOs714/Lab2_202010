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
from Sorting import insertionsort as sort
from DataStructures import listiterator as it
from ADT import list as slt
import copy 
from App import app as apl


class insertionSortTest (unittest.TestCase):

    #list_type = 'ARRAY_LIST'
    list_type = 'SINGLE_LINKED_LIST'

    def setUp (self):

        self.lst = slt.newList(apl.loadCSVFile("Data/SmallMoviesDetailsClened.csv"))

    def tearDown (self):
        pass

    def less( self, element1, element2):
        if int(element1['vote_count']) <  int(element2['vote_count']):
            return True
        return False
    
    def greater( self, element1, element2):
        if int(element1['book_id'])  > int(element2['book_id']):
            return True
        return False

    def verifySorting(self, lista, compFunction):
        iterator = it.newIterator(lista)
        count=0
        prev_element=None
        while  it.hasNext(iterator):
            element = it.next(iterator)
            #result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            #print (result)
            if count > 0:
                if compFunction(element, prev_element):
                    return False
            count+=1
            prev_element=copy.copy(element)
        return True

    def test_randomElements (self):
        """
         Lista con elementos en orden aleatorio
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book5)
        slt.addFirst (self.lst, self.book6)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book10)
        slt.addFirst (self.lst, self.book1)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book8)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book7)
        slt.addFirst (self.lst, self.book9)
     
        print ("Random list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            #result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            #print (result)
        print ("Sorting ....")
        sort.insertionSort (self.lst, self.less)
        self.assertTrue(self.verifySorting(self.lst, self.less))
    

    def test_invertedElements (self):
        """
        Lista ordenada inversamente
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book1)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book5)
        slt.addFirst (self.lst, self.book6)
        slt.addFirst (self.lst, self.book7)
        slt.addFirst (self.lst, self.book8)
        slt.addFirst (self.lst, self.book9)
        slt.addFirst (self.lst, self.book10)

        print ("Inverted list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        count=0
        while  it.hasNext(iterator):
            element = it.next(iterator)
            count+=1
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.insertionSort (self.lst, self.less)
        self.assertTrue(self.verifySorting(self.lst, self.less))

    def test_orderedElements (self):
        """
        Lista ordenada
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book10)
        slt.addFirst (self.lst, self.book9)
        slt.addFirst (self.lst, self.book8)
        slt.addFirst (self.lst, self.book7)
        slt.addFirst (self.lst, self.book6)
        slt.addFirst (self.lst, self.book5)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book1)

        print ("ordered list:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.insertionSort (self.lst, self.less)
        self.assertTrue(self.verifySorting(self.lst, self.less))

    def test_oneElement (self):
        """
        Un elemento
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book1)

        print ("one element:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.insertionSort (self.lst, self.less)
        iterator = it.newIterator(self.lst)
        self.assertTrue(self.verifySorting(self.lst, self.less))



    def test_repeatedElements (self):
        """
           Con muchos elementos en la lista
        """
        self.lst = slt.newList(self.list_type)
        slt.addFirst (self.lst, self.book5)
        slt.addFirst (self.lst, self.book6)
        slt.addFirst (self.lst, self.book14)
        slt.addFirst (self.lst, self.book3)
        slt.addFirst (self.lst, self.book13)
        slt.addFirst (self.lst, self.book10)
        slt.addFirst (self.lst, self.book1)
        slt.addFirst (self.lst, self.book12)
        slt.addFirst (self.lst, self.book2)
        slt.addFirst (self.lst, self.book8)
        slt.addFirst (self.lst, self.book4)
        slt.addFirst (self.lst, self.book11)
        slt.addFirst (self.lst, self.book7)
        slt.addFirst (self.lst, self.book9)

        print ("Repeated elements:----------------------------------------------------")
        iterator = it.newIterator(self.lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            result = "".join(str(key) + ": " + str(value) + ",  " for key, value in element.items())
            print (result)
        print ("sorting ....")
        sort.insertionSort (self.lst, self.less)
        self.assertTrue(self.verifySorting(self.lst, self.less))




if __name__ == "__main__":
    unittest.main()
