"""Calculation Class"""
class Calculation:
    """ calculation base class"""
    def __init__(self,v: tuple):
        """constructor"""
        self.v = Calculation.args_to_list_float(v)
    @classmethod
    def create(cls, v: tuple):
        """ factory method"""
        return cls(v)
    @staticmethod
    def args_to_list_float(v):
        """ standardize values to list of floats"""
        list_values_float = []
        for i in v:
            list_values_float.append(float(i))
        return tuple(list_values_float)
