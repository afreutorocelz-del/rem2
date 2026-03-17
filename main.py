from render_sdk import Workflows
from math_tasks import app as math_app
from text_tasks import app as text_app

app = Workflows.from_workflows(math_app, text_app)

if __name__ == "__main__":
  app.start()
