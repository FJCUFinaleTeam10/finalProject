from RMDP import RMDP


def main():
    delay = float('Inf')
    Theta: list = []
    P_hat: list = []
    for i in range(0, 480):
        Theta, P_hat = RMDP(i, Theta, delay, P_hat)

main()
