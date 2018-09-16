from cache_simulations import Simulator

sim1 = Simulator("FIFO", 0.9, 10)
hits, misses, hit_miss = sim1.simulate_cache()

print hits, misses, hit_miss