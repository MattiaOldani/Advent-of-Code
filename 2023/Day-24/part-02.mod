# Solution: 1025127405449117

# DATI
param NumeroCoordinate;
set Coordinate := 1 .. NumeroCoordinate;
param NumeroPunti;
set Punti := 1 .. NumeroPunti;
param CoordinatePunti {Punti, Coordinate};
param VelocitaPunti {Punti, Coordinate};

# VARIABILI
var CoordinateRoccia {Coordinate} >= 1;
var VelocitaRoccia {Coordinate} >= -500, <= 500;
var Tempo {Punti} >= 0;
var Somma;

# VINCOLI   
subject to DefinizioneSomma:
    Somma = sum {c in Coordinate} CoordinateRoccia[c];
subject to Intersezione {p in Punti, c in Coordinate}:
    CoordinatePunti[p,c] + VelocitaPunti[p,c]*Tempo[p] = CoordinateRoccia[c] + VelocitaRoccia[c]*Tempo[p];

# DATI

data;

param NumeroCoordinate := 3;
param NumeroPunti := 3;
param CoordinatePunti: 1 2 3 :=
1 260346828765750 357833641339849 229809969824403
2 340220726383465 393110064924024 226146987100003
3 11361697274707 101596061919750 46099495948720;
param VelocitaPunti: 1 2 3 :=
1 64 -114 106
2 -79 -61 158
3 328 162 333;

end;
