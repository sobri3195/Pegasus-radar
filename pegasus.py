import numpy as np
import matplotlib.pyplot as plt

# Parameter radar
radar_range = 100  # Jangkauan radar dalam satuan jarak (misal meter)
radar_angle = 60  # Sudut pandang radar dalam derajat

# Fungsi untuk membuat objek di area tertentu
def create_objects(num_objects, area_range):
    objects = []
    for _ in range(num_objects):
        x = np.random.uniform(-area_range, area_range)
        y = np.random.uniform(-area_range, area_range)
        objects.append((x, y))
    return objects

# Fungsi untuk mendeteksi objek dalam jangkauan radar
def detect_objects(radar_position, objects, radar_range, radar_angle):
    detected_objects = []
    radar_angle_rad = np.deg2rad(radar_angle / 2)
    for obj in objects:
        distance = np.sqrt((obj[0] - radar_position[0]) ** 2 + (obj[1] - radar_position[1]) ** 2)
        angle = np.arctan2(obj[1] - radar_position[1], obj[0] - radar_position[0])
        if distance <= radar_range and -radar_angle_rad <= angle <= radar_angle_rad:
            detected_objects.append(obj)
    return detected_objects

# Inisialisasi radar dan objek
radar_position = (0, 0)  # Posisi radar
objects = create_objects(50, 150)  # Membuat 50 objek dalam area -150 sampai 150

# Deteksi objek
detected_objects = detect_objects(radar_position, objects, radar_range, radar_angle)

# Plot area dan objek yang terdeteksi
plt.figure(figsize=(10, 10))
ax = plt.gca()

# Plot area radar
circle = plt.Circle(radar_position, radar_range, color='b', fill=False, linestyle='--')
ax.add_artist(circle)

# Plot sudut pandang radar
left_line_x = [radar_position[0], radar_range * np.cos(np.deg2rad(radar_angle / 2))]
left_line_y = [radar_position[1], radar_range * np.sin(np.deg2rad(radar_angle / 2))]
right_line_x = [radar_position[0], radar_range * np.cos(np.deg2rad(-radar_angle / 2))]
right_line_y = [radar_position[1], radar_range * np.sin(np.deg2rad(-radar_angle / 2))]

plt.plot(left_line_x, left_line_y, 'b--')
plt.plot(right_line_x, right_line_y, 'b--')

# Plot objek
for obj in objects:
    plt.plot(obj[0], obj[1], 'ro')

# Plot objek yang terdeteksi
for obj in detected_objects:
    plt.plot(obj[0], obj[1], 'go')

plt.xlim(-radar_range * 1.5, radar_range * 1.5)
plt.ylim(-radar_range * 1.5, radar_range * 1.5)
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Pegasus-Radar: Simulasi Deteksi Objek')
plt.grid(True)
plt.show()
