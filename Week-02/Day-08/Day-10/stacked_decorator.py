def bold(func):
    def inner(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return inner

def italic(func):
    def inner(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return inner

@bold
@italic
def text():
    return "Python!"

print(text())  # <b><i>Python!</i></b>