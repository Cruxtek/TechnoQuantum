import scqubits as scq
import jupyter
import ipyvuetify as create


transmon = scq.Transmon(
    EJ=30.0,
    EC=1.2,
    ng=0.3,
    ncut=31
)

tmon = scq.Transmon.create()
