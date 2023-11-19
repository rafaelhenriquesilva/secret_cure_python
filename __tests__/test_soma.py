import sys
import os

# Obtendo o caminho absoluto do diretório atual (__tests__) e adicionando o diretório pai (SecretCure) ao PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.soma import soma

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(-5, -7) == -12