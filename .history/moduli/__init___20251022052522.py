"""
🧠 Moduli Mente Artificiale
============================
Package contenente tutti i moduli cerebrali simulati
"""

__version__ = "1.0.0"
__author__ = "Guerra Games"

# Import automatico dei moduli principali
from . import visione
from . import udito
from . import motoria
from . import prefrontale
from . import memoria
from . import emozione
from . import talamo
from . import tronco

__all__ = [
    'visione',
    'udito',
    'motoria',
    'prefrontale',
    'memoria',
    'emozione',
    'talamo',
    'tronco'
]

