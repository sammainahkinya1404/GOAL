import simpy
def machine(env):
    try:
        print("Machine starts at", env.now)
        yield env.timeout(10)
        print("Machine finished at", env.now)
    except simpy.Interrupt:
        print("Machine interrupted at", env.now)

def interrupter(env, proc):
    yield env.timeout(3)
    proc.interrupt()

env = simpy.Environment()
m_proc = env.process(machine(env))
env.process(interrupter(env, m_proc))
env.run()
