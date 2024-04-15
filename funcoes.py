
def maiores(data):
    return len([pessoa for pessoa in data if pessoa['idade'] > 50])

def salario(data):
    salario = len([pessoa for pessoa in data if float(pessoa['salario']) > 2000])    
    porcentagem = (salario / len(data)) * 100
    return salario, porcentagem

def maxsalarios(data, n=3):
    max_salarios = sorted(data, key=lambda x: x['salario'], reverse=True)
    return max_salarios[:n]

def media_profissao(data):
    salarios_profissao = {}
    contagem_profissao = {}

    for pessoa in data:
        profissao = pessoa['profissao']
        salario = float(pessoa['salario'])

        if profissao in salarios_profissao:
            salarios_profissao[profissao] += salario
            contagem_profissao[profissao] += 1
        else:
            salarios_profissao[profissao] = salario
            contagem_profissao[profissao] = 1

    media_salarial = {profissao: salarios_profissao[profissao] / contagem_profissao[profissao] for profissao in salarios_profissao}
    return media_salarial

def sexoidade(data):
    idades = [pessoa['idade'] for pessoa in data if float(pessoa['salario']) > 2000]
    sexos = [pessoa['sexo'] for pessoa in data if float(pessoa['salario']) > 2000]

    if not sexos:  # Se a lista de sexos estiver vazia, retorna None
        return None

    # Conta quantos homens e mulheres existem na lista de sexos
    count_masculino = sexos.count('Masculino')
    count_feminino = sexos.count('Feminino')

    # Determina o sexo predominante com base nas contagens
    if count_masculino > count_feminino:
        sexo_maior_2000 = 'Masculino'
    elif count_masculino < count_feminino:
        sexo_maior_2000 = 'Feminino'
    else:
        sexo_maior_2000 = 'Masculino/Feminino'


    intervalo_idades = (min(idades), max(idades))
    return intervalo_idades, sexo_maior_2000

