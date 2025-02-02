def ends_with_s(word):
    if len(word) < 1:
        return False
    return word[-1] == "s" or word[-1] == 'S'
