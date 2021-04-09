class Lol(object):
    _private_param = 1

    def __init__(self):
        print('init')

    def _method_private(self, x, y):
        return ( x + y ) * self._private_param

    def method_public(self):
        return Lol.static_function()

    @staticmethod
    def static_function(number = 0):
        return 1 + number


instance = Lol()

#function exists
instance.method_public()

#function not exists
instance._method_private(1, 2)

#param not exists
instance._private_param