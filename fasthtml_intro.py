from fasthtml.common import *

app,rt = fast_app(live=True) # live=True auto reloads page when updating code

@rt('/') # define home route
def get(): 
    return Titled("Greeting", 
    Div(P('Hello World')),
    P(A("Link", href="/change"))
    )

@rt('/change')
def get():
    return(Titled("New Page"),
    Div(P("This is the second page")),
    P(A("Home", href="/"))
    )
    

serve()
