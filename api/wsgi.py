from correct_spelling import app as spelling_app
from correct_grammar import app as grammar_app

# This is the main WSGI entry point
# You can choose which app to run based on a condition or deploy separately
app = spelling_app  # or grammar_app, depending on the endpoint

# To dynamically switch based on request, you might need a more complex routing logic
