import simpy
import random

# Parameters
ARRIVAL_RATE = 0.5     # Mean arrival rate (λ = 0.5 -> interarrival time = 2 mins)
SERVICE_RATE = 1.0     # Mean service rate (μ = 1.0 -> service time = 1 min)
SIM_TIME = 30          # Total simulation time (minutes)
NUM_SERVERS = 3        # Number of check-in counters

def passenger(env, name, checkin):
    arrival_time = env.now
    print(f"{name} arrives at {arrival_time:.2f}")

    with checkin.request() as request:
        yield request
        wait_time = env.now - arrival_time
        print(f"{name} starts check-in after waiting {wait_time:.2f} minutes")

        service_time = random.expovariate(SERVICE_RATE)
        yield env.timeout(service_time)

        print(f"{name} completes check-in at {env.now:.2f} (Service time: {service_time:.2f})")

def setup(env):
    checkin = simpy.Resource(env, capacity=NUM_SERVERS)
    i = 0
    while True:
        interarrival = random.expovariate(ARRIVAL_RATE)
        yield env.timeout(interarrival)
        i += 1
        env.process(passenger(env, f"Passenger {i}", checkin))

# Run the simulation
env = simpy.Environment()
env.process(setup(env))
env.run(until=SIM_TIME)
