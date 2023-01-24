"""
/usr/local/bin/python3 /Users/kristenfinley/Documents/datafun-02-functions/user_stats.py
(base) kristenfinley@Kristens-MBP datafun-02-functions % /usr/local/bin/python3 /Users/kristenfinley/Documents/datafun-02-functions/u
ser_stats.py

=============================================================

On-base plus slugging (OPS) is a sabermetric baseball statistic calculated as the sum of a player's on-base percentage and slugging percentage.

The ability of a player both to get on base and to hit for power, two important offensive skills, are represented.
An OPS of .800 or higher in Major League Baseball puts the player in the upper echelon of hitters.
Typically, the league leader in OPS will score near, and sometimes above, the 1.000 mark.

Source: https://en.wikipedia.org/wiki/On-base_plus_slugging#:~:text=On%2Dbase%20plus%20slugging%20(OPS,base%20percentage%20and%20slugging%20percentage.


Paul Goldschmidt's OPS in 2022 was 0.981!!! Way to go, Goldie!


=============================================================

Here are the OPSs of all the 2022 St. Louis Cardinal's players: [0.981, 0.725, 0.891, 0.773, 0.7, 0.695, 0.788, 0.721, 0.895, 0.673, 0.601, 0.698, 0.742, 0.535, 0.53, 0.515, 0.535, 0.492, 0.407, 0.563, 0.302, 0]

Descriptive statistics about the Cardinal's OPS:
   mean=0.626
   median=0.684
   mode=0.535
   highest=0.981
   lowest=0.000
   var=0.046
   stddev=0.215



=============================================================


Let's look at more hitting data from the 2022 Redbirds

Total Runs:[106, 95, 73, 64, 56, 56, 53, 44, 42, 35, 28, 28, 27, 19, 19, 17, 4, 3, 2, 1, 0, 0]

Batting Averages:[0.317, 0.265, 0.293, 0.281, 0.228, 0.236, 0.228, 0.226, 0.27, 0.256, 0.215, 0.267, 0.253, 0.214, 0.157, 0.189, 0.188, 0.15, 0.154, 0.176, 0.111, 0]



=============================================================


Is there a relationship between runs, batting averages, and OPS?

   correlation between runs and batting averages = 0.762
   correlation between batting averages and OPS = 0.961
   correlation between runs and OPS = 0.773

There appears to be a strong correlation between OPS and batting averages,
so we will use these two variables to predict a players batting average based off of an OPS of 1.000.

Let OPS = the x values:[0.981, 0.725, 0.891, 0.773, 0.7, 0.695, 0.788, 0.721, 0.895, 0.673, 0.601, 0.698, 0.742, 0.535, 0.53, 0.515, 0.535, 0.492, 0.407, 0.563, 0.302, 0]

Let Batting Averages = the y values:[0.317, 0.265, 0.293, 0.281, 0.228, 0.236, 0.228, 0.226, 0.27, 0.256, 0.215, 0.267, 0.253, 0.214, 0.157, 0.189, 0.188, 0.15, 0.154, 0.176, 0.111, 0]

Calculate the slope and intercept of a best fit straight line:

   slope = 0.315
   intercept = 0.016

We will use our best fit line to predict an x value from the curve.

   So if a player would have had an OPS of = 1.000,
   we predict their batting average would have been 0.330.



Source of MLB stats: https://www.baseball-reference.com/teams/STL/2022.shtml
(base) kristenfinley@Kristens-MBP datafun-02-functions % 
"""