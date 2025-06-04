import simpy
import random

def customer(env, name, server):
    arrival = env.now
    print(f'{name} arrives at {arrival:.2f}')
    with server.request() as req:
        yield req
        wait = env.now - arrival
        print(f'{name} waits for {wait:.2f} units')
        service_time = random.expovariate(1.0)
        yield env.timeout(service_time)
        print(f'{name} leaves at {env.now:.2f}')

def setup(env):
    server = simpy.Resource(env, capacity=1)
    i = 0
    while True:
        yield env.timeout(random.expovariate(0.5))
        i += 1
        env.process(customer(env, f'Customer {i}', server))

env = simpy.Environment()
env.process(setup(env))
env.run(until=20)
