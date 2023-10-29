import numpy 
import skfuzzy as fuzz
import matplotlib.pyplot as plt
# Define the input variable
x = numpy.arange(0, 10, 0.1)
# Define the Gaussian membership function
mf = fuzz.gaussmf(x, 5, 2)
# Plot the membership function
plt.plot(x, mf)
plt.show()
# Fuzzify the input variable
z = fuzz.interp_membership(x, mf, 6.5)
# Print the fuzzified value
print(z)
# Defuzzify the fuzzified value using centre-of-gravity defuzzifier
y = fuzz.defuzz(x, mf, 'centroid')
# Print the defuzzified value
print(y)
