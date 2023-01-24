"""
Name: Kristen Finley
Course: 44-608 Data Analytics Fundamentals
Date: 18Jan2023
Domain: Baseball (The class defined in this file are the 2022 St. Louis Cardinal's players)
Project: 2
Task: 5



"""
from enum import Enum


class Position(Enum):
    FirstBase = 1
    ShortStop = 2
    ThirdBase = 3
    Utility = 4
    LeftField = 5
    OutField = 6
    RightField = 7
    SecondBase = 8
    DH = 9
    CenterField = 10
    Catcher = 11


import statistics


class STL_Cardinal:
    def __init__(self, name, pos, age, at_bat, runs, hits, avg):
        """Built-in method to create a new instance."""
        self.name = str(name)
        self.pos = str(pos)
        self.age = int(age)
        self.at_bat = int(at_bat)
        self.runs = int(runs)
        self.hits = int(hits)
        self.avg = float(avg)

    def __str__(self):
        """Built-in method to return a string describing this instance"""
        s0 = f"I'm {self.name} and I play {self.pos}.\n"
        s1 = f"I'm {self.age} years old.\n"
        s2 = f"I went to bat {self.at_bat} times in 2022.\n"
        s3 = f"During those at bats, I had {self.hits} hits and {self.runs} runs.\n"
        s4 = f"The percentage of times I got a hit during an at bat is {self.calc_per_hit()}%.\n"
        s5 = f"The percentage of times I got a run during an at bat is {self.calc_per_runs()}%.\n"
        s6 = f"My batting average was {self.avg}.\n"

        if self.avg > 0.200:
            s7 = "I hit OVER the Mendoza Line.\n"
        else:
            s7 = "I hit UNDER the Mendoza Line.\n"

        s = s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7
        return s

    def calc_per_hit(self):
        hits = self.hits
        at_bat = self.at_bat
        per_hits = round(hits / at_bat * 100)
        return per_hits

    def calc_per_runs(self):
        runs = self.runs
        at_bat = self.at_bat
        per_runs = round(runs / at_bat * 100)
        return per_runs

    def display_welcome(self):
        print()
        print("Welcome, I'm a 2022 St. Louis Cardinal.\n")
        # print using our built-in to string method
        print(self.__str__())


# -------------------------------------------------------------
# Calls some functions and execute code!

# if this is the main file being run

if __name__ == "__main__":
    p1 = STL_Cardinal("Paul Goldschmidt", Position.FirstBase, 34, 561, 106, 178, 0.317)
p1.display_welcome()


if __name__ == "__main__":
    p2 = STL_Cardinal("Tommy Edman", Position.ShortStop, 27, 577, 95, 153, 0.265)
p2.display_welcome()

if __name__ == "__main__":
    p3 = STL_Cardinal("Nolan Arenado", Position.ThirdBase, 31, 557, 73, 163, 0.293)
p3.display_welcome()

if __name__ == "__main__":
    p4 = STL_Cardinal("Brendan Donovan", Position.Utility, 25, 391, 64, 110, 0.281)
p4.display_welcome()

if __name__ == "__main__":
    p5 = STL_Cardinal("Tyler O'Neill", Position.LeftField, 27, 334, 56, 76, 0.228)
p5.display_welcome()

if __name__ == "__main__":
    p6 = STL_Cardinal("Dylan Carlson#", Position.OutField, 23, 432, 56, 102, 0.236)
p6.display_welcome()

if __name__ == "__main__":
    p7 = STL_Cardinal("Lars Nootbaar", Position.RightField, 24, 290, 53, 66, 0.228)
p7.display_welcome()

if __name__ == "__main__":
    p8 = STL_Cardinal("Nolan Gorman", Position.SecondBase, 22, 283, 44, 64, 0.226)
p8.display_welcome()

if __name__ == "__main__":
    p9 = STL_Cardinal("Albert Pujols", Position.DH, 42, 307, 42, 83, 0.270)
p9.display_welcome()

if __name__ == "__main__":
    p10 = STL_Cardinal("Harrison Bader", Position.CenterField, 28, 246, 35, 63, 0.256)
p10.display_welcome()

if __name__ == "__main__":
    p11 = STL_Cardinal("Andrew Knizner", Position.Catcher, 27, 260, 28, 56, 0.215)
p11.display_welcome()

if __name__ == "__main__":
    p12 = STL_Cardinal("Corey Dickerson", Position.LeftField, 33, 281, 28, 75, 0.267)
p12.display_welcome()

if __name__ == "__main__":
    p13 = STL_Cardinal("Juan Yepez", Position.OutField, 24, 253, 27, 64, 0.253)
p13.display_welcome()

if __name__ == "__main__":
    p14 = STL_Cardinal("Yadier Molina", Position.Catcher, 39, 262, 19, 56, 0.214)
p14.display_welcome()

if __name__ == "__main__":
    p15 = STL_Cardinal("Paul DeJong", Position.ShortStop, 28, 210, 19, 33, 0.157)
p15.display_welcome()

if __name__ == "__main__":
    p16 = STL_Cardinal("Edmundo Sosa", Position.ShortStop, 26, 122, 17, 23, 0.189)
p16.display_welcome()

print("=============================================================")
print()

# Is there a better/easier way to perform the follow?
Batting_avg = [
    p1.avg,
    p2.avg,
    p3.avg,
    p3.avg,
    p4.avg,
    p5.avg,
    p6.avg,
    p7.avg,
    p8.avg,
    p9.avg,
    p10.avg,
    p11.avg,
    p12.avg,
    p13.avg,
    p14.avg,
    p15.avg,
    p16.avg,
]

mean = statistics.mean(Batting_avg)
median = statistics.median(Batting_avg)
mode = statistics.mode(Batting_avg)
var = statistics.variance(Batting_avg)
stdev = statistics.stdev(Batting_avg)
lowest = min(Batting_avg)
highest = max(Batting_avg)
print(
    "Now that we've met the players, let's look at the 2022 St. Louis Cardial's Batting Averages"
)
print("=============================================================")
print(f"   mean={mean:.3f}")
print(f"   median={median:.3f}")
print(f"   mode={mode:.3f}")
print(f"   highest={highest:.3f}")
print(f"   lowest={lowest:.3f}")
print(f"   var={var:.3f}")
print(f"   stddev={stdev:.3f}")
