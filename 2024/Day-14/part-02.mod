# Solution: 7774

# DATI

# VARIABILI
var X >= 0 integer;
var Y >= 0 integer;
var step >= 0 integer;

# VINCOLI
subject to Equals:
    101 * X + 98 = 103 * Y + 49;

subject to StepValue:
    step = 101 * X + 98;

# OBIETTIVO
