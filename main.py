import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Настройка 3D-сцены
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')  # Чёрный фон для контраста
ax.grid(False)

### 1. Создаём глазное яблоко (сфера) ###
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
x = 0.8 * np.outer(np.cos(u), np.sin(v))
y = 0.8 * np.outer(np.sin(u), np.sin(v))
z = 0.8 * np.outer(np.ones(np.size(u)), np.cos(v))

# Рисуем сферу с эффектом "свечения"
ax.plot_surface(x, y, z, color='white', alpha=0.9, edgecolor='cyan', linewidth=0.5)

### 2. Радужная оболочка (кольцо с градиентом) ###
iris_radius = 0.4
for r in np.linspace(iris_radius, 0.3, 10):
    iris_u = np.linspace(0, 2 * np.pi, 100)
    iris_x = r * np.cos(iris_u)
    iris_y = r * np.sin(iris_u)
    iris_z = 0.8  # Смещаем вперёд относительно центра глаза
    ax.plot(iris_x, iris_y, iris_z, color=plt.cm.hsv(r/iris_radius), linewidth=2)

### 3. Зрачок (чёрный круг) ###
pupil_radius = 0.15
pupil_u = np.linspace(0, 2 * np.pi, 50)
pupil_x = pupil_radius * np.cos(pupil_u)
pupil_y = pupil_radius * np.sin(pupil_u)
pupil_z = 0.81  # Чуть ближе к камере, чем радужка
ax.fill(pupil_x, pupil_y, pupil_z, color='black')

### 4. Блики (эффект влажного глаза) ###
highlight_x = [0.2, 0.3]
highlight_y = [0.3, 0.2]
highlight_z = [0.82, 0.83]
ax.scatter(highlight_x, highlight_y, highlight_z, color='white', s=50, alpha=0.8)

### 5. Веки (полукольца вокруг глаза) ###
eyelid_theta = np.linspace(-np.pi/3, np.pi/3, 50)
eyelid_x = 1.0 * np.cos(eyelid_theta)
eyelid_y = 1.0 * np.sin(eyelid_theta)
eyelid_z = 0.5 * np.ones_like(eyelid_theta)
ax.plot(eyelid_x, eyelid_y, eyelid_z, color='gold', linewidth=3, alpha=0.5)

### Настройка вида ###
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_title('3D Глаз-Иллюминатор', color='white', fontsize=16)

plt.tight_layout()
plt.show()