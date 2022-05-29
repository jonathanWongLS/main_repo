import random
import time
import math
import matplotlib.pyplot as plt
from Q1 import num_rad_sort

def base_timer(num_list, base_list):
    time_taken = []
    for i in range(len(base_list)):
        start = time.time()
        num_rad_sort(num_list, base_list[i])
        end = time.time() - start
        time_taken.append(end)

    return time_taken 


random.seed("FIT2004S22021")
data1 = [random.randint(0,2**25) for _ in range(2**15)]
data2 = [random.randint(0,2**25) for _ in range(2**16)]
bases1 = [2**i for i in range(1,23)]
bases2 = [2*10**6 + (5*10**5)*i for i in range(1,10)]

# logarithmic scale 
log_bases1 = []
log_bases2 = []
for i in range(len(bases1)):
    log_bases1.append(math.log(bases1[i]))
    
for i in range(len(bases2)):
    log_bases2.append(math.log(bases2[i]))

y1 = base_timer(data1, bases1)
y2 = base_timer(data2, bases1)
y3 = base_timer(data1, bases2)
y4 = base_timer(data2, bases2)

plt.subplot(1,2,1)
plt.plot(log_bases1,y1)
plt.plot(log_bases1,y2)
plt.legend(['y1','y2'])
plt.title('Logarithmic Scale')
plt.xlabel('Base')
plt.ylabel('Runtimes')

plt.subplot(1,2,2)
plt.plot(bases2, y3)
plt.plot(bases2, y4)
plt.legend(['y3','y4'])
plt.title('Linear Scale')
plt.xlabel('Base')
plt.ylabel('Runtimes')

plt.show()

