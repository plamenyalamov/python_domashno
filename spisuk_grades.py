grades = [95, 82, 67, 54, 100, 73, 88, 42]

excellent = []
good = []
passed = []
fail = []

for g in grades:
    if g >= 90:
        excellent.append(g)
    elif 70 <= g <= 89:
        good.append(g)
    elif 50 <= g <= 69:
        passed.append(g)
    else:
        fail.append(g)

print("Excellent:", excellent)
print("Good:", good)
print("Pass:", passed)
print("Fail:", fail)
