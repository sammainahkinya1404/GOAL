import random
import simpy
def customer(env, name, server):
    if len(server.queue) >= server.capacity - 1:
        print(f'{name} is rejected at {env.now:.2f} (Queue full)')
        return
    arrival = env.now
    with server.request() as req:
        yield req
        yield env.timeout(random.expovariate(1.0))
        print(f'{name} served at {env.now:.2f}')

def setup(env, K=5):
    server = simpy.Resource(env, capacity=1)
    i = 0
    while True:
        if len(server.queue) < K:
            i += 1
            env.process(customer(env, f'Customer {i}', server))
        yield env.timeout(random.expovariate(0.5))
