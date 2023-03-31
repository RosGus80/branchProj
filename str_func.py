def func(str):
    """My docstring"""
    return str.upper()

def func1(str):
    """Docstring"""
    dic = str.split(" ")
    dic1 = []
    for word in dic:
        dic1.append(word.title())
    return " ".join(dic1)