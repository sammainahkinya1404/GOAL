import simpy
def car(env, fuel, start_signal):
    print("Car waiting at", env.now)
    yield simpy.AllOf(env, [fuel.get(10), start_signal])
    print("Car starts driving at", env.now)

env = simpy.Environment()
fuel = simpy.Container(env, init=0, capacity=50)
start_signal = env.timeout(5)
env.process(car(env, fuel, start_signal))

# Add fuel later
env.process(fuel.put(10))
env.run()
