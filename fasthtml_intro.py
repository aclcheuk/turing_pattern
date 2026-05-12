from fasthtml.common import *

app,rt = fast_app(live=True) # live=True auto reloads page when updating code

@rt('/') # define home route
def get(): 
    return Titled("Greeting", 
    Div(P('Hello World')),
    P(A("Link", href="/change")) # makes a hyperlink to page "/change"
    # We need to add a new route: @rt('/change') below
    )

def NumList(i):
    return Ul(*[Li(o) for o in range(i)])

@rt('/change')
def get():
    nums = NumList(15) # Make a list of numbers
    return(Titled("New Page"),
    nums,
    Div(P("This is the second page updated. We linked to this new page with <a> href")),
    P(A("Home", href="/")), # back to Home with href
    P(A("In-Place (hx_get)", hx_get ='/new_change')) # uses HTMX to update page
    )

@rt('/new_change')
def get():
    return(P("Newly Changed text"))

serve()
