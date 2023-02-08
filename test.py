def linear_search_recursive(lst, target):
    """
    Zoek een element in de gegeven lijst door middel van recursief lineair zoeken.
    Zorg dat de inhoud van de gegeven lijst niet verandert.
    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.
    Returns:
        bool: Of het element in de lijst voorkomt.
    """
    for i in lst:
        if i == target:
            return True
    return False