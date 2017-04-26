from pygol import rule_formats

import unittest

class TestRleRuleFormat(unittest.TestCase):

    def test_can_be_serialized_as_string(self):
        """ Can get the rules serialized as a string """

        rule_format = rule_formats.RleRuleFormat("B3/S23")
        self.assertEquals(rule_format.serialize(), "B3/S23")

    def test_list_birth_neighbors(self):
        """ Must have a list of number of living neighbors to cause birth """

        rule_format = rule_formats.RleRuleFormat("B3, S23")
        self.assertFalse(rule_format.valid)

        rule_format = rule_formats.RleRuleFormat("B3/S23")
        self.assertTrue(rule_format.valid)
        self.assertEquals(rule_format.birth_neighbors[0], '3')

        rule_format = rule_formats.RleRuleFormat("B137/S2459")
        self.assertTrue(rule_format.valid)
        self.assertEquals(rule_format.birth_neighbors[0], '1')
        self.assertEquals(rule_format.birth_neighbors[1], '3')
        self.assertEquals(rule_format.birth_neighbors[2], '7')

    def test_list_sustain_neighbors(self):
        """ Must have a list of number of living neighbors to prevent death """

        rule_format = rule_formats.RleRuleFormat("B3/S23")
        self.assertTrue(rule_format.valid)
        self.assertEquals(rule_format.sustain_neighbors[0], '2')
        self.assertEquals(rule_format.sustain_neighbors[1], '3')

        rule_format = rule_formats.RleRuleFormat("B137/S2459")
        self.assertTrue(rule_format.valid)
        self.assertEquals(rule_format.sustain_neighbors[0], '2')
        self.assertEquals(rule_format.sustain_neighbors[1], '4')
        self.assertEquals(rule_format.sustain_neighbors[2], '5')
        self.assertEquals(rule_format.sustain_neighbors[3], '9')
