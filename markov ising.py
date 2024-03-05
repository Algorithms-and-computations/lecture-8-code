import random, math

L = 6
N = L * L
nbr = {i : ((i // L) * L + (i + 1) % L, (i + L) % N,
            (i // L) * L + (i - 1) % L, (i - L) % N) \
                                    for i in range(N)}
nsteps = 10000000
T = 1.0
beta = 1.0 / T
S = [random.choice([1, -1]) for k in range(N)]
E = -0.5 * sum(S[k] * sum(S[nn] for nn in nbr[k]) \
                                for k in range(N))
E_tot, E2_tot = 0.0, 0.0
for step in range(nsteps):
    k = random.randint(0, N - 1)
    h = sum(S[nn] for nn in nbr[k])
    Sk_old = S[k]
    delta_E = 2.0 * S[k] * h
    if random.uniform(0.0, 1.0) < math.exp(-beta * delta_E):
        S[k] *= -1
        E -= 2.0 * h * S[k]
    E_tot += E
    E2_tot += E ** 2
E_av  = E_tot / float(nsteps)
E2_av = E2_tot / float(nsteps)
c_V = beta ** 2 * (E2_av - E_av ** 2) / float(N)
print(E_av / N, c_V)
