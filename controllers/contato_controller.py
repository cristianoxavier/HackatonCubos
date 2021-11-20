from flask_mail import Message
from configurations.enviroment import EMAIL


def envia_email(*args):
    infos = args[0]
    msg = Message('Uma empresa se interessou!', sender=EMAIL, recipients=[EMAIL])
    msg.body = f"""
    Olá Equipe!
    
    Uma empresa se interessou, por favor entre em contato para mais detalhes!
    Nome da empresa: {infos['inputName']}
    E-mail para contato: {infos['inputEmail']}
    Telefone: {infos['inputPhone']}
    Mensagem: {infos['inputText']}
    """
    return msg
