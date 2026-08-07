import numpy as np
import matplotlib.pyplot as plt

# Band Pass Filter Data
bp_f = np.array([100, 200, 400, 600, 1000, 1200, 1600, 1800, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000])
bp_vout = np.array([150, 260, 400, 600, 670, 800, 820, 850, 910, 950, 980, 990, 990, 980, 960, 940, 910, 890, 860, 830, 810, 800, 780, 750, 720, 700, 660, 660]) / 1000.0 # Convert mV to V
bp_vin = 2.0
bp_gain = bp_vout / bp_vin
bp_gain_db = 20 * np.log10(bp_gain)

plt.figure(figsize=(10, 6))
plt.semilogx(bp_f, bp_gain_db, marker='o', linestyle='-', color='b')
plt.title('Frequency Response of Band Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Voltage Gain (dB)')
plt.grid(True, which="both", ls="-")

max_bp_gain = np.max(bp_gain_db)
plt.axhline(max_bp_gain - 3, color='r', linestyle='--', label='-3dB Level')
plt.axvline(1100, color='purple', linestyle=':', label='f_L (~1.1 kHz)')
plt.axvline(18000, color='orange', linestyle=':', label='f_H (~18 kHz)')
plt.axvline(4450, color='black', linestyle='-.', label='Center Freq f_r (~4.45 kHz)')
plt.fill_betweenx(y=[np.min(bp_gain_db), np.max(bp_gain_db)], x1=1100, x2=18000, color='green', alpha=0.1, label='Pass Band')

plt.legend()
plt.savefig('band_pass_graph.png')
plt.close()

# Band Reject Filter Data
br_f = np.array([20, 50, 100, 140, 160, 180, 200, 400, 600, 800, 1000, 1100, 1200, 1400, 1600, 1800, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000])
br_vout = np.array([2.160, 2.080, 2.000, 1.840, 1.760, 1.680, 1.680, 1.040, 0.610, 0.320, 0.096, 0.075, 0.160, 0.300, 0.450, 0.570, 0.700, 0.950, 1.140, 1.420, 1.600, 1.740, 1.820, 1.900, 1.940, 1.980, 2.010, 2.020, 2.050, 2.060, 2.100, 2.100, 2.120, 2.130, 2.140, 2.140, 2.140])
br_vin = 2.0
br_gain = br_vout / br_vin
br_gain_db = 20 * np.log10(br_gain)

plt.figure(figsize=(10, 6))
plt.semilogx(br_f, br_gain_db, marker='o', linestyle='-', color='g')
plt.title('Frequency Response of Band Reject Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Voltage Gain (dB)')
plt.grid(True, which="both", ls="-")

max_br_gain = np.max(br_gain_db)
plt.axhline(max_br_gain - 3, color='r', linestyle='--', label='-3dB Level')
plt.axvline(250, color='purple', linestyle=':', label='f_L (~250 Hz)')
plt.axvline(4000, color='orange', linestyle=':', label='f_H (~4 kHz)')
plt.axvline(1100, color='black', linestyle='-.', label='Notch Freq f_c (~1.1 kHz)')
plt.fill_betweenx(y=[np.min(br_gain_db), np.max(br_gain_db)], x1=250, x2=4000, color='red', alpha=0.1, label='Stop Band')

plt.legend()
plt.savefig('band_reject_graph.png')
plt.close()
