
def cipher(text, shift, encrypt=True):
    
    """
    This function can replace each letter in a sentence or word by another letter that is at some fixed number of positions down or up of the alphabet.
    
    Parameters
    ----------
    text : str
        A text string.
    shift : int
        Unit of alphabet to shift along the alphabet string (-/+ for left and right).
    encrypt : bool
        Default is True, whether the text is to be encrypted or decrypted.
        
    Returns
    -------
    str
        The encrypted or decrypted string.
        
    Examples
    --------
    >>> cipher("abc", 1)
    'bcd'
    """    
    
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text



