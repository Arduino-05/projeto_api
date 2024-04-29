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

Agora vou fazer um passo a passo de puxar esse repositorio para sua maquina

Inicialize o repositório Git local:

Abra o terminal ou prompt de comando.
Navegue até o diretório do seu projeto.
Execute o comando git init para inicializar o repositório Git local.

Adicione os arquivos do seu projeto:

Use o comando git add . para adicionar todos os arquivos do seu projeto ao repositório.
Ou use git add <arquivo> para adicionar arquivos específicos.

Faça o primeiro commit:

Execute o comando git commit -m "Commit inicial" para criar o primeiro commit.

Crie um repositório remoto:

Acesse o site do GitHub (ou outro serviço de hospedagem de repositórios, como GitLab ou Bitbucket).
Faça login na sua conta.
Clique em "Novo repositório" ou "Create new repository".
Preencha as informações do novo repositório, como nome, descrição e visibilidade.
Não inicialize o repositório com um arquivo README.

Vincule o repositório local ao repositório remoto:

Copie a URL do repositório remoto que você acabou de criar.
No terminal, execute o comando git remote add origin <URL_DO_REPOSITÓRIO_REMOTO>.
Substitua <URL_DO_REPOSITÓRIO_REMOTO> pela URL que você copiou.
Verifique se o remote foi adicionado corretamente com o comando git remote -v.

Envie seu projeto para o repositório remoto:

Execute o comando git push -u origin master.
O parâmetro -u define o branch remoto padrão para futuras operações de push.
Insira suas credenciais de login do GitHub (ou outro serviço) quando solicitado.
Pronto! Seu projeto local agora está sincronizado com o repositório remoto. 