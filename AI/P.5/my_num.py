import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.datasets import fetch_openml


mnist = fetch_openml('mnist_784', version=1, as_frame=False)
X, y = mnist["data"], mnist["target"]
y = y.astype(np.uint8)


ones_indices = np.where(y == 1)[0]
eights_indices = np.where(y == 8)[0]



def plot_18(one_idx, eight_idx, position):
    plt.subplot(5, 2, position * 2 - 1)
    plt.imshow(X[one_idx].reshape(28, 28), cmap=mpl.cm.binary)
    plt.axis('off')

    plt.subplot(5, 2, position * 2)
    plt.imshow(X[eight_idx].reshape(28, 28), cmap=mpl.cm.binary)
    plt.axis('off')



plt.figure(figsize=(10, 20))
for i in range(5):
    plot_18(ones_indices[i], eights_indices[i], i + 1)

plt.tight_layout()
plt.show()