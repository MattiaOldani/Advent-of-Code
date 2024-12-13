# Solution: 32026

# DATI
param nB;
set Buttons := 1 .. nB;

param nD;
set Dimensions := 1 .. nD;

param Movements {Dimensions, Buttons};

param Targets {Dimensions};

param TokenPrices {Buttons};

# VARIABILI
var Push {Buttons} >= 0, <= 100 integer;

# VINCOLI
subject to ReachTheTarget {d in Dimensions}:
    sum {b in Buttons} Movements[d,b] * Push[b] = Targets[d];

# OBIETTIVO
minimize z : sum {b in Buttons} Push[b] * TokenPrices[b];
