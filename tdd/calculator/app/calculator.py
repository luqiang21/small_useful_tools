class Calculator(object):

    def add(self, x, y):
        number_types = (int, float, complex)
        print(x, y)
        if isinstance(x, number_types) and isinstance(y, number_types):
            print('X is: {}'.format(x))
            print('Y is: {}'.format(y))
            print('Result is: {}'.format(x-y))
            # import pdb; pdb.set_trace()
            return x + y
        else:
            # pass
            raise ValueError
