# -------------------
# TestXML.py
# Lab 2
# Mateusz Dubaniowski
# Vincent Steil
# -------------------

# imports

import StringIO
import unittest

from XML import XML_parseline
from XML import XML_find_occurrences

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO('<one>\n')
        a = [1]
        aa = []
        b = XML_parseline(r, aa, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  2)
        self.assert_(aa ==  [['one', 1]])

    def test_read1 (self) :
        r = StringIO.StringIO("<one><two>\n")
        a = [1]
        aa = []
        b = XML_parseline(r, aa, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  3)
        self.assert_(aa ==  [["one", 1], ["two", 2]])
        
    def test_read2 (self) :
        r = StringIO.StringIO("<one><bum></bum>\n")
        a = [1]
        aa = []
        b = XML_parseline(r, aa, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  2)
        self.assert_(aa ==  [["one", 1], ["bum", 2]])

    def test_read3 (self) :
        r = StringIO.StringIO("</one></woops>\n")
        a = [1]
        aa = []
        b = XML_parseline(r, aa, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  -1)
        self.assert_(aa ==  [])


    # ----
    # XML_find_occurences
    # ----

    def test_eval_1 (self) :
        v = XML_find_occurrences([['one', 1], ['two', 2], ['three', 3], ['a', 2]], [['two', 1]])
        self.assert_(v == [2])

    def test_eval_2 (self) :
        v = XML_find_occurrences([['THU', 1], ['Team', 2], ['ACRush', 3], ['Jelly', 3], ['Cooly', 3], ['JiaJia', 2], ['Team', 3], ['Ahyangyi', 4], ['Dragon', 4], ['Cooly', 4], ['Amber', 5]], [['Team', 1], ['Cooly', 2]])
        self.assert_(v == [2, 7])

    def test_eval_3 (self) :
        v = XML_find_occurrences([['one', 1], ['two', 2], ['three', 3], ['a', 4], ['a', 2]], [['a', 1]])
        self.assert_(v == [4, 5])

    def test_eval_4 (self) :
        v = XML_find_occurrences([['one', 1], ['two', 2], ['three', 3], ['a', 4], ['y', 5], ['z', 5], ['x', 6], ['a', 2], ['y', 3], ['z', 3]], [['a', 1], ['y', 2], ['z', 2]])
        self.assert_(v == [4, 8])

    def test_eval_5 (self) :
        v = XML_find_occurrences([['a', 1], ['y', 2], ['z', 2], ['x', 3], ['y', 4], ['y', 3]], [['y', 1]])
        self.assert_(v == [2, 5, 6])

    def test_eval_6 (self) :
        v = XML_find_occurrences([['one', 1], ['two', 2], ['three', 3], ['a', 3]], [['one', 1], ['two', 2], ['three', 3], ['a', 3]])
        self.assert_(v == [1])

    def test_eval_7 (self) :
        v = XML_find_occurrences([['one', 1], ['b', 2], ['c', 3]], [['one', 1], ['c', 2]])
        self.assert_(v == [])

# ----
# main
# ----

print "TestXML.py"
unittest.main()
print "Done."
