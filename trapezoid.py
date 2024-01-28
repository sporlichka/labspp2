'''
Using the Trapezoidal Rule
a. Estimate the integral with n = 4 steps and find an upper bound for |Et|.
b. Evaluate the integral directly and find |Et| .
c. Use the formula (|Et| >(true value)) * 100 to express |Et| as a percentage of the integrals true value.
'''

import numpy as np
from scipy.integrate import quad
import sympy as sp

def main():
    n = 4
    a, b = map( float, input("Enter a and b: ").split())
    func_str = input("input f(x)= ")
    print("n, a, b = ", float(n), float(a), float(b))
    
    x = sp.symbols('x')
    f = sp.sympify(func_str)
    print("f(x) =", f)
    
    stepsize = (b - a) / n
    print("Step size = ", float(stepsize))

    stepvalues = [a + i * stepsize for i in range(n + 1)]
    funcvalues = [f.subs(x, step) for step in stepvalues]
    # A
    T = (stepsize/2)*(funcvalues[0] + 2*sum(funcvalues[1:-1]) + funcvalues[-1])
    print("T = ", float(T))    

    fprime = sp.diff(f, x)
    fdoubleprime = sp.diff(fprime, x)
    print(fdoubleprime)

    if fdoubleprime.is_constant():
        M = fdoubleprime.evalf()
    else:
        M = abs(fdoubleprime.evalf(subs={x: a}) if f.subs(x, a) > f.subs(x, b) else fdoubleprime.evalf(subs={x: b}))

    print("M = ", float(M))
    
    Et = (M * pow((b - a), 3))/(12 * pow(n, 2))
    print("Et = ", float(Et))
    # B
    f_lambda = sp.lambdify(x, f, modules=['numpy'])
    true_value, _ = quad(f_lambda, a, b) 
    print("True value = ", float(true_value))
    
    # C
    C = (abs(true_value-T) / (true_value)) * 100
    print("C = ", int(C) + "%")

if __name__ == "__main__":
    main()