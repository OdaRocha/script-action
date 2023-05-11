class AccessControl:
    def __init__(self, api_key, name, throttling):
        self.api_key = api_key
        self.name = name
        self.throttling = throttling

    def __eq__(self, other):
        return self.api_key==other.api_key
    
    def __hash__(self):
        return hash(('api_key', self.api_key))
    
    def __repr__(self):
        return str(self)

    def __str__(self):
        template = '{0.api_key} {0.name} {0.throttling}'
        return template.format(self)