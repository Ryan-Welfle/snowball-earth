import numpy
import matplotlib.pyplot as plt

n_iterations = 100             #number of iterations per L value
m_albedo = -1e-2                #slope of albedo function (see README)
b_albedo = 2.8                  #intercept of albedo function (see README)
sigma = 5.67e-8                 #sigma value, for calculating temperature


x = []                          #list for x-values (iterations)
y = []                          #list for y-values (temperature)
snowball_L = 0                  #placeholder for L value in "snowball" iter
snowball_albedo = 0             #placeholder for albedo "snowball" iter
largest_diff = 0                #placeholder for temp difference of iter with largest temp difference (which would be "snowball" iter)
snowball_high_temp = 0          #placeholder for highest temperature in "snowball" iter
snowball_low_temp = 0           #placeholder for lowest temperature in "snowball" iter

LRange = [1150, 1350]           #range of L values to use for this graph

L = LRange[1]                   #setting the L value at the highest value, to then iterate towards lowest L value
albedo = 0.15                   #setting the albedo at a "low" value, which will increase during while loop iterations
       
while L > LRange[0] - 1:                                            #setting up while loop so that iterations only happen within LRange, going down
    snowball_finder = []                                            #empty list to help with finding "snowball" iter
    for iter in range (0, n_iterations):                            #setting up for loop, to do 100 iterations per L value
        temperature = pow(L * (1 - albedo)/(4 * sigma), 0.25)       #calculating temperature
        albedo = temperature * m_albedo + b_albedo                  #calculating new albedo based on iteration's temperature
        albedo = min (albedo, 0.7)                                  #keeping albedo within a minimum albedo
        albedo = max (albedo, 0.15)                                 #keeping albedo within a maximum albedo
        x.append(iter)                                              #adding iteration number to x-list
        y.append(temperature)                                       #adding temperature to y-list
        snowball_finder.append(temperature)                         #appending n_iterations temps to list to prepare for finding "snowball" iter
    temperature_diff = max(snowball_finder)-min(snowball_finder)    #calculating temp differ between highest and lowest temp in current iter
    if temperature_diff>=largest_diff:                              #higher temp diffs will always replace other high temp diffs until the "snowball" iter is reached
        largest_diff=temperature_diff
        snowball_L=L
        snowball_albedo=albedo
        snowball_high_temp = max(snowball_finder)
        snowball_low_temp = min(snowball_finder)
    x.append(numpy.nan)                         #adding a non-number at the end of each L iteration cycle in x-list to have clear break between iteration slopes
    y.append(numpy.nan)                         #adding a non-number at the end of each L iteration cycle in y-list to have clear break between iteration slopes
    L = L - 1                                   #changing L-value, so that new iterations can be done for the next L-value


print('\nSNOWBALL EARTH SIMULATOR\n')
print('The conditions that create a "snowball Earth" are as follows:')
print(f'Incoming sunlight heat of: {snowball_L} W/m2')
print(f'An albedo of: {snowball_albedo}')
print(f'\nTemperatures drop from {snowball_high_temp}°K to {snowball_low_temp}°K with the above conditions')
    
plt.plot(x, y)                                                                                      #plotting temperature over iterations

plt.suptitle('Snowball Earth Simulator', weight='bold')                                             #title for plot
plt.title(f'Temperature over Iterations for L-Values {LRange[0]}-{LRange[1]} W/m2', fontsize=10)    #subtitle for plot
plt.axhline(y=223.15, color='r', linestyle='--')
plt.annotate('Average "Snowball Earth" Temperature Below Here',(5.0,224.15), color='r')
plt.xlabel('Iterations')                                                                            #title for x-axis
plt.ylabel('Temperature (in ˚K)')                                                                   #title for y-axis

plt.show()
