import os
import psycopg

DATABASE_URL = os.getenv("DATABASE_URL")

def get_conn():
    return psycopg.connect(
        DATABASE_URL,
        autocommit=True,
        row_factory=psycopg.rows.dict_row
    )

def create_schema():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS hotel_rooms (
                id SERIAL PRIMARY KEY,
                room_number INT NOT NULL,
                type VARCHAR(100) NOT NULL,
                price NUMERIC(10,2) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS hotel_guests (
                id SERIAL PRIMARY KEY,
                firstname VARCHAR(100) NOT NULL,
                lastname VARCHAR(100) NOT NULL,
                address VARCHAR(255)
            );

            CREATE TABLE IF NOT EXISTS hotel_bookings (
                id SERIAL PRIMARY KEY,
                guest_id INT NOT NULL,
                room_id INT NOT NULL,
                datefrom DATE NOT NULL,
                dateto DATE NOT NULL,
                addinfo VARCHAR(255),
                CONSTRAINT fk_guest
                    FOREIGN KEY (guest_id) REFERENCES hotel_guests(id),
                CONSTRAINT fk_room
                    FOREIGN KEY (room_id) REFERENCES hotel_rooms(id)
            );
        """)

        def insert_example_data():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            INSERT INTO hotel_rooms (room_number, type, price)
            VALUES
                (101, 'Single Room', 80.00),
                (202, 'Double Room', 120.00),
                (404, 'Suite', 500.00);
        """)

        cur.execute("""
            INSERT INTO hotel_guests (firstname, lastname, address)
            VALUES
                ('Ali', 'Khan', 'Helsinki, Finland'),
                ('Sara', 'Ahmed', 'Oulu, Finland');
        """)

        cur.execute("""
            INSERT INTO hotel_bookings (guest_id, room_id, datefrom, dateto, addinfo)
            VALUES
                (1, 1, '2026-05-01', '2026-05-05', 'Needs early check-in'),
                (2, 2, '2026-06-10', '2026-06-15', 'Late arrival');
        """)