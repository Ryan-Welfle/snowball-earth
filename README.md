# Welcome to my Snowball Earth Simulator

This is a program based on the "Iterative Runaway Ice-Albedo Feedback Model" that is a part of the "Global Warming II: Create You Own Models in Python" Coursera course, provided by the University of Chicago.

This main output of this program is a multiple line graph, that simulates decreasing planetary temperatures that eventually drop dramatically into temperatures that would create a "snowball earth", based on a positive cooling feedback loop. 

The decreasing planetary temperatures (marked along the graph's y-axis) are a function of decreasing incoming sunlight heat (represented by 'L' in the code, in W/m2), and simultaneous increases of albedo values; both the 'L' and albedo values derive their values based on the other. Each blue line is created through a set of 100 (default) iterations (marked along the graph's x-axis), each with a constant 'L' value being fed into temperature calculations, which then feed into albedo calculations. A "snowball earth" scenario is reached when average global temperatures drop below ~223.15 °K; the program takes note of the set of iterations that this occurs on, and outputs the 'L' value, the albedo value, and the highest and lowest temperature of the "snowball" iteration-set (along with the multiple line graph).

## What the program does, in simple terms

| Mean Planetary Temperature    | Planetary Albedo  |
|:------------------------------|:------------------|
| 265                           | 0.15              |
| 255                           | 0.25              |
| 245                           | 0.35              |
| 235                           | 0.45              |
| 225                           | 0.55              |
| 215                           | 0.65              |

After these values are inputted, they work in conjunction with a few constants to create:

1. Heat Capacity: the ability of the simulated water to retain incoming heat (sunlight) per second
2. Heat Content: the amount of heat present on the simulated Earth/water per second
3. Heat In: a fixed amount of incoming heat (based on constants of sunlight [L] and albedo values) per second
4. Heat Out: a growing amount of outgoing heat (based on constants of epsilon, sigma, as well as growing temperature values)

Along the way, temperature per time-step is appended to a temperature array, that grows in tandem with a time-step array, for the purposes of plotting them on the final simulation graph.

Have fun using the program!

