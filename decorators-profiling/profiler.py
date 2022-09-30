"""
File: profiler.py

Description: a Python3 code profiler using decorators
"""

import time
from collections import defaultdict


class Profiler:
    calls = defaultdict(int)  # function name -> int
    time = defaultdict(float)  # elapsed time -> float

    def __init__(self):
        pass

    @staticmethod
    def _add(func_name, sec):
        Profiler.calls[func_name] += 1
        Profiler.time[func_name] += sec

    @staticmethod
    def profile(func):
        """
            Code profiler decorator
        :param func:
            Given function to profile
        :return:
        """
        def wrapper(*args, **kwargs):
            # grab function name, splitting dict on spaces
            func_name = str(func).split()[1]

            start = time.time_ns()
            val = func(*args, **kwargs)
            finish = time.time_ns()

            elapsed_time = (finish-start)/10 **9
            Profiler._add(func_name, elapsed_time)
            return val
        return wrapper

    @staticmethod
    def report():
        """
            Summarize # calls, total runtime, and time/call for each function
        """
        print("Function              Calls     TotSec   Sec/Call")
        for name, num in Profiler.calls.items():
            sec = Profiler.time[name]
            print(f'{name:20s} {num:6d} {sec:10.6f} {sec / num:10.6f}')


def profile(f) -> None:
    """
        Helper function to profile a given function
    :param f:
         Function to profile
    :return:
        None
    """
    Profiler.profile(f)

