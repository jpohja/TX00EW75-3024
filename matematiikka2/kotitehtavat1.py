#kotitehtävä 1
import numpy as np
# 1. a)
a = 2.493
print(np.degrees(a))
# 1. b)
b = 0.911
print(np.degrees(b))
# 2. a)
a = 137.7
print(np.radians(a))
# 2. b)
b = 62.3
print(np.radians(b))
# 3.
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
for i in A:
    print(np.radians(i))
#kotitehtävä 2
kateetti_a = 1.6
kateetti_b = 2.3
hypotenuusa = np.hypot(kateetti_a, kateetti_b)
print(hypotenuusa)