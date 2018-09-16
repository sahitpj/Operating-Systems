import random
from cache_algorithms import fifo_cache, Random, lru, optimal
import matplotlib.pyplot as plt

#workload represent the percentage distribtuon

class Simulator(object):
    def __init__(self, algorithm, workload, cache_size, seed):
        self.seed = seed
        self.algorithm = algorithm
        self.workload = workload
        self.algos = ['FIFO', 'Random', 'LRU', 'Optimal']
        self.pages = 100
        self.workloadSize = 1000
        self.cacheSequence = None
        self.hotPages = None
        self.cache_size = cache_size

    def generate_hotPages(self):
        hotPages = []
        numberOfHotPages = int((1-self.workload)*self.pages)
        while len(hotPages) < numberOfHotPages:
            page = random.randint(1, 101)
            if page not in hotPages:
                hotPages.append(page)
        self.hotPages = hotPages

    def workload_stats(self):
        hot = 0
        not_hot = 0
        for i in self.cacheSequence:
            if i in self.hotPages:
                hot += 1
            else:
                not_hot += 1
        plt.scatter([1,2],[hot,not_hot])
        plt.show()


    def generate_cacheSequence(self):
        cacheSequence = [0]*self.workloadSize
        for i in xrange(int(self.workloadSize*self.workload)):
            k = random.choice(self.hotPages)
            flag = 0
            while flag == 0:
                g = random.randint(0, 1000)
                if cacheSequence[g] == 0:
                    cacheSequence[g] = k
                    flag = 1
        for i in xrange(int(self.workloadSize*(1-self.workload))):
            flag_1 = 0
            while flag_1 == 0:
                k = random.choice(range(1,101))
                if k not in self.hotPages:
                    flag_1 = 1
                    flag_2 = 0
                    while flag_2 == 0:
                        g = random.randint(0, 999)
                        if cacheSequence[g] == 0:
                            cacheSequence[g] = k
                            flag_2 = 1
        self.cacheSequence = cacheSequence

    def simulate_cache(self):
        self.generate_hotPages()
        self.generate_cacheSequence()
        if self.algorithm == "FIFO":
            hits, misses, miss_hit_table = fifo_cache(self.cacheSequence, self.cache_size)
            return  hits, misses, miss_hit_table
        elif self.algorithm == "Random":
            hits, misses, miss_hit_table = Random(self.cacheSequence, self.cache_size, self.seed) 
            return  hits, misses, miss_hit_table  
        elif self.algorithm == "LRU":
            hits, misses, miss_hit_table = lru(self.cacheSequence, self.cache_size)
            return  hits, misses, miss_hit_table
        elif self.algorithm == "Optimal":
            hits, misses, miss_hit_table = optimal(self.cacheSequence, self.cache_size)
            return  hits, misses, miss_hit_table





        
