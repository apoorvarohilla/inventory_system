from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import time
import logging

# Setup FastAPI
app = FastAPI()

# Logging configuration
logging.basicConfig(level=logging.INFO)

# SQLite Database Setup
def get_db():
    conn = sqlite3.connect('inventory.db')
    return conn

# Pydantic Models
class TransformData(BaseModel):
    position: list
    rotation: list
    scale: list

class Item(BaseModel):
    name: str
    quantity: int

# Delay function to simulate server delay
def simulate_delay():
    time.sleep(10)

# Endpoints

@app.post("/transform")
async def transform(data: TransformData):
    simulate_delay()
    logging.info(f"Received Transform Data: {data}")
    return {"status": "success"}

@app.post("/translation")
async def translation(position: list):
    simulate_delay()
    logging.info(f"Received Translation Data: {position}")
    return {"status": "success"}

@app.post("/rotation")
async def rotation(rotation: list):
    simulate_delay()
    logging.info(f"Received Rotation Data: {rotation}")
    return {"status": "success"}

@app.post("/scale")
async def scale(scale: list):
    simulate_delay()
    logging.info(f"Received Scale Data: {scale}")
    return {"status": "success"}

@app.get("/file-path")
async def file_path(projectpath: bool = False):
    simulate_delay()
    path = "/path/to/your/project/file" if projectpath else "/path/to/your/dcc/file"
    return {"file_path": path}

# Inventory Endpoints
@app.post("/add-item")
async def add_item(item: Item):
    simulate_delay()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (?, ?)", (item.name, item.quantity))
    conn.commit()
    conn.close()
    return {"status": "item added"}

@app.post("/remove-item")
async def remove_item(item: Item):
    simulate_delay()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventory WHERE name=?", (item.name,))
    conn.commit()
    conn.close()
    return {"status": "item removed"}

@app.post("/update-quantity")
async def update_quantity(item: Item):
    simulate_delay()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE inventory SET quantity=? WHERE name=?", (item.quantity, item.name))
    conn.commit()
    conn.close()
    return {"status": "item quantity updated"}
