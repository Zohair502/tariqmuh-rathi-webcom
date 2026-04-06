from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.db import get_conn, create_schema, insert_example_data

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_schema()
insert_example_data()

rooms = [
    {"room_number": 101, "room_type": "single room", "price": 80},
    {"room_number": 202, "room_type": "double room", "price": 120},
    {"room_number": 404, "room_type": "suite", "price": 500}
]

@app.get("/")
def read_root(): 
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT version() ")
        result = cur.fetchone()

    return { "msg": f"Hotel API!", "db_status": result }

@app.get("/api/ip")
def api_ip(request: Request):
    return {"ip": request.client.host}

@app.get("/ip", response_class=HTMLResponse)
def ip(request: Request):
    return f"""
    <html>
        <head><title>My IP Address</title></head>
        <body>
            <h1>Your IP Address is: {request.client.host}</h1>
        </body>
    </html>
    """

@app.get("/rooms")
def get_rooms():
    return rooms

@app.post("/bookings")
async def create_booking(request: Request):
    body = await request.json()
    return {
        "msg": "Booking created!",
        "booking": body
    }