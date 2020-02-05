"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import insertionsort as sort1
from Sorting import selectionsort as sort2
from Sorting import shellsort as sort3

from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    """
    #lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    with open(file, encoding="utf-8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader: 
            lt.addLast(lst,row)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Organizar la información")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst, directores):
    id=[]

    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        for element in directores:
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                for elemento in lst:
                    if element["id"]==elemento['id'] and float(elemento['vote_average'])>=6:
                        counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

    return counter

def less( element1, element2):
    t1_start = process_time() #tiempo inicial
    if int(element1['vote_count']) <  int(element2['vote_count']):
        return True
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return False
    
def greater( self, element1, element2):
    t1_start = process_time() #tiempo inicial
    if int(element1['vote_average'])  > int(element2['vote_average']):
        return True
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return False

def main():
    lista = None
    directores= []
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                lista = loadCSVFile("Data/SmallMoviesDetailsCleaned.csv") #llamar funcion cargar datos
                print("Datos cargados, ",lista['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')

                    Columna="original_title"

                    counter=countElementsFilteredByColumn(criteria, "original_title" , lista) #filtrar una columna por criterio  
                    
                    """Hay que tener en cuenta que no es el columna nombre, ya que usamos otro archivo de pruebas\n 
                    y en este no se encuentra esta columna""" 

                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    directores= loadCSVFile("Data/MoviesCastingRaw-small.csv") 
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsByCriteria(criteria,0,lista, directores)
                    print("Coinciden ",counter," elementos con el criterio: '", criteria ,"' (en construcción ...)")
            elif int(inputs[0])==5: #opcion 5
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    print("Seleccione el tipo de algoritmo según como desee organizar su información")
                    print("51- SelectionSort")
                    print("52- InsertionSort")
                    print("53- ShellSort")
                    centi=True
                    while centi:
                        opcion= int(input('Seleccione una opción para continuar'))
                        if len(inputs)>0:
                            if opcion==51: #opcion 1  
                                sort1.insertionSort(lista,less) 
                            elif opcion==52: #opcion 2  
                                sort2.selectionSort(lista,less) 
                            elif opcion==53: #opcion 3
                                sort3.shellSort(lista,less) 
                            else:
                                centi=False
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()