import numpy as np
from matplotlib.colors import LinearSegmentedColormap, rgb2hex
from kaleidoscope import bloch_sphere

# цветовая карта от жёлтого к чёрному
lsm = LinearSegmentedColormap.from_list('yellow_to_black', ["#ffff00", "#000000"])

rz = [[0, np.sin(th), -np.cos(th)] for th in np.linspace(0, np.pi/2, 15)]
ry = [[-np.cos(th), -np.sin(th), 0] for th in np.linspace(3*np.pi/2, np.pi, 15)]
rx = [[np.sin(th), np.cos(th), 0] for th in np.linspace(np.pi/2, np.pi, 15)]

points = rz + ry + rx

# изменение прозрачности от 1.0 до 0.75
points_alpha = np.linspace(1.0, 0.75, len(points))

# изменение цвета точек от жёлтого к чёрному
points_color = [rgb2hex(lsm(kk)) for kk in np.linspace(0, 1, len(points))]

# начальный вектор (|1⟩) и конечный вектор (|-Y⟩)
vectors = [[0, 0, -1], [0, -1, 0]]  # от |1⟩ (ось -Z) до |-Y⟩ (ось -Y)

# визуализирую сферу Блоха
bloch_sphere(
    points=points,
    vectors=vectors,
    vectors_color=["#ffff00", "#000000"],  # Цвета векторов: жёлтый -> чёрный
    points_alpha=points_alpha,
    points_color=points_color
).show()
