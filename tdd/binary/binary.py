import collections

class Binary():
    def __init__(self, value=0):
        if isinstance(value, collections.abc.Sequence):
            if len(value) > 2 and value[:2] == '0b':
                self._value = int(value, base=2)
            elif len(value) > 2 and value[:2] == '0x':
                self._value = int(value, base=16)
            else:
                self._value = int(''.join([str(i) for i in value]), base=2)

        else:
            try:
                self._value = int(value)
                if self._value < 0:
                    raise ValueError("Binary cannot accept negative numbers, use SizedBinary instead")
            except ValueError:
                raise ValueError("Cannot convert value {} to Binary".format(value))

    def __int__(self):
        return self._value

    def __index__(self):
        # to correct return an integer
        return self.__int__()

    def __str__(self):
        return bin(self)[2:]

    def __eq__(self, other):
        return int(self) == int(other)
