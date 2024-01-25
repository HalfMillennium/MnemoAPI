import sys
sys.path.append('../')

from chiseler import parse_response

EXAMPLE_HTML = '<html>example page</html>'

class ExampleResponse:
    def __init__(self, text = None):
        self.text = text

def test_parse_response_success():
    example_response = [ExampleResponse(EXAMPLE_HTML)]
    parsed = parse_response(example_response)
    assert parsed == EXAMPLE_HTML

def test_parse_response_failure_no_entries():
    example_response = []
    parsed = parse_response(example_response)
    assert parsed == None

def test_parse_response_failure_empty_entry():
    example_response = [ExampleResponse()]
    parsed = parse_response(example_response)
    assert parsed == None