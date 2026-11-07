cpu_readings = [65, 48, 72, 31, 59, 31, 84]

max_cpu = cpu_readings[0]
max_position = 0

low_cpu = cpu_readings[0]
low_position = 0

for position, cpu in enumerate(cpu_readings):
    if cpu > max_cpu:
        max_cpu = cpu
        max_position = position

    if cpu < low_cpu :
        low_cpu = cpu
        low_position = position


print(f"{max_position}, {max_cpu}")
print(f"{low_position}, {low_cpu}")