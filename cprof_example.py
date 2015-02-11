import numpy as np
from numpy.linalg import eigvals

def run_experiment(niter=100):
    Y = 100
    results = []
    
    for _ in xrange(niter):
        mat = np.random.randn(Y, Y)
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results

some_results = run_experiment()
print 'Largest one we saw: %s' % np.max(some_results)
