# Instruções

Leia atentamente esse texto para fazer o exercício corretamente.

## Regras

Aqui vão algumas regras para resolver os exercícios, as regras estão em órdem decrescente de prioridade:

1. Você não poderá alterar o arquivo `test_main.py` sob pena de ter sua nota zerada.
2. O programa deve ter como arquivo principal o `main.py`, a alteração do nome desse arquivo pode inviabilizar os testes afetando negativamente a sua nota.
3. Você deve procurar nos comentários do programa dicas de aonde deve colocar ou completar o código para que ele seja executado corretamente.
4. Você pode criar e modificar arquivos.
5. Quando receber um *feedback* pelo *GitHub* **não** clique no botão **merge**, pois ali será o espaço que utilizarei para explicar como melhorar o seu código.

## Avaliação

O script será avaliado pelos seguintes fatores em órdem decrescente de importância:

1. O script deve rodar sem erros.
2. O script deve passar nos testes automáticos.
3. O script deve passar nos testes feitos manualmente.
4. O script deve ser capaz de resolver o problema como especificado.
5. O script deve seguir as convenções de código segundo a [PEP8](https://www.python.org/dev/peps/pep-0008) em [português](https://www.vivaolinux.com.br/artigo/PEP-8-Guia-de-estilo-para-codigo-Python).
6. O script deve utilizar as estruturas *corretas* para resolver o problema.
7. O script deve ter comentários explicando as técnicas utilizadas quando elas não forem de conhecimento geral.

## Como realizar os testes automáticos antes de enviar

Se quiser realizar os testes automáticos antes de enviar o arquivo, basta escrever o seguinte comando no terminal:
`python -m unittest test_main.py`  
Durante o teste todas as saídas são capturadas, ou seja, só aparecerá no console o que o usuário digitar.
Assim, não serão exibidas as mensagens para o usuário resultantes de prints ou inputs.
Fora isso o programa executa normalmente.
