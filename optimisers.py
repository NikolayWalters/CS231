# Adagrad
# Assume the gradient dx and parameter vector x
cache += dx**2
x += - learning_rate * dx / (np.sqrt(cache) + eps)
# weights that receive high gradients will have their effective learning rate reduced
# weights that receive small or infrequent updates will have their effective learning rate increased
# eps - smoothing term, usually 1e-4 - 1e-8
# downside: the monotonic learning rate usually proves too aggressive and stops learning too early

# RMSprop
cache = decay_rate * cache + (1 - decay_rate) * dx**2
x += - learning_rate * dx / (np.sqrt(cache) + eps)
# decay_rate typically [0.9, 0.99, 0.999]

# Adam
# Conceptually, RMSprop with momentum
m = beta1*m + (1-beta1)*dx
v = beta2*v + (1-beta2)*(dx**2)
x += - learning_rate * m / (np.sqrt(v) + eps)
# with bias correction mechnaism:
# t is your iteration counter going from 1 to infinity
m = beta1*m + (1-beta1)*dx
mt = m / (1-beta1**t)
v = beta2*v + (1-beta2)*(dx**2)
vt = v / (1-beta2**t)
x += - learning_rate * mt / (np.sqrt(vt) + eps)