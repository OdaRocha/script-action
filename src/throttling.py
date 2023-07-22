class Throttling:
    def __init__(self, method, tps):
        self.method = method
        self.tps = tps

    def __eq__(self, other):
        return self.method==other.method
    
    def __hash__(self):
        return hash(('method', self.method))
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        template = '{0.method} {0.tps}'
        return template.format(self)