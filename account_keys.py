def account(filename):
    with open(filename) as file:
        return file.read()


saxo = account('saxo.key')
quandl = account('quandl.key')
tradier = account('tradier.key')
