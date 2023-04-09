# L1 distance (sum of absolute value differences)
distances = np.sum(np.abs(self.Xtr - X[i,:]), axis = 1)

# Euclidian / L2
distances = np.sqrt(np.sum(np.square(self.Xtr - X[i,:]), axis = 1))
# L2 distance prefers many medium disagreements to one big one
