import re

class RleRuleFormat(object):

    formatted = re.compile("B([0-9]+)/S([0-9]+)")

    def __init__(self, rule_string, valid=False, birth_neighbors=None, sustain_neighbors=None):
        self.rule_string = rule_string
        self.valid = valid
        self.birth_neighbors = birth_neighbors if birth_neighbors is not None else []
        self.sustain_neighbors = sustain_neighbors if sustain_neighbors is not None else []

        rule_values = self.formatted.findall(rule_string)
        if len(rule_values) > 0:
            rule_value = rule_values[0]
            self.birth_neighbors = rule_value[0]
            self.sustain_neighbors = rule_value[1]
            self.valid = True

    def serialize(self):
        return self.rule_string
