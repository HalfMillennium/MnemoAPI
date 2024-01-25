import sys
sys.path.append('../')

from chiseler import parse_response

EXAMPLE_HTML = '<html>example page</html>'

class ExampleResponse:
    def __init__(self, text):
        self.text = text

def test_parse_response():
    example_response = [ExampleResponse(EXAMPLE_HTML)]
    parsed = parse_response(example_response)
    assert parsed == EXAMPLE_HTML