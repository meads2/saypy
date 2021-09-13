def say_hi(name:str=None) -> str:
    """" Say Hi

    Args:
    name (str) - Name to greet user with
    """
    msg = f"Hey, {name}! Whats Up?"
    print(msg)
    return msg

def say_bye(goodbye:str=None) -> str:
    """ Goodbye Function
    
    Args:
    goodbye (str) - Goodbye message added to output
    """
    msg = f'Goodbye! see you soon. P.S. {goodbye}'
    print(msg)
    return msg
    