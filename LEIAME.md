Esta API Flask foi desenvolvida para operar em dados provenientes de um banco de dados. Ela oferece uma variedade de funcionalidades, como retornar números aleatórios, processar informações sobre idade, salário, profissões e sexo das pessoas no banco de dados.

A API consiste em três arquivos:

### app.py
- **Descrição:** Contém as rotas da API Flask.
- **Rotas:**
  1. **/**: Retorna uma mensagem indicando o status da API.
  2. **/aleatorios**: Retorna um número aleatório entre 49 e 100.
  3. **/argumentos/<string:nome>**: Retorna o nome fornecido como parâmetro.
  4. **/argumentos**: Retorna o valor do parâmetro "nome" passado na query da URL.
  5. **/idades**: Retorna o número de pessoas com idade superior a 50 anos.
  6. **/salario**: Retorna a quantidade e a porcentagem de pessoas com salário acima de 2000.
  7. **/maior_salario**: Retorna os N maiores salários.
  8. **/profissoes**: Retorna a média de salários por profissão.
  9. **/idade/<string:tipo>**: Retorna contagem de pessoas por sexo ou intervalo de idade.

### funcoes.py
- **Descrição:** Contém funções utilizadas pelas rotas para processar os dados.
- **Funções:**
  1. **maiores(data)**: Retorna a quantidade de pessoas com idade superior a 50 anos.
  2. **salario(data)**: Retorna a quantidade e porcentagem de pessoas com salário acima de 2000.
  3. **maxsalarios(data, n=3)**: Retorna os N maiores salários.
  4. **media_profissao(data)**: Retorna a média de salários por profissão.
  5. **sexoidade(data)**: Retorna contagem de pessoas por sexo, intervalo de idade e sexo com mais pessoas acima de 2000 de salário.

### randan_data.py
- **Descrição:** Representa o banco de dados utilizado pela API.
