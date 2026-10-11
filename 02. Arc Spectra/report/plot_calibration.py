import matplotlib.pyplot as plt
import numpy as np

# Hartmann constants from observation sheet (signed by Shivanand Sir on 11/09/2026)
lambda0 = 248.6934
d0 = 4714.8846
C = 708674.98

def hartmann(d):
    return lambda0 + C / (d0 - d)

# Continuous curve
d_vals = np.linspace(100, 3100, 500)
lambda_vals = hartmann(d_vals)

# Hg calibration points
d_hg = np.array([171, 928, 2332])
lambda_hg = np.array([404.656, 435.833, 546.096])

# Other prominent Hg lines for verification
d_hg_other = np.array([2554, 2568])
lambda_hg_other = np.array([576.960, 579.066])

# Copper experimental points
d_cu = np.array([1343, 1443, 2010, 2058, 2121, 2190, 2509, 2564])
lambda_cu_calc = hartmann(d_cu)
lambda_cu_theo = np.array([458.700, 465.112, 510.554, 515.324, 521.641, 529.252, 570.024, 578.213])

# Brass experimental points
d_brass = np.array([1442, 1484, 1545, 1663, 2009, 2057, 2085, 2121, 2563, 2881])
lambda_brass_calc = hartmann(d_brass)
lambda_brass_theo = np.array([465.112, 468.014, 472.010, 481.053, 510.554, 515.324, 518.199, 521.641, 578.213, 633.893])

# Plot 1: Hartmann Calibration Curve
plt.figure(figsize=(9, 6), dpi=300)
plt.plot(d_vals, lambda_vals, 'k-', linewidth=1.8, label=r'Hartmann Calibration Curve $\lambda(d) = 248.69 + \frac{708675}{4714.88 - d}$')
plt.scatter(d_hg, lambda_hg, color='#8E24AA', s=90, zorder=5, marker='o', edgecolors='black', label='Hg Calibration Points')
plt.scatter(d_hg_other, lambda_hg_other, color='#AB47BC', s=70, zorder=5, marker='v', edgecolors='black', label='Hg Yellow Doublet (Verification)')
plt.scatter(d_cu, lambda_cu_calc, color='#E65100', s=70, zorder=5, marker='s', edgecolors='black', label='Copper (Cu I) Emission Lines')
plt.scatter(d_brass, lambda_brass_calc, color='#00897B', s=70, zorder=5, marker='^', edgecolors='black', label='Brass Emission Lines (Cu + Zn)')

plt.xlabel('CCD Pixel Position, $d$ (pixels)', fontsize=12, fontweight='bold')
plt.ylabel('Wavelength, $\lambda$ (nm)', fontsize=12, fontweight='bold')
plt.title('Spectrometer Calibration: Hartmann Dispersion Curve', fontsize=14, fontweight='bold', pad=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10, loc='upper left', framealpha=0.95)
plt.tight_layout()
plt.savefig('hartmann_calibration_curve.png')
plt.close()

# Plot 2: Percentage Error vs Wavelength
plt.figure(figsize=(9, 4.5), dpi=300)
err_cu = ((lambda_cu_calc - lambda_cu_theo) / lambda_cu_theo) * 100
err_brass = ((lambda_brass_calc - lambda_brass_theo) / lambda_brass_theo) * 100

plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.scatter(lambda_cu_theo, err_cu, color='#E65100', s=80, marker='s', edgecolors='black', label='Copper Lines Error (%)')
plt.scatter(lambda_brass_theo, err_brass, color='#00897B', s=80, marker='^', edgecolors='black', label='Brass Lines Error (%)')

plt.xlabel('Theoretical Wavelength, $\lambda_{\mathrm{theo}}$ (nm)', fontsize=11, fontweight='bold')
plt.ylabel('Percentage Error (%)', fontsize=11, fontweight='bold')
plt.title('Percentage Error of Measured Emission Lines Relative to Standard NIST Values', fontsize=12, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(-0.15, 0.25)
plt.legend(fontsize=10, loc='upper right', framealpha=0.95)
plt.tight_layout()
plt.savefig('error_distribution.png')
plt.close()
print("Graphs generated successfully.")
