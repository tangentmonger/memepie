from result import Result

class GChart():
    """Munges data for use by Google Chart API"""

    def generate_pie_data(self, result):
        return [(",".join(["[\"%s\",%d]" % pair for pair in result.get_list()]))]
