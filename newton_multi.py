beta0=10
beta1=5
y=beta0+beta1*x+np.random.normal(size=n)

def test_fun(theta):
    return np.sum(y-theta[0]-theta[1]*x)**2

optimize_mv(np.array([0.5,0]), test_fun)

import numdifftools as nd

def optimize_mv(x0, f, tol=1e-4):
    grad = nd.Gradient(f)
    hessian = nd.Hessian(f)
    x = x0
    x_new =  x0 - scipy.linalg.solve(hessian(x0), grad(x0))
    while pow(np.sum((x_new-x)**2), 0.5)>tol:
        x = x_new
        x_new = x-scipy.linaly.solve(hessian(x), grad(x))
    return {"x": x_new, "value": f(x_new)}

optimize_mv(np.array([2,0]), test_fun)