import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-25672-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "917721s009":
        {
            "name": "Harinni",
            "major": "datascience",
            "starting_year": 2021,
            "total_attendance": 10,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-10-13 00:54:34"
        },
    "917721s041":
        {
            "name": "Emily blunt",
            "major": "blockchain",
            "starting_year": 2022,
            "total_attendance": 6,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2023-10-10 12:54:34"
        },
    "917721s016":
        {
            "name": "Elon musk",
            "major": "robotics",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-13 02:54:34"
        },
    "917721s017":
        {
            "name": "keerthana",
            "major": "data science",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-13 02:54:34"
        },
    "917721s025":
        {
            "name": "Rekha",
            "major": "robotics",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-13 02:54:34"
        },
    "917721s039":
        {
            "name": "Vinotha",
            "major": "blockchain",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-13 02:54:34"
        },
    "917721s032":
        {
            "name": "Sowmya",
            "major": "machine learning",
            "starting_year": 2021,
            "total_attendance": 15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-13 02:54:34"
        }


}

for key,value in data.items():
    ref.child(key).set(value)