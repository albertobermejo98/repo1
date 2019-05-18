import numpy as np

def euler(f, y0, t0, stop, h):
    # solve y' = f(t, y), y(t0) = y0
    y = y0
    t = t0
    print('t0', t, 'y0', y)
    for i in range(int((stop - t0)/h)):
        y += h*f(t, y)
        t += h
        print('t', t, 'y', y)

if __name__ == '__main__':
    # June 2014 INFO-F207
    print('June 2014 INFO-F207')
    f = lambda t, y: 3*np.exp(-4*t) - 2*y
    euler(f, 1.618, 1, 1.3, 0.1)
