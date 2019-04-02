import numpy as np

class GP:
    def __init__(self):
        self.kernel_l = 1
        self.kernel_sigma = 5
        self.alpha = 1

    def _K_matrix(self, X):
        # matrix of xi-xj
        # distance = np.stack([X for _ in range(X.shape[0])], axis=1) - X
        # another emplement
        distance = np.expand_dims(X, 1) - np.expand_dims(X, 0)

        # matrix = ||xi-xj||^2
        distance = self.kernel_sigma ** 2 * np.exp(-np.sum(distance**2, axis=2) / (self.kernel_l * 2))
        return self._K_star_matrix(X, X)

    def _K_star_matrix(self, X, new_x):
        distance = np.expand_dims(X, 1) - np.expand_dims(new_x, 0)
        distance = self.kernel_sigma ** 2 * np.exp(-np.sum(distance**2, axis=2) / (self.kernel_l * 2))
        return distance

    def fit(self, X, y):
        self.K = self._K_matrix(X) + np.eye(len(y)) * np.std(y)* self.alpha
        self.X = X
        self.y = y
        self.invK = np.linalg.inv(self.K)

    def predict(self, X_test):
        K_star_star = self._K_matrix(X_test)
        K_star = self._K_star_matrix(self.X, X_test)
        mu = np.matmul(np.matmul(K_star.T, self.invK), self.y.T)
        sigma = K_star_star - np.matmul(np.matmul(K_star.T, self.invK), K_star)
        return mu, sigma
    
if __name__ == "__main__":
    from matplotlib  import pyplot as plt
    X = np.array([[1],[2],[3],[4],[5],[8]])
    y = np.array([1,3,5,8,9,6])
    gp = GP()
    gp.fit(X, y)
    x = []
    mean = []
    std = []
    for i in range(100):
        x.append(i/10)
        asnwer = gp.predict(np.array([[i/10]]))
        mean.append(asnwer[0][0])
        std.append(asnwer[1][0][0])
    plt.plot(x, mean)
    plt.scatter(X.T[0], y, marker='o')
    plt.fill_between(x, np.array(mean) - np.array(std),
                     np.array(mean) + np.array(std), alpha=0.1,
                     color="r")
    plt.show()
    