import unittest

class ILookLikeATestButShouldntRun(unittest.TestCase):

  def setUp(self):
    raise Exception("Pbbbt you ran me! Have this exception.")

  def tearDown(self):
    pass

  def test_its_a_trap(self):
    pass
