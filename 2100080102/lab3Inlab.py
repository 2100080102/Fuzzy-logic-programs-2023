import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
%matplotlib inline
x = np.arange(4, 7, 0.1)
## LINEAR
# Create the membership functions
veryshort = fuzz.trimf(x, [3.5, 3.7, 4.2])
short = fuzz.trimf(x, [4.4, 4.6, 4.8])
normal = fuzz.trimf(x, [4.9, 5.3, 5.7])
tall = fuzz.trimf(x, [6.0,6.2, 6.3])
verytall = fuzz.trimf(x, [6.5, 6.7, 6.9])
# Plot the results of the linear fuzzy membership
plt.figure()
plt.plot(x,veryshort, 'b', linewidth=1.5, label='very_short')
plt.plot(x,short , 'k', linewidth=1.5, label='short')
plt.plot(x,normal, 'm', linewidth=1.5, label='normal')
plt.plot(x,tall, 'r', linewidth=1.5, label='tall')
plt.plot(x,verytall, 'y', linewidth=1.5, label='verytall')
plt.title('heights,fuzzy membership')
plt.ylabel('Membership')
plt.xlabel('HEIGHT OF PEOPLE')
plt.legend(loc='center right', bbox_to_anchor=(1.50, 0.5),
          ncol=1, fancybox=True, shadow=True);

## GAUSSIAN
x = np.arange(1, 10, 0.1)
# Create the membership functions
xwhite = fuzz.gaussmf(x, 2, 3)
xmoderate = fuzz.gaussmf(x, 5, 3)
xblack = fuzz.gaussmf(x, 8, 3)
# Plot the results of the gaussian fuzzy membership
plt.figure()
plt.plot(x, xwhite, 'b', linewidth=1.5, label='white')
plt.plot(x, xmoderate, 'k', linewidth=1.5, label='moderate')
plt.plot(x, xblack, 'm', linewidth=1.5, label='black')
plt.title('race of people, Gaussian Fuzzy')
plt.ylabel('Membership')
plt.xlabel('Race of people')
plt.legend(loc='center right', bbox_to_anchor=(1.5, 0.3),
          ncol=1, fancybox=True, shadow=True);
