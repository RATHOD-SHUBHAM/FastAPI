from fastapi import FastAPI, HTTPException, Query
from db import Person
import json
from typing import Annotated, Optional
import random

app = FastAPI(
    title="RestAPI Tutorials",
    description="""Building my first Pyhon APIS""",
    version="2023.1.31",
)

# todo: Invoke DB
with open('people.json', 'r') as f:
    people = json.load(f)['people']

print(people)


### todo: Get

@app.get("/")
async def root():
    return {"message": "Building my first Pyhon API's"}


# get person name based on id
@app.get("/person/{person_id}")
async def get_person(person_id: int):
    for p in people:
        if p['id'] == person_id:
            return {"person name": p['first_name']}
    raise HTTPException(
        status_code=404,
        detail="Person not found"
    )


# get person details based on id
@app.get("/persondetail/{person_id}")
async def get_person(person_id: int):
    for p in people:
        if p['id'] == person_id:
            return {"person": p}
    raise HTTPException(
        status_code=404,
        detail="Person not found"
    )


# todo: Query Parameter
@app.get("/search_person")
async def read_items(
        gender: Annotated[str | None, Query(title="Gender", description="The Gender used to filter")] = None,
        first_name: Annotated[
            str | None, Query(title="First Name", description="The First name used to filter")] = None):
    if first_name is None and gender is None:
        return people

    elif gender is None:
        for p in people:
            if first_name.lower() == p['first_name'].lower():
                return {"Person": p}

    elif first_name is None:
        gender_people = []
        for p in people:
            if gender.lower() == p['gender'].lower():
                gender_people.append(p['first_name'])
        return gender_people
    else:
        people_q = []
        for p in people:
            if first_name.lower() == p['first_name'].lower():
                if gender.lower() == p['gender'].lower():
                    people_q.append(p)
        return {"Person": people_q}


####  Todo: Post

# todo: Add new person
@app.post("/add_person")
async def add_person(person: Person):
    p_id = max(p['id'] for p in people) + 1
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

    new_person = {
        'id': p_id,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'email': person.email,
        'gender': person.gender,
        'ip_address': ip
    }

    people.append(new_person)

    with open('people.json', 'w') as f:
        json.dump(people, f)

    return new_person


####  Todo: Put

# todo: Update person
@app.put("/updatePerson")
async def update_person(person: Person):
    new_person = {
        'id': person.id,
        'first_name': person.first_name,
        'last_name': person.last_name,
        'email': person.email,
        'gender': person.gender,
        'ip_address': person.ip_address
    }

    person_lst = []
    # get all the people with the id
    for p in people:
        if p['id'] == person.id:
            person_lst.append(p)

    if person_lst is None:
        raise HTTPException(
            status_code=404,
            detail="Person not found"
        )
    else:
        for per in person_lst:
            people.remove(per)
            people.append(new_person)

            with open('people.json', 'w') as f:
                json.dump(people, f)

        return people


####  Todo: Delete

@app.delete('/deletePerson/{p_id}')
async def delete_user(p_id: int):
    for p in people:
        if p_id == p['id']:
            people.remove(p)

            with open('people.json', 'w') as f:
                json.dump(people, f)

    return people
