import heapq
import random

# Parameters
SIM_TIME = 50
ARRIVAL_RATE = 0.5
SERVICE_RATE = 1.0

# System state
clock = 0
server_busy = False
queue = []
events = []  # Future Event List (FEL)

# Statistics
wait_times = []

def schedule(event_time, event_type, data=None):
    heapq.heappush(events, (event_time, event_type, data))

def handle_arrival():
    global server_busy
    print(f"[{clock:.2f}] Arrival")
    if server_busy:
        queue.append(clock)
    else:
        server_busy = True
        service_time = random.expovariate(SERVICE_RATE)
        schedule(clock + service_time, "departure", clock)

    next_arrival = clock + random.expovariate(ARRIVAL_RATE)
    if next_arrival < SIM_TIME:
        schedule(next_arrival, "arrival")

def handle_departure(start_time):
    global server_busy
    print(f"[{clock:.2f}] Departure")
    wait_times.append(clock - start_time)
    if queue:
        start = queue.pop(0)
        service_time = random.expovariate(SERVICE_RATE)
        schedule(clock + service_time, "departure", start)
    else:
        server_busy = False

# Initial event
schedule(random.expovariate(ARRIVAL_RATE), "arrival")

# Simulation loop
while events and clock < SIM_TIME:
    clock, event_type, data = heapq.heappop(events)
    if event_type == "arrival":
        handle_arrival()
    elif event_type == "departure":
        handle_departure(data)

# Summary
print(f"\nAverage wait: {sum(wait_times)/len(wait_times):.2f} minutes")
