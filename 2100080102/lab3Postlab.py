import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define temperature categories and their mean and standard deviation values
categories = ['Warm', 'Moderate', 'Cold', 'Hot']
categoryparams = {
    'Warm': {'mean': 25, 'std_dev': 3},
    'Moderate': {'mean': 15, 'std_dev': 4},
    'Cold': {'mean': 5, 'std_dev': 3},
    'Hot': {'mean': 35, 'std_dev': 5}
}

# Generate x values for the temperature range
x = np.linspace(0, 50, 100)

# Create subplots for each membership function
plt.figure(figsize=(12, 6))

for category in categories:
    params = categoryparams[category]
    pdf = norm.pdf(x, params['mean'], params['std_dev'])

    plt.plot(x, pdf, label=category)

plt.title('Gaussian Membership Functions for Temperature Categories')
plt.xlabel('Temperature')
plt.ylabel('Membership')
plt.legend()
plt.grid(True)
plt.show()
