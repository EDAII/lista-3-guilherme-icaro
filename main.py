from quick_sort import quick_sort
from mergesort import merge_sort
from heap_sort import heapsort
from radix_sort import radix_sort
from plot_graphic import plot_graphic
import time
import random
# from plot_graphic import plot_graphic
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def cria_lista(quantidade, limite):
    return random.sample(range(limite), quantidade)

def menu_inicial():
    print("Painel de Contextos para algoritmos de ordenação - O(nlogn)")
    print("(1) - Analisar algoritmos separadamente.")
    print("(2) - Fazer comparativo entre algoritmos.")
    print("(0) - Sair.")

    option = input("Selecione uma opção: ")

    if option == '1':
        menu_de_algoritmos()
    elif option == '2':
        comparativo_de_algoritmos()
    elif option != '0':
        print("Esta opção não é valida!")
        menu_inicial()

def menu_de_algoritmos():
    print("Analise de algoritmos separadamente")
    print("(1) - Quick Sort")
    print("(2) - Merge Sort")
    print("(3) - Heap Sort")
    print("(4) - Radix Sort")

    option = input("Escolha uma opção: ")

    quantity = [100, 1000, 10000, 100000]
    limit = 1000**2

    if option == '1':

        for i in quantity:
            lista = cria_lista(i, limit)

            inicio = time.time()
            quick_sort(lista, 0, len(lista))
            fim = time.time()
            result = fim - inicio
            print("O tempo de ordenação do quicksort em um vetor de {} elementos é de {} segundos.".format(i, result))

    elif option == '2':

        for i in quantity:
            lista = cria_lista(i, limit)

            inicio = time.time()
            merge_sort(lista)
            fim = time.time()
            result = fim - inicio
            print("O tempo de ordenação do mergesort em um vetor de {} elementos é de {} segundos.".format(i, result))

    elif option == '3':
        # Chama o heapsort
        pass
    elif option == '4':
        # Chama o Radix Sort
        pass

def comparativo_de_algoritmos():

    quantity = [100, 1000, 10000]
    limit = 1000**2

    for i in quantity:
        lista = cria_lista(i, limit)

        lista_quick = lista
        inicio = time.time()
        quick_sort(lista_quick, 0, len(lista_quick))
        fim = time.time()
        tempo = fim - inicio

        lista_merge = lista
        inicio = time.time()
        merge_sort(lista_merge)
        fim = time.time()
        tempo = fim - inicio

initial_map = {
    '1': menu_de_algoritmos,
    '2': comparativo_de_algoritmos
}

menu_inicial()
