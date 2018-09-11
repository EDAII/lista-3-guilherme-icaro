from quick_sort import quick_sort
from mergesort import merge_sort
from heap_sort import heapsort
from radix_sort import radix_sort
import time
import random
from plot_graphics import plota_grafico

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

        for i in quantity:
            lista = cria_lista(i, limit)

            inicio = time.time()
            heapsort(lista)
            fim = time.time()
            result = fim - inicio
            print("O tempo de ordenação do heap em um vetor de {} elementos é de {} segundos.".format(i, result))
        
    elif option == '4':

        for i in quantity:
            lista = cria_lista(i, limit)

            inicio = time.time()
            radix_sort(lista)
            fim = time.time()
            result = fim - inicio
            print("O tempo de ordenação do radix em um vetor de {} elementos é de {} segundos.".format(i, result))

def comparativo_de_algoritmos():
    limit = 1000**2

    for i in range(0,100):
        lista = cria_lista(1000, limit)

        results_quicksort = []
        lista_quick = lista
        inicio = time.time()
        quick_sort(lista_quick, 0, len(lista_quick))
        fim = time.time()
        tempo = fim - inicio
        results_quicksort.append(tempo)

        results_mergesort = []
        lista_merge = lista
        inicio = time.time()
        merge_sort(lista_merge)
        fim = time.time()
        tempo = fim - inicio
        results_mergesort.append(tempo)

        results_heapsort = []
        lista_heap = lista
        inicio = time.time()
        heapsort(lista_heap)
        fim = time.time()
        tempo = fim - inicio
        results_heapsort.append(tempo)

        results_radixsort = []
        lista_radix = lista
        inicio = time.time()
        radix_sort(lista_radix)
        fim = time.time()
        tempo = fim - inicio
        results_radixsort.append(tempo)
        
    plota_grafico(results_quicksort, results_mergesort, results_heapsort, results_radixsort)

initial_map = {
    '1': menu_de_algoritmos,
    '2': comparativo_de_algoritmos
}

menu_inicial()
