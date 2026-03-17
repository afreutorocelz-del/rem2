from render_sdk import Workflows

app = Workflows()

@app.task(
  plan="performance" 
)
def add(a: int, b: int) -> int:
  return a + b
