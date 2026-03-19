# Stores edge between two vertices
# edge represents "relationship" ie: DIRECTED, ACTOR, ROLE
class EdgeData:
    def __init__(self, label, data):
        self.label = label
        self.data = data