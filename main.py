from RMDP import RMDP


def main():
    Theta: list = []
    P_hat: list = []
    delay = float('inf')
    for i in range(0, 480):
        Theta, P_hat = RMDP(i, Theta, P_hat, delay)


main()
