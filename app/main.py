from fastapi import FastAPI, Request as REQUEST
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [ "*" ]  # Allow all origins for development; restrict in production

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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