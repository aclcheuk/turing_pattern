from fasthtml.common import *

# Initialise the app
app, rt = fast_app(
    hdrs=(
        Link(rel="stylesheet", href="/static/style.css")
        ),
    static_path="static"
)

def LabelledSlider(label, id, val, min_val, max_val, step):
    return Div(
        Label(label, _for=id),
        Input(type="range", id=id, min = min_val, max = max_val, step = step,
        value=val, oninput=f"document.getElementById('{id}-val)').textContent = this.value"),
        Span(val, id=f"{id}-val", _class="val-display"),
        _class="control-group"
    )

# Define the main page route
@rt('/')
def get():
    return Title("Turing Pattern Simulator"), Main(
        H1("Turing Pattern Simulator"),
        Canvas(id="patternCanvas", width="200", height="200"),
        Div(
            H3("Simulation Parameters"),
            LabelledSlider("Feed Rate (f)", "feed", "0.055", "0.01", "0.1", "0.001"),
            LabelledSlider("Kill Rate (k)", "kill", "0.062", "0.01", "0.1", "0.001"),
            LabelledSlider("Diffusion U", "diffU", "1.0", "0.1", "1.0", "0.05"),
            LabelledSlider("Diffusion V", "diffV", "0.5", "0.1", "1.0", "0.05"),
            Button("Reset Simulation", id="resetBtn", cls="secondary"),
            id="controls")
    )

# Start the Server
serve()