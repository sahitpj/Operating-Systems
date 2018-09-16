from cache_simulations import Simulator

sim1 = Simulator("FIFO", 0.9, 10, None)
sim1.generate_hotPages()
sim1.generate_cacheSequence()
sim1.workload_stats()

