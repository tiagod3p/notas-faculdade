from bs4 import BeautifulSoup
import requests


url_login = 'https://interage.fei.org.br/secureserver/portal/graduacao/'
url_notas = 'https://interage.fei.org.br/secureserver/portal/graduacao/secretaria/consultas/notas'
lista_ativs = []
lista_notas = []

# Iniciando sessão de scraping.
sessao = requests.Session()


def cria_login(usuario, senha):
    credenciais = {
        'Usuario': usuario,
        'Senha': senha,
    }
    return credenciais


def faz_login(usuario, senha):
    response = sessao.post(url_login, data=cria_login(usuario, senha))
    return response


def pega_notas(usuario, senha):
    response = faz_login(usuario, senha)
    response = sessao.get(url_notas)
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


def organiza_notas(soup, lista_ativs, lista_notas):
    for valor in soup.select('tbody tr'):
        ativ = valor.find('td', class_='Avaliação:')
        nota = valor.find('td', class_='Valor:')
        if ativ is None:
            continue
        if nota is None:
            print(f'A atividade [{ativ.text}] não tem nota ainda.')
            continue
        lista_notas.append(nota.text)
        lista_ativs.append(ativ.text)


def formata_notas(lista_ativs, lista_notas):
    body_msg = f'\tPlanejamento\nAtividade: [{lista_ativs[0]}] - Nota: {lista_notas[0]}\n\n\tFísica II\n'
    for indice in range(1, 6):
        body_msg += f'Atividade: [{lista_ativs[indice]}] - Nota: {lista_notas[indice]}\n'

    body_msg += '\n\tCalculo III\n'
    for indice in range(6, 9):
        body_msg += f'Atividade: [{lista_ativs[indice]}] - Nota: {lista_notas[indice]}\n'

    body_msg += '\n\tQuimica\n'
    for indice in range(9, 13):
        body_msg += f'Atividade: [{lista_ativs[indice]}] - Nota: {lista_notas[indice]}\n'
    return body_msg
