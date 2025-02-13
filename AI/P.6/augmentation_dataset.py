import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml




def shift_image(image, direction):
    """
    Сдвигает изображение на 1 пиксель в указанном направлении

    Параметры:
    image: одномерный массив 784 пикселей
    direction: 'left', 'right', 'up', или 'down'

    Возвращает:
    Сдвинутое изображение в виде одномерного массива
    """
    # Преобразование в 2D массив
    img_2d = image.reshape(28, 28)
    shifted = np.zeros_like(img_2d)

    if direction == 'left':
        shifted[:, :-1] = img_2d[:, 1:]
    elif direction == 'right':
        shifted[:, 1:] = img_2d[:, :-1]
    elif direction == 'up':
        shifted[:-1, :] = img_2d[1:, :]
    elif direction == 'down':
        shifted[1:, :] = img_2d[:-1, :]

    # Возвращаем в 1D формат
    return shifted.reshape(784)


def augment_dataset(x_train, y_train):
    """
    Создает расширенный набор данных, добавляя сдвинутые версии каждого изображения

    Возвращает:
    x_augmented, y_augmented: расширенные наборы данных и меток
    """
    directions = ['left', 'right', 'up', 'down']
    n_samples = x_train.shape[0]

    # Создаем массивы для расширенного набора (оригинал + 4 сдвинутых версии)
    x_augmented = np.zeros((n_samples * 5, 784))
    y_augmented = np.zeros((n_samples * 5, 10))

    for i in range(n_samples):
        # Добавляем оригинальное изображение
        x_augmented[i * 5] = x_train[i]
        y_augmented[i * 5] = y_train[i]

        # Добавляем сдвинутые версии
        for j, direction in enumerate(directions):
            x_augmented[i * 5 + j + 1] = shift_image(x_train[i], direction)
            y_augmented[i * 5 + j + 1] = y_train[i]

    return x_augmented, y_augmented





def visualize_augmentation(image):
    """
    Визуализирует оригинальное изображение и его сдвинутые версии

    Параметры:
    image: одномерный массив 784 пикселей
    """
    directions = ['original', 'left', 'right', 'up', 'down']
    fig, axes = plt.subplots(1, 5, figsize=(15, 3))

    # Показываем оригинальное изображение
    axes[0].imshow(image.reshape(28, 28), cmap='gray')
    axes[0].set_title('Original')
    axes[0].axis('off')

    # Показываем сдвинутые версии
    for i, direction in enumerate(directions[1:], 1):
        shifted = shift_image(image, direction)
        axes[i].imshow(shifted.reshape(28, 28), cmap='gray')
        axes[i].set_title(f'Shift {direction}')
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()


def compare_datasets(x_train, x_train_augmented):
    """
    Выводит статистику по оригинальному и расширенному наборам данных
    """
    print(f"Размер оригинального набора данных: {x_train.shape[0]} изображений")
    print(f"Размер расширенного набора данных: {x_train_augmented.shape[0]} изображений")
    print(f"Коэффициент увеличения: {x_train_augmented.shape[0] / x_train.shape[0]:.1f}x")
def main():
    mnist = fetch_openml('mnist_784', version=1, as_frame=False)
    train_images = mnist["data"].astype('float32') / 255
    train_labels = mnist["target"].reshape(-1, 1).astype('int32')
    train_labels = np.eye(10)[train_labels]
    print(train_labels[0])

    # Создание расширенного набора данных
    train_images_augmented, train_labels_augmented = augment_dataset(train_images, train_labels)

    # Вывод статистики
    compare_datasets(train_images, train_images_augmented)

    # Визуализация примера аугментации
    sample_idx = np.random.randint(0, len(train_images_augmented))
    print("\nВизуализация примера аугментации для случайного изображения:")
    visualize_augmentation(train_images_augmented[sample_idx])


if __name__ == "__main__":
    main()