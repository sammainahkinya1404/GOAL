import simpy

def producer(env, store):
    for i in range(3):
        print(f'Producing item {i} at time {env.now}')
        yield store.put(f'item {i}')
        yield env.timeout(1)

def consumer(env, store):
    while True:
        item = yield store.get()
        print(f'Consumed {item} at time {env.now}')
        yield env.timeout(2)

env = simpy.Environment()
store = simpy.Store(env)
env.process(producer(env, store))
env.process(consumer(env, store))
env.run(until=110)
