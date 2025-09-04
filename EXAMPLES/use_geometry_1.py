import sys
import geometry  # load geometry.py

# MODULE.name
circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{round(square, 3) = }")

# module search order
# 1. current folder
# 2. folders in PYTHONPATH
# 3. folders under installation folder

for path in sys.path:
    print(path)

print(f"{sys.prefix = }")
