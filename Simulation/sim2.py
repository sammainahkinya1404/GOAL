import simpy
import random

def machine(env):
    while True:
        working_time = random.randint(5, 10)
        print(f"Machine works for {working_time} at time {env.now}")
        yield env.timeout(working_time)

        print(f"Machine broke at time {env.now}")
        repair_time = random.randint(2, 5)
        yield env.timeout(repair_time)
        print(f"Machine repaired at time {env.now}")

env = simpy.Environment()
env.process(machine(env))
env.run(until=30)
