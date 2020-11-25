"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
import random
from unittest.mock import patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_main(self):
        """Função que testa se a saída do programa corresponde ao que foi especificado."""
        # Lista de valores que serão retornados pela função input.
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        c = float(random.randint(0, 1000))
        input_returns = [a, b, c]
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            a1 = 2 * a + 0.5 * b
            a2 = 3 * a + c
            a3 = c**3
            assert mock_input.call_count == 3
            mock_print.called_with(f'valor da opção 1: {a1}')
            mock_print.called_with(f'valor da opção 2: {a2}')
            mock_print.called_with(f'valor da opção 3: {a3}')


if __name__ == '__main__':
    unittest.main()
