from render_sdk import Workflows

app = Workflows()

@app.task
def capitalize(s: str) -> str:
  return s.upper()
