import random

# cache sequence appears as a list

def fifo_cache(cache_sequence, cache_size):
    misses = 0
    hits = 0
    miss_hit_table = [0]*len(cache_sequence)
    cache = []
    firstCache_tracker = []
    for i in xrange(len(cache_sequence)):
        if cache_sequence[i] not in cache:
            if len(cache) < cache_size:
                cache.append(cache_sequence[i])
                firstCache_tracker.append(i+1)
            else:
                f = min(firstCache_tracker)
                ind = firstCache_tracker.index(f)
                cache[ind] = cache_sequence[i]
                firstCache_tracker[ind] = i+1
            misses += 1
            miss_hit_table[i] = 1
        else:
            hits += 1
            miss_hit_table[i] = 0
    return hits, misses, miss_hit_table




def Random(cache_sequence, cache_size, seed):
    misses = 0
    hits = 0
    miss_hit_table = [0]*len(cache_sequence)
    cache = []
    random.seed(seed)
    for i in xrange(len(cache_sequence)):
        if cache_sequence[i] not in cache:
            if len(cache) < cache_size:
                cache.append(cache_sequence[i])
            else:
                l = random.randint(0, cache_size-1)
                cache[l] = cache_sequence[i]
            misses += 1
            miss_hit_table[i] = 1
        else:
            hits += 1
            miss_hit_table[i] = 0
    return hits, misses, miss_hit_table    


def lru(cache_sequence, cache_size):
    misses = 0
    hits = 0
    miss_hit_table = [0]*len(cache_sequence)
    cache = []
    recentCache_tracker = []
    for i in xrange(len(cache_sequence)):
        if cache_sequence[i] not in cache:
            if len(cache) < cache_size:
                cache.append(cache_sequence[i])
                recentCache_tracker.append(i+1)
            else:
                f = min(recentCache_tracker)
                ind = recentCache_tracker.index(f)
                cache[ind] = cache_sequence[i]
                recentCache_tracker[ind] = i+1 
            misses += 1
            miss_hit_table[i] = 1
        else:
            ind = cache.index(cache_sequence[i])
            recentCache_tracker[ind] = i+1
            hits += 1
            miss_hit_table[i] = 0
    return hits, misses, miss_hit_table


def optimal(cache_sequence, cache_size):
    misses = 0
    hits = 0
    miss_hit_table = [0]*len(cache_sequence)
    cache = []
    for i in xrange(len(cache_sequence)):
        if cache_sequence[i] not in cache:
            if len(cache) < cache_size:
                cache.append(cache_sequence[i])
            else:
                flag = 0
                remove_item = None
                j = cache_sequence[i+1:]
                d = []
                for k in xrange(cache_size):
                    try:
                        d.append(j.index(cache[k]))
                    except:
                        remove_item = cache[k]
                        flag = 1
                if flag == 0:
                    remove_item = j[max(d)]
                cache.remove(remove_item)
                cache.append(cache_sequence[i])
            misses += 1
            miss_hit_table[i] = 1
        else:
            hits += 1
            miss_hit_table[i] = 0
    return hits, misses, miss_hit_table


                
