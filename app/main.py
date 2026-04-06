from fastapi import FastAPI, Request as REQUEST
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Hello docker dev mode"}


# what is my ip address?
@app.get("/api/ip")
def api_ip(request : REQUEST):
    return { "ip": request.client.host }

@app.get("/ip", response_class=HTMLResponse)
def ip(request : REQUEST):
    return f"""
    <html>
        <head>
            <title>My IP Address</title>
        </head>
        <body>
            <h1>Your IP Address is: {request.client.host}</h1>
        </body>
    </html>
    """