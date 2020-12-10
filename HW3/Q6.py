def root(f, L, U, EPS=10 ** -10, TOL=100):
    """ Given a real valued continuous function f
        and L<U such that f(L) < 0 < f(U)
        Use the intermediate value theorem from HEDVA
        to find a root with binary search on [L,U]
        EPS: epsilon = distance of f from 0.0 to declare root
        TOL: tolerance = number of iterations allowed
    """

    for i in range(TOL):
        M = (L + U) / 2
        fM = f(M)
        print("Itertion", i, "L =", L, "M =", M, "U =", U, "f(m) =", fM)

        if abs(fM) < EPS:
            print("Found an approximated root")
            return M
        elif not L < M < U:
            print("Search interval too small")
            return None
        elif fM < 0:
            L = M  # continue search in upper half
        else:  # fM > 0
            U = M  # continue search in lower half

    print("No root found in", TOL, "iterations")
    return None


print(root(lambda x: x ** 2 - x - 1, 1.5, 2, TOL=12))
