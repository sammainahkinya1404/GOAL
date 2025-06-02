import simpy
import random

def customer(env, name, atm):
    print(f"{name} arrives at the bank at {env.now:.2f}")
    with atm.request() as request:
        yield request
        print(f"{name} starts using the ATM at {env.now:.2f}")
        yield env.timeout(random.uniform(1, 3))
        print(f"{name} leaves the ATM at {env.now:.2f}")

def setup(env, num_customers, interval):
    atm = simpy.Resource(env, capacity=1)
    for i in range(num_customers):
        yield env.timeout(random.expovariate(1.0 / interval))
        env.process(customer(env, f'Customer {i+1}', atm))

env = simpy.Environment()
env.process(setup(env, num_customers=5, interval=2))
env.run()


