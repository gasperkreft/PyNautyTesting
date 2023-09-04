from pynauty import *
import random
import time
import matplotlib.pyplot as plt


št_ponovitev = 100
avg_times = []
velikosti = [10,20,30,50,100,200,500,1000,2000]
for size in velikosti:
    times = []
    for ponovitev in range(št_ponovitev):
        g = Graph(size)
        for i in range(size):
            num = random.randint(0, size/10+3) #stevilo sosedov
            for j in range(num):
                g.connect_vertex(i,random.randint(0, size-1))

        start_time = time.time()
        canon_label(g)
        end_time = time.time()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

    avg_times.append(sum(times)/len(times))

print(avg_times)
plt.plot(velikosti,avg_times, marker='o', linestyle='-',)
plt.yscale("log")
plt.xscale("log")
plt.xlabel('Število vozlišč')
plt.ylabel('Čas [s]')

plt.savefig('line_plot.svg')
