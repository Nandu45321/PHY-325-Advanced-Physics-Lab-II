import numpy as np
import matplotlib.pyplot as plt

# Matplotlib styling
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 1.2
plt.rcParams['grid.alpha'] = 0.4
plt.rcParams['grid.linestyle'] = '--'

# ==========================================
# 1. Single Crystal XRD Analysis (Mo tube)
# ==========================================
# Wavelengths in pm
# Mo K_beta = 63.09 pm, Mo K_alpha = 71.08 pm
sc_data = [
    {"order": 1, "line": r"$\mathrm{Mo\ K}_\beta$", "lambda_pm": 63.09, "theta_deg": 6.4, "I": 184.0},
    {"order": 1, "line": r"$\mathrm{Mo\ K}_\alpha$", "lambda_pm": 71.08, "theta_deg": 7.3, "I": 262.6},
    {"order": 2, "line": r"$\mathrm{Mo\ K}_\beta$", "lambda_pm": 63.09, "theta_deg": 12.9, "I": 21.3},
    {"order": 2, "line": r"$\mathrm{Mo\ K}_\alpha$", "lambda_pm": 71.08, "theta_deg": 14.6, "I": 26.5},
]

n_vals = np.array([d["order"] for d in sc_data])
lambda_vals = np.array([d["lambda_pm"] for d in sc_data])
n_lambda = n_vals * lambda_vals
theta_sc_deg = np.array([d["theta_deg"] for d in sc_data])
theta_sc_rad = np.radians(theta_sc_deg)
sin_theta_sc = np.sin(theta_sc_rad)

# a_0 for each peak: n * lambda = a_0 * sin(theta) => a_0 = (n * lambda) / sin(theta)
a0_sc_individual = n_lambda / sin_theta_sc

# Linear fit: sin(theta) = m * (n * lambda) + c
# where m = 1 / a_0
slope_sc, intercept_sc = np.polyfit(n_lambda, sin_theta_sc, 1)
# Also fit through origin: sin(theta) = m_0 * (n * lambda)
slope_sc_origin = np.sum(n_lambda * sin_theta_sc) / np.sum(n_lambda**2)

a0_sc_fit = 1.0 / slope_sc
a0_sc_fit_origin = 1.0 / slope_sc_origin
a0_sc_mean = np.mean(a0_sc_individual)

print("--- SINGLE CRYSTAL XRD ---")
for i, d in enumerate(sc_data):
    print(f"n={d['order']}, Line={d['line']}, lambda={d['lambda_pm']} pm, theta={d['theta_deg']} deg, sin(theta)={sin_theta_sc[i]:.5f}, n*lambda={n_lambda[i]:.2f} pm, a_0={a0_sc_individual[i]:.2f} pm")
print(f"Mean a_0 = {a0_sc_mean:.2f} pm")
print(f"Linear Fit Slope = {slope_sc:.7f} pm^-1, Intercept = {intercept_sc:.5f} => a_0 = {a0_sc_fit:.2f} pm")
print(f"Fit through origin Slope = {slope_sc_origin:.7f} pm^-1 => a_0 = {a0_sc_fit_origin:.2f} pm")

# Plot Single Crystal: sin(theta) vs n*lambda
fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(n_lambda, sin_theta_sc, color='#1f77b4', s=70, zorder=5, label='Measured Peaks (LD DIDACTIC)')

x_fit = np.linspace(50, 160, 200)
y_fit = slope_sc * x_fit + intercept_sc
ax.plot(x_fit, y_fit, color='#d62728', linestyle='-', linewidth=2, 
        label=f'Linear Fit: $\\sin\\theta = {slope_sc:.6f}\\,(n\\lambda) {intercept_sc:+.4f}$\n$a_0 = 1/m = {a0_sc_fit:.2f}$ pm ($R^2 = {np.corrcoef(n_lambda, sin_theta_sc)[0,1]**2:.4f}$)')

