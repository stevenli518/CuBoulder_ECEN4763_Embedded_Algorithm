from structures.array import array
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def display_data(array, index, title, xlabel, ylabel, filename):
    df = pd.DataFrame(array, index=index)
    ax = df.plot()
    ax.set_ylim(bottom=0)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(filename)


def main():
    size = 1001
    time_array = []
    memory_array = []
    my_array = array.Array()

    for test in ('Time', 'Memory'):
        for i in range(size):
            if test == 'Memory':
                import tracemalloc
                tracemalloc.start()

            start = time.time_ns()
            my_array.insert(100)  # append to end
            end = time.time_ns()

            if test == 'Memory':
                current, peak = tracemalloc.get_traced_memory()
                memory_array.append(peak)
                tracemalloc.stop()
            elif test == 'Time':
                time_array.append((end - start)/1000000)

    index = [i for i in range(len(time_array))]
    display_data(memory_array,
                 index,
                 title='Memory Comparison for Array Insert',
                 xlabel='Input Size',
                 ylabel='Memory Consumed in Bytes',
                 filename='ArrayInsert_Memory.png')

    display_data(time_array,
                 index,
                 title='Time Comparison for Array Insert',
                 xlabel='Input Size',
                 ylabel='Time Taken in Milliseconds',
                 filename='ArrayInsert_Time.png')


if __name__ == '__main__':
    main()
