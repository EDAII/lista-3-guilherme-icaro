import matplotlib.pyplot as plt
import numpy as np

def plota_grafico(results_quicksort, results_mergesort, results_heapsort, results_radixsort):
    plt.title('Gráfico de desempenho')
    plt.ylabel('Tempo')
    plt.xlabel('Iteração')
    plt.plot(results_quicksort, color='blue')
    plt.plot(results_mergesort, color='red')
    plt.plot(results_heapsort, color='green')
    plt.plot(results_radixsort, color='yellow')


    plt.show()
