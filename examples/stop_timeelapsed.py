import scipy
import time, random

from climin import GradientDescent
from climin.stops import stop_time_elapsed

quadratic = lambda x: (x**2).sum()
quadraticprime = lambda x: 2 * x

if __name__ == '__main__':
    dim = 10
    wrt = scipy.random.standard_normal((dim,)) * 10 + 5
    
    opt = GradientDescent(wrt, quadraticprime, steprate=0.01)
    stop = stop_time_elapsed(5)
        
    for info in opt:
        # pretend that optimizing step takes some time
        time.sleep(0.01)
        print "iteration %3i loss=%g" % (info['n_iter'], info['loss'])
    
        if stop(info):
            break
            
    assert (abs(wrt) < 0.01).all(), 'did not find solution'
