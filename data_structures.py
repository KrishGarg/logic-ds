class Literal:
    def __init__(self, atomic_prop: str, valuation: bool = None):
        self._atomic_prop = atomic_prop
        self._valuation = valuation
        
    def _negationStr(self):
        if self._atomic_prop[0] == '~':
            return self._atomic_prop[1:]
        else:
            return "~" + self._atomic_prop
        
    def getNegation(self):
        return Literal(self._negationStr())
    
    def negate(self):
        self._atomic_prop = self._negationStr
        if self._valuation != None:
            self._valuation = not self._valuation

    def getValuation(self):
        return self._valuation
    
    def setValuation(self, val):
        self._valuation = val
        
    def __eq__(self, value):
        if isinstance(value, Literal):
            return self._atomic_prop == value._atomic_prop
        if isinstance(value, str):
            return self._atomic_prop == value
        return False
