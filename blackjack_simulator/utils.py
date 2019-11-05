from difflib import get_close_matches


def raise_close_match_error(eval, available_list, var_name):
    """Raise error if variable defined is not in available arguments.

    Parameters
    ----------
    eval : str
        Variable to evaluate
    available_list : list of str
        List of accepted arguments.
    var_name : str
        Name of variable being evaluated.

    Returns
    -------
    str
        Returns evaluating value.

    Raises
    -------
    ValueError
        Raises value error if eval is not on available_list.

    """
    if eval not in available_list:
        try:
            close = get_close_matches(eval, available_list, n=1)[0]
            error = "'{}' is not an available {}. Did you mean '{}'?"
            error = error.format(eval, var_name, close)
        except IndexError:
            error = f"'{eval}' is not an available {var_name}."
        raise ValueError(error)
    return eval
