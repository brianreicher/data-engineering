from drv import DRV


def main():
    # simulation item distributions
    burgers: DRV = DRV(type="normal", mean=600, std=200, bin=20)
    fries: DRV = DRV(type="normal", mean=500, std=50, bin=20)
    cokes: DRV = DRV(type="normal", mean=2000, std=100, bin=20)

    # profit distribution
    profit: DRV = 0.25*burgers + 0.5*fries + 1*cokes

    # expenses distribution (constant)
    expenses: DRV = DRV({2500:1.0})

    # profit nets
    net: DRV = profit - expenses
    annual_net: DRV = 0.365 * net

    annual_net.plot(title='Annual Net ($000')


if __name__ == '__main__':
    main()