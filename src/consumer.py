class Consumer:
    def __init__(self, path, access_control):
        self.path = path
        self.access_control = access_control

    def __eq__(self, other):
        return self.path==other.path
    
    def __hash__(self):
        return hash(('path', self.path))
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        template = '{0.path} {0.access_control}'
        return template.format(self)