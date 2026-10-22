from DesmosKiller import DesmosKiller as dk

healthvals=[1045]
rounds=[10]

for carrier in range(245):
    healthvals.append(healthvals[len(healthvals)-1]*1.1)
    rounds.append(rounds[len(rounds)-1]+1)

dk.graph(xlabel="rounds", ylabel="zombie health", xlist=rounds, ylist=healthvals)
dk.show()