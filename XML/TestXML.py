#-------------------
#TestXML.py
#Lab 2
#Mateusz Dubaniowski
#Vincent Steil
#-------------------

# imports

import StringIO
import unittest

from XML import XML_parseline

# -----------
# TestXML
# -----------

class TestXML (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("<one>")
        a = [0]
        b = XML_parseline(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)

    def test_read1 (self) :
        r = StringIO.StringIO("<one><two>")
        a = [0]
        b = XML_parseline(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  2)
        
    def test_read2 (self) :
        r = StringIO.StringIO("<one><bum></bum>")
        a = [0]
        b = XML_parseline(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)

    def test_read3 (self) :
        r = StringIO.StringIO("</one></woops>")
        a = [0]
        b = XML_parseline(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  -2)


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_eval_5 (self) :
        v = collatz_eval(1, 999999)
        self.assert_(v == 525)

    def test_eval_6 (self) :
        v = collatz_eval(1, 1)
        self.assert_(v == 1)

    def test_eval_7 (self) :
        v = collatz_eval(500, 5000)
        self.assert_(v == 238)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assert_(w.getvalue() == "1 1 1\n")

    def test_print2 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1993, 1993, 51)
        self.assert_(w.getvalue() == "1993 1993 51\n")

    def test_print3 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assert_(w.getvalue() == "1 999999 525\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve1 (self) :
        r = StringIO.StringIO("1 1\n5 5\n19999 19999\n9005 10000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n5 5 6\n19999 19999 67\n9005 10000 260\n")

    def test_solve2 (self) :
        r = StringIO.StringIO("1 10000\n10000 200000\n900000 999999\n1 999999\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10000 262\n10000 200000 383\n900000 999999 507\n1 999999 525\n")

    def test_solve3 (self) :
        r = StringIO.StringIO("1 5\n894 895\n201 347\n905 90000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 5 8\n894 895 99\n201 347 144\n905 90000 351\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