# Annotate points
labels = [r'$n=1, \mathrm{Mo}\ K_\beta$', r'$n=1, \mathrm{Mo}\ K_\alpha$', r'$n=2, \mathrm{Mo}\ K_\beta$', r'$n=2, \mathrm{Mo}\ K_\alpha$']
offsets = [(-45, -30), (12, 10), (-55, 12), (12, -20)]
for i, txt in enumerate(labels):
    ax.annotate(f"{txt}\n($\\theta={theta_sc_deg[i]}^\\circ$)", 
                (n_lambda[i], sin_theta_sc[i]),
                textcoords="offset points", xytext=offsets[i], 
                fontsize=9, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", alpha=0.8))

ax.set_xlabel(r'$n\lambda$ (pm)', fontsize=12, fontweight='bold')
ax.set_ylabel(r'$\sin\theta$', fontsize=12, fontweight='bold')
ax.set_title('Single Crystal NaCl: Bragg Reflection Calibration Curve', fontsize=13, fontweight='bold', pad=12)
ax.grid(True)
ax.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
plt.tight_layout()
plt.savefig('single_crystal_bragg_fit.png', dpi=300)
plt.close()

# ==========================================
# 2. Powder XRD Analysis (Cu tube)
# ==========================================
# lambda_Cu = 154.184 pm (1.54184 A, standard Cu K_alpha)
lambda_Cu_pm = 154.184

powder_data = [
    {"theta_deg": 15.3, "hkl": "(200)", "h": 2, "k": 0, "l": 0, "I": 17.2},
    {"theta_deg": 22.5, "hkl": "(220)", "h": 2, "k": 2, "l": 0, "I": 7.2},
    {"theta_deg": 28.0, "hkl": "(222)", "h": 2, "k": 2, "l": 2, "I": 2.4},
    {"theta_deg": 33.0, "hkl": "(400)", "h": 4, "k": 0, "l": 0, "I": 2.4},
    {"theta_deg": 37.5, "hkl": "(420)", "h": 4, "k": 2, "l": 0, "I": 2.8},
]

theta_pwd_deg = np.array([p["theta_deg"] for p in powder_data])
theta_pwd_rad = np.radians(theta_pwd_deg)
sin_theta_pwd = np.sin(theta_pwd_rad)
sin2_theta_pwd = sin_theta_pwd**2

hkl_sq = np.array([p["h"]**2 + p["k"]**2 + p["l"]**2 for p in powder_data])
d_spacings_pm = lambda_Cu_pm / (2.0 * sin_theta_pwd)
a0_pwd_individual = d_spacings_pm * np.sqrt(hkl_sq)

# Quadratic fit: sin^2(theta) = m * (h^2+k^2+l^2) + c
slope_pwd, intercept_pwd = np.polyfit(hkl_sq, sin2_theta_pwd, 1)
a0_pwd_fit = lambda_Cu_pm / (2.0 * np.sqrt(slope_pwd))

print("\n--- POWDER XRD ---")
for i, p in enumerate(powder_data):
    print(f"(hkl)={p['hkl']}, s={hkl_sq[i]}, theta={p['theta_deg']} deg, sin(theta)={sin_theta_pwd[i]:.5f}, d={d_spacings_pm[i]:.2f} pm, a_0={a0_pwd_individual[i]:.2f} pm")
print(f"Mean a_0 = {np.mean(a0_pwd_individual):.2f} pm")
print(f"Fit Slope = {slope_pwd:.7f}, Intercept = {intercept_pwd:.5f} => a_0 = {a0_pwd_fit:.2f} pm")

# Plot Powder XRD: sin^2(theta) vs (h^2 + k^2 + l^2)
fig, ax = plt.subplots(figsize=(7, 5), dpi=300)
ax.scatter(hkl_sq, sin2_theta_pwd, color='#2ca02c', s=70, zorder=5, label='Indexed Diffraction Peaks')

x_fit_pwd = np.linspace(2, 22, 200)
y_fit_pwd = slope_pwd * x_fit_pwd + intercept_pwd
ax.plot(x_fit_pwd, y_fit_pwd, color='#ff7f0e', linestyle='-', linewidth=2, 
        label=f'Linear Fit: $\\sin^2\\theta = {slope_pwd:.6f}\\,(h^2+k^2+l^2) {intercept_pwd:+.4f}$\n$a_0 = \\lambda/(2\\sqrt{{m}}) = {a0_pwd_fit:.2f}$ pm ($R^2 = {np.corrcoef(hkl_sq, sin2_theta_pwd)[0,1]**2:.4f}$)')

for i, p in enumerate(powder_data):
    ax.annotate(f"{p['hkl']}\n$\\theta={p['theta_deg']}^\\circ$", 
                (hkl_sq[i], sin2_theta_pwd[i]),
                textcoords="offset points", xytext=(-15, 10 if i%2==0 else -25), 
                fontsize=9, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", alpha=0.8))

ax.set_xlabel(r'$h^2 + k^2 + l^2$', fontsize=12, fontweight='bold')
ax.set_ylabel(r'$\sin^2\theta$', fontsize=12, fontweight='bold')
ax.set_title('Powder NaCl: Quadratic Form Indexing Fit', fontsize=13, fontweight='bold', pad=12)
ax.grid(True)
ax.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
plt.tight_layout()
plt.savefig('powder_nacl_indexing_fit.png', dpi=300)
plt.close()


