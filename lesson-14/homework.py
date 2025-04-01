import numpy as np
from PIL import Image


# Task 1: Fahrenheit to Celsius conversion function using numpy.vectorize
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


temps_fahrenheit = np.array([32, 68, 100, 212, 77])
temps_celsius = np.vectorize(fahrenheit_to_celsius)(temps_fahrenheit)
print("Task 1:")
print("Fahrenheit:", temps_fahrenheit)
print("Celsius:", temps_celsius)
print()


# Task 2: Custom function for power calculation using numpy.vectorize
def power_function(x, y):
    return x**y


numbers1 = np.array([2, 3, 4, 5])
numbers2 = np.array([1, 2, 3, 4])
result = np.vectorize(power_function)(numbers1, numbers2)
print("Task 2:")
print("Numbers 1:", numbers1)
print("Numbers 2:", numbers2)
print("Power result:", result)
print()

# Task 3: Solving a system of equations using numpy
coefficients = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
constants = np.array([7, 4, 5])
solution = np.linalg.solve(coefficients, constants)
print("Task 3:")
print("Solution (x, y, z):", solution)
print()

# Task 4: Solving electrical circuit equations using numpy
circuit_coefficients = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
circuit_constants = np.array([12, -5, 15])
currents = np.linalg.solve(circuit_coefficients, circuit_constants)
print("Task 4:")
print("Currents (I1, I2, I3):", currents)
print()


# Image Manipulation using NumPy and PIL
def flip_image(image):
    flipped_lr = np.fliplr(image)
    flipped_ud = np.flipud(flipped_lr)
    return flipped_ud


def add_random_noise(image):
    noise = np.random.randint(0, 50, size=image.shape)
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image


def brighten_channels(image, brightness=40):
    brightened_image = np.clip(image + brightness, 0, 255).astype(np.uint8)
    return brightened_image


def apply_mask(image, mask_position=(100, 100), mask_size=(100, 100)):
    x, y = mask_position
    w, h = mask_size
    image_masked = image.copy()
    image_masked[x : x + w, y : y + h] = [0, 0, 0]
    return image_masked


# Load the image
image_path = "images/birds.jpg"
original_image = np.array(Image.open(image_path))

# Perform manipulations
flipped_image = flip_image(original_image)
noisy_image = add_random_noise(original_image)
brightened_image = brighten_channels(original_image)
masked_image = apply_mask(original_image)

# Save modified images back using PIL
Image.fromarray(flipped_image).save("images/birds_flipped.jpg")
Image.fromarray(noisy_image).save("images/birds_noisy.jpg")
Image.fromarray(brightened_image).save("images/birds_brightened.jpg")
Image.fromarray(masked_image).save("images/birds_masked.jpg")

print("Image manipulations completed and saved successfully.")
