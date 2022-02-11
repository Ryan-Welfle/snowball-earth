# Welcome to my Snowball Earth Simulator

This is a program based on the "Iterative Runaway Ice-Albedo Feedback Model" that is a part of the "Global Warming II: Create You Own Models in Python" Coursera course, provided by the University of Chicago.

The main output of this program is a multiple line graph, that simulates decreasing planetary temperatures that eventually drop dramatically into temperatures that would create a "snowball earth" scenario, based on a positive cooling feedback loop. 

The decreasing planetary temperatures (marked along the graph's y-axis) are a function of decreasing incoming sunlight heat (represented by 'L' in the code, in W/m2), and simultaneous increases of albedo values; both the 'L' and albedo values derive their values in tandem with each other. Each blue line is created through a set of 100 (default) iterations (marked along the graph's x-axis), each with a constant 'L' value being fed into temperature calculations, which then feed into albedo calculations. A "snowball earth" scenario is reached when average global temperatures drop below ~223.15 °K; the program takes note of the set of iterations that this occurs on, and outputs the 'L' value, the albedo value, and the highest and lowest temperature of the "snowball" iteration-set (along with the multiple line graph).

## What the program does, in simple terms

Negative slope (m) and y-intercept (b) values are derived from the following table below (provided by the Global Warming II course), to ensure that as mean planetary temperature decrease, albedo increases. These are set to variables in the code.

| Mean Planetary Temperature    | Planetary Albedo  |
|:------------------------------|:------------------|
| 265                           | 0.15              |
| 255                           | 0.25              |
| 245                           | 0.35              |
| 235                           | 0.45              |
| 225                           | 0.55              |
| 215                           | 0.65              |

The default "L" range is set between 1150-1350 W/m2, and the default albedo range is set between 0.15 and 0.7 (the highest albedo representing highly reflective "bare ice").

Beginning our first iteration-set with the "L" value of 1150 W/m2, temperature is derived using "L" and sigma values; this temperature equation is a synthesis of the "HeatIn" and "HeatOut" equations from my "naked-planet" program.

Albedo is calculated using basic slope formula, using our derived "m" and "b" variables, and subbing in our "temperature" value for the pseudo-"x" value (making our pseudo-"y" value our albedo). 

At the end of each iteration, we append temperature to the "y" axis (via our "y" list), and our iteration number (out of 100) to the "x" axis (via our "x" list). While we don't technically append our albedo values to any true axis, deriving our albedo values through the derived slope values (and then plugging those albedo values into subsequent temperature equations) ensures that our temperature values are a function of our albedo values.

Before the end of each while loop iteration, the program checks to see which iteration-set represents the tip-over into the "snowball earth" scenario by always take note of the greatest temperature difference per iteration-set thus far (as well its its associated values). At the end of each while loop iteration, the "L" value decreases by a (default) 10 W/m2, and a new iteration-set gets calculated. Each iteration-set slowly increases the albedo values by nature of the slope values.

When the iteration-sets are completed, the program outputs the values associated with the "snowball earth" scenario, as well as the multiple line graph to show this process visually.

## Further relevant notes

The planetary temperature used to indicate when a "snowball earth" scenario has been reached, as well as the albedo range for "bare ice", can be found here:
https://www.snowballearth.org/what.html

The way the program code is set up shows the approximate "L" and albedo values that will almost always create the "snowball earth" scenario (even when playing arounding with some of the initial "L" and albedo values). Increasing the maximum albedo value (within the code) will have little effect on changing the maximum "L" value for the "snowball earth" scenario, since the "L" value will always hit that scenario once the upper range of the "bare ice" albedo is encountered. However, feel free to experiment with tinkering with default values (like more finely decreasing "L" values).

Have fun using the program!

