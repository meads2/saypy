def say_hi(name:str=None) -> str:
    """" Say Hi

    Args:
    name (str) - Name to greet user with
    """
    msg = f"Hey, {name}! Whats Up?"
    print(msg)
    return msg
