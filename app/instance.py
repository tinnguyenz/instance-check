class Instance:
    TARGET_TO_REMOVE = [('inbound', '0.0.0.0/0', 22)]

    def __init__(self, id, rule):
         self.id = id
         self._rule = rule

    def get_rule(self):
        return self._rule

    def remove_loose_open_rule(self):
        for i, el in enumerate(self._rule):
            if el in self.TARGET_TO_REMOVE:
                self._rule.pop(i)
        return self._rule

    rule = property(get_rule, 'Rule property')

