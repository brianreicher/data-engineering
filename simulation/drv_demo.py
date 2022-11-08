"""
File: drv_demo.py

Description: demo of DRV class
"""

from drv import DRV


def main() -> None:
    # coin flip simulation
    C: DRV = DRV({'H': 0.5, 'T': 0.5})
    flips = [C.random() for _ in range(10)]
    print(flips)

    # drv simulation
    X: DRV = DRV({1: 0.6, 3: 0.4})
    Y: DRV = DRV({0: 0.2, 2: 0.5, 5: 0.3})

    Z: DRV = X + Y
    Z.plot()

    # dice simulation
    D: DRV = DRV(type='uniform', min=1, max=6, bin=6)
    D.plot(show_cumulative=False)

    two_die: DRV = D + D
    two_die.plot(bins=11, show_cumulative=False)

    # normal distribution
    N: DRV = DRV(type='normal', mean=5, std=3, bins=100)
    N.plot(trials=1000)

if __name__ == "__main__":
    main()