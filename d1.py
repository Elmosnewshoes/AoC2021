from pzzl import pzzl

inp = pzzl(1,)
pzzl1 = inp.inp

def calc_energy(x):
    energies = [0,]
    for en in x:
        if en == '':
            energies.append(0)
            continue

        energies[-1] += int(en)
    return energies

energies = calc_energy(pzzl1)
energies.sort()
print(energies[-1])
print(sum(energies[-3:]))
