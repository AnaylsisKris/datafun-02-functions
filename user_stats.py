"""
Name: Kristen Finley
Course: 44-608 Data Analytics Fundamentals
Date: 18Jan2023
Domain: Baseball
Project: 2
Task: 4

This example illustrates basic analytics using just the built-in statistics module.

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# defines a variable with some univariant data

stl_OPS = [
    0.981,
    0.725,
    0.891,
    0.773,
    0.7,
    0.695,
    0.788,
    0.721,
    0.895,
    0.673,
    0.601,
    0.698,
    0.742,
    0.535,
    0.53,
    0.515,
    0.535,
    0.492,
    0.407,
    0.563,
    0.302,
    0,
]

# Task 4) Averages and Measure of Tendency and Spread

mean = statistics.mean(stl_OPS)
median = statistics.median(stl_OPS)
mode = statistics.mode(stl_OPS)
var = statistics.variance(stl_OPS)
stdev = statistics.stdev(stl_OPS)
lowest = min(stl_OPS)
highest = max(stl_OPS)
print()
print("=============================================================")
print()
print(
    "On-base plus slugging (OPS) is a sabermetric baseball statistic calculated as the sum of a player's on-base percentage and slugging percentage."
)
print()
print(
    "The ability of a player both to get on base and to hit for power, two important offensive skills, are represented."
)
print(
    "An OPS of .800 or higher in Major League Baseball puts the player in the upper echelon of hitters."
)
print(
    "Typically, the league leader in OPS will score near, and sometimes above, the 1.000 mark."
)
print()
print(
    "Source: https://en.wikipedia.org/wiki/On-base_plus_slugging#:~:text=On%2Dbase%20plus%20slugging%20(OPS,base%20percentage%20and%20slugging%20percentage."
)
print()
print()
print("Paul Goldschmidt's OPS in 2022 was 0.981!!! Way to go, Goldie!")
print()
print()
print("=============================================================")
print()
print(f"Here are the OPSs of all the 2022 St. Louis Cardinal's players: {stl_OPS}")
print()
print("Descriptive statistics about the Cardinal's OPS:")
print(f"   mean={mean:.3f}")
print(f"   median={median:.3f}")
print(f"   mode={mode:.3f}")
print(f"   highest={highest:.3f}")
print(f"   lowest={lowest:.3f}")
print(f"   var={var:.3f}")
print(f"   stddev={stdev:.3f}")
print()
print()
print()
print("=============================================================")
print()
stl_runs = [
    106,
    95,
    73,
    64,
    56,
    56,
    53,
    44,
    42,
    35,
    28,
    28,
    27,
    19,
    19,
    17,
    4,
    3,
    2,
    1,
    0,
    0,
]
b_avgs = [
    0.317,
    0.265,
    0.293,
    0.281,
    0.228,
    0.236,
    0.228,
    0.226,
    0.27,
    0.256,
    0.215,
    0.267,
    0.253,
    0.214,
    0.157,
    0.189,
    0.188,
    0.15,
    0.154,
    0.176,
    0.111,
    0,
]
print()
print("Let's look at more hitting data from the 2022 Redbirds")
print()
print(f"Total Runs:{stl_runs}")
print()
print(f"Batting Averages:{b_avgs}")
print()
print()
print()
print("=============================================================")
print()

# if the lists are not the same size, print an error and quit the program
if len(stl_runs) != len(stl_OPS):
    print("ERROR: The related sets are not the same size.")
    print(f"      {len(stl_runs)}!={len(stl_OPS)}")
    quit()

try:

    runs_bavg_corr = statistics.correlation(stl_runs, b_avgs)
    OPS_bavgs_corr = statistics.correlation(stl_OPS, b_avgs)
    OPS_runs_corr = statistics.correlation(stl_runs, stl_OPS)

except Exception as e:
    print(f"ERROR:    {e}")
    print("Try updating to Python 3.10 or greater.")
    print("Or select your updated conda environment in VS Code.")
    print("VS Code Menu / View / Command Palette / Python: Select Interpretor")
    quit()

print()
print(
    "Is there a relationship between runs, batting averages, and OPS?",
)
print()
print(f"   correlation between runs and batting averages = {runs_bavg_corr:.3f}")
print(f"   correlation between batting averages and OPS = {OPS_bavgs_corr:.3f}")
print(f"   correlation between runs and OPS = {OPS_runs_corr:.3f}")
print()
# Calls linear_regression() function -
# and gets back 2 values: slope and intercept describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(stl_OPS, b_avgs)

# Chooses an x value off in the future (future x)
future_OPS = 1.000

# Extends the line out into the unknown future and read the value (of future y)
future_bavgs = slope * future_OPS + intercept
print("There appears to be a strong correlation between OPS and batting averages,")
print(
    "so we will use these two variables to predict a players batting average based off of an OPS of 1.000."
)
print()
print(f"Let OPS = the x values:{stl_OPS}")
print()
print(f"Let Batting Averages = the y values:{b_avgs}")
print()
print("Calculate the slope and intercept of a best fit straight line:")
print()
print(f"   slope = {slope:.3f}")
print(f"   intercept = {intercept:.3f}")
print()
print("We will use our best fit line to predict an x value from the curve.")
print()
print(f"   So if a player would have had an OPS of = {future_OPS:.3f},")
print(f"   we predict their batting average would have been { future_bavgs:.3f}.")
print()
print()
print()
print("Source of MLB stats: https://www.baseball-reference.com/teams/STL/2022.shtml")
