import unittest
from result import Result
from gchart import GChart

class GChartTest(unittest.TestCase):

    def test_generate_pie_data(self):
        r = Result()
        r.add("foo", None)
        r.add("bar", None)
        r.add("foo", None)
        gchart = GChart()
        self.assertEqual(gchart.generate_pie_data(r), ['["foo",2],["bar",1]'])


if __name__ == "__main__":
    unittest.main()
