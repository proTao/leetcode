import numpy as np

class GP:
    def __init__(self, lambda_):
        self.lambda_ = lambda_

    def _k(x, x_):
        return exp()

    def _kernel_matrix(self, X):
        # matrix of xi-xj
        # distance = np.stack([X for _ in range(X.shape[0])], axis=1) - X
        # another emplement
        distance = np.expand_dims(X, 1) - np.expand_dims(X, 0)

        # matrix = ||xi-xj||^2
        distance = np.exp(self.lambda_ * np.sum(distance**2, axis=2))
        return distance

    def _kernel_vector(self, X, new_x):
        distance = X - new_x
        distance = np.exp(self.lambda_ * np.sum(distance**2, axis=1))
        return distance

    def fit(X, y):
        self.empirical_kernel_matrix = self._kernal_matrix(X)
        self.y = y
    def predict_one(x):
        pass