from correct_spelling import app as spelling_app
from correct_grammar import app as grammar_app

# Choose which app to run based on the request
def application(environ, start_response):
    path = environ["PATH_INFO"]
    if path == "/api/correct_spelling":
        app = spelling_app
    elif path == "/api/correct_grammar":
        app = grammar_app
    else:
        # Handle 404
        def not_found(start_response):
            start_response("404 Not Found", [("Content-Type", "text/plain")])
            return [b"404 Not Found"]

        return not_found(start_response)

    return app(environ, start_response)
