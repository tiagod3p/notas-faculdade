from scraping import pega_notas, organiza_notas, formata_notas
from scraping import lista_ativs, lista_notas
from enviar_email import envia_email
from time import sleep

soup = pega_notas('USUARIO_DA_UNIVERSIDADE', 'SENHA')
organiza_notas(soup, lista_ativs, lista_notas)
texto = formata_notas(lista_ativs, lista_notas)

lista_comparativa = ['', '', '10', '', '',
                     '', '1,25', '', '', '1,15', '10', '', '']


def permissao_pra_enviar():
    """
    Verifica se a lista de notas foi alterada para permitir
    enviar um e-mail.

    Returns:
        True -- Lista de notas foi alterada, ou seja != da lista comparativa
        False -- Lista de notas não foi alterada.
    """
    if len(lista_comparativa) == len(lista_notas):
        if lista_comparativa != lista_notas:
            return True
        else:
            return False
    return False


while True:
    """
    Loop infinito garante que sempre se esteja verificando
    por alterações de nota no sistema.
    Aguarda sempre 2 horas para rodar o loop e procurar
    por novas notas, pois o site da universidade atualiza o
    Portal com as notas a cada 2 horas nos horários impares.
    """
    if permissao_pra_enviar():
        envia_email(texto, 'SEU_EMAIL', 'SUA_SENHA')
        lista_comparativa = lista_notas
        continue
    else:
        sleep(7200)
        print('tentando de novo...')
        continue
