import matplotlib.pyplot as plt
import numpy as np

# Data for Graph 1: Stopping Potential vs Frequency
freq = np.array([8.21, 7.40, 6.88, 5.49, 5.20])
v_2mm = np.array([-1.920, -1.543, -1.357, -0.819, -0.700])
v_4mm = np.array([-1.926, -1.560, -1.375, -0.824, -0.703])
v_8mm = np.array([-1.940, -1.575, -1.386, -0.832, -0.709])

vs_2mm = np.abs(v_2mm)
vs_4mm = np.abs(v_4mm)
vs_8mm = np.abs(v_8mm)

plt.figure(figsize=(8, 5))
plt.plot(freq, vs_2mm, 'o-', label='2 mm Aperture')
plt.plot(freq, vs_4mm, 's-', label='4 mm Aperture')
plt.plot(freq, vs_8mm, '^-', label='8 mm Aperture')
plt.xlabel('Frequency (10^14 Hz)')
plt.ylabel('Stopping Potential (V)')
plt.title('Stopping Potential vs Frequency')
plt.grid(True)
plt.legend()
plt.savefig('graph1_vs_f.png')

# Data for Graph 2: Current vs Voltage (Constant Frequency, Different Intensities)
v2 = np.array([-4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
i_2mm = np.array([0, 0, 22, 73, 106, 127, 147, 168, 184, 200, 216, 230, 244, 259, 272, 286, 298, 306])
i_4mm = np.array([0, 0, 62, 250, 398, 490, 570, 643, 730, 786, 843, 900, 950, 1006, 1060, 1124, 1175, 1225])
i_8mm = np.array([0, 0, 168, 776, 1420, 1800, 2100, 2500, 2750, 3000, 3270, 3500, 3730, 3950, 4180, 4450, 4630, 4780])

plt.figure(figsize=(8, 5))
plt.plot(v2, i_2mm, 'o-', label='2 mm Aperture')
plt.plot(v2, i_4mm, 's-', label='4 mm Aperture')
plt.plot(v2, i_8mm, '^-', label='8 mm Aperture')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (10^-11 A)')
plt.title('Current vs Voltage (Constant Frequency $\lambda = 436$ nm)')
plt.grid(True)
plt.legend()
plt.savefig('graph2_i_vs_v_intensity.png')

# Data for Graph 3: Current vs Voltage (Constant Intensity, Different Frequencies)
v3_365 = np.array([-1.91, -0.95, 0.90, 1.92, 2.90, 3.90, 4.90, 5.92, 7.02, 7.90, 8.82, 9.86, 10.93, 11.97, 12.90, 13.84, 14.94, 15.97, 16.89])
i3_365 = np.array([30, 40, 200, 340, 490, 620, 710, 790, 850, 900, 950, 1040, 1080, 1180, 1210, 1270, 1290, 1370, 1420])

v3_405 = np.array([-0.83, 0.11, 0.94, 1.32, 2.12, 3.12, 4.12, 5.12, 6.12, 7.15, 8.16, 9.13, 10.13, 11.17, 12.10, 13.10, 14.12, 15.12, 16.14, 17.11, 18.14, 19.25])
i3_405 = np.array([30, 60, 100, 120, 170, 220, 250, 280, 300, 330, 340, 390, 410, 430, 440, 460, 490, 500, 520, 530, 570, 580])

v3_436 = np.array([-0.95, 0.14, 0.43, 0.70, 1.01, 1.25, 1.65, 1.82, 1.97, 2.46, 2.98, 3.97, 4.96, 5.97, 6.97, 7.97, 8.96, 9.95, 10.92, 11.92, 12.92, 13.92, 14.93, 15.93, 16.93, 17.93, 18.93])
i3_436 = np.array([30, 90, 110, 130, 160, 180, 230, 240, 260, 320, 360, 410, 460, 510, 540, 570, 610, 630, 690, 720, 750, 790, 850, 870, 880, 900, 930])

plt.figure(figsize=(8, 5))
plt.plot(v3_365, i3_365, 'o-', label='365 nm')
plt.plot(v3_405, i3_405, 's-', label='405 nm')
plt.plot(v3_436, i3_436, '^-', label='436 nm')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (10^-11 A)')
plt.title('Current vs Voltage (Constant Intensity 4 mm)')
plt.grid(True)
plt.legend()
plt.savefig('graph3_i_vs_v_freq.png')
