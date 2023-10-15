from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
import pymysql
import geopy.distance
from random import randint

def req():
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='dima',
            password='bebrik123',
            database='test',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)
        try:
            # create table
            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM `offices`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                return rows
        finally:
            connection.close()
    
    except Exception as ex:
        print("Connection refused...")
        print(ex)

app = FastAPI()

time = 1000

@app.get("/windows/{id}")
async def user(id: str):
    global time
    time += 1000
    if time > 10000:
        time = 1000
    return [{"name": "Окно 1", "operation": "Операция депозит", "time": time},
	{"name": "Окно 2", "operation": "Операция кредит", "time": 5000},
	{"name": "Окно 3", "operation": "Операция оформление", "time": 7000},
	{"name": "Окно 3", "operation": "Операция оформление", "time": 7000}]

@app.get("/offices/{latitude}/{longitude}")
async def getoffices(latitude: str, longitude: str):
    rows = req()
    for office in rows:
        coords_1 = (latitude, longitude)
        coords_2 = (office['latitude'], office['longitude'])
        office['distance'] = geopy.distance.geodesic(coords_1, coords_2).km
        office['time'] = randint(10, 60)

    maxdist = max(rows, key=lambda x:x['distance'])['distance']
    mindist = min(rows, key=lambda x:x['distance'])['distance']
    
    for office in rows:
       office['score'] = ((maxdist - office['distance']) / maxdist) * 60 + (60 - office['time']) 
    
    best = sorted(rows, key=lambda d: d['score'], reverse=True)
	
    return best[:5]


app.add_middleware(CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")