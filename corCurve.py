import numpy as np
import matplotlib.pyplot as plt

# Given data matrix (rows: A1-E1, columns: A2-E2)
data = np.array([
    [0.12, 3.74, 1.52, 3.31, 4.31],  # A1
    [3.81, 0.08, 0.97, 3.00, 3.85],  # B1
    [1.53, 1.21, 0.98, 1.22, 2.21],  # C1
    [3.24, 3.00, 0.99, 0.25, 3.45],  # D1
    [4.30, 3.65, 2.45, 3.46, 0.17]   # E1
])

# Extract genuine and impostor comparisons
genuine = np.diag(data)  # Diagonal elements (A1-A2, B1-B2, ..., E1-E2)
impostor = data[~np.eye(data.shape[0], dtype=bool)].flatten()  # Off-diagonal elements

# Sort scores for threshold sweeping
genuine_sorted = np.sort(genuine)
impostor_sorted = np.sort(impostor)

# Initialize arrays for FMR and FNMR
thresholds = np.unique(np.concatenate([genuine_sorted, impostor_sorted]))
fmr = np.zeros_like(thresholds)
fnmr = np.zeros_like(thresholds)

# Calculate FMR and FNMR for each threshold
for i, threshold in enumerate(thresholds):
    fmr[i] = np.sum(impostor <= threshold) / len(impostor)
    fnmr[i] = np.sum(genuine > threshold) / len(genuine)

# Plot ROC curve (FMR vs 1-FNMR)
plt.figure(figsize=(8, 6))
plt.plot(fmr * 100, (1 - fnmr) * 100, marker='o', linestyle='-', color='b')
plt.xlabel(' (FMR) %')
plt.ylabel('True Match Rate (1-FNMR) %')
plt.title('ROC Curve')
plt.grid(True)
plt.xlim([-.5, 20])  # Focus on low FMR range
plt.ylim([-.5, 103])  # Extend y-axis to 100% for clarity
plt.show()

# Print key points (FMR, 1-FNMR)
print("Key ROC Curve Points (FMR %, 1-FNMR %):")
for f, t in zip(fmr, 1 - fnmr):
    print(f"{f * 100:.1f}, {t * 100:.1f}")