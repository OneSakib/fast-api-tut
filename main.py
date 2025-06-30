import json
from typing import Union
from fastapi import FastAPI, Path, Query
from fastapi.exceptions import HTTPException

app = FastAPI()


def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data


@app.get("/")
def read_root():
    return {"message": "Patient Management System Api"}


@app.get('/about')
def about():
    return {"message": "A fully functioned api to manage patient data"}


@app.get('/view')
def load_patients(sort_by: str = Query(..., description="Sort on the basic of height"), order: str = Query(default='asc', description="Order of the list of Data as asc or desc")):
    valid_sort_fields = ['height', 'weight', 'bmi']
    valid_order_fields = ['asc', 'desc']
    if sort_by not in valid_sort_fields:
        raise HTTPException(
            status_code=400, detail=f"Invalid Sort Value  {valid_sort_fields}")
    if order not in valid_order_fields:
        raise HTTPException(
            status_code=400, detail=f"Invalid Order value {valid_order_fields}")
    data = load_data()
    sort_order = order == 'desc'
    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data


@app.get('/view/{patient_id}')
def get_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient is not Found")
