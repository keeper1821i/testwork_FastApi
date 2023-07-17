import json
import os
from typing import List, Dict

from fastapi import FastAPI, Request
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise

from models import Rates_Pydantic, Rates, RatesIn_Pydantic

app = FastAPI()


basedir = os.path.abspath(os.path.dirname(__file__))


@app.get("/rates", response_model=List[Rates_Pydantic])
async def get_rates():
    return await Rates_Pydantic.from_queryset(Rates.all())


class Rate(BaseModel):
    cargo_type: str
    rate: str


class RateList(BaseModel):
    data: Dict[str, List[Rate]]


test_list = []

@app.post("/rates")
async def add_body(data: RateList):
    test_list.extend(data)
    key_list =data.data.values()

    # for i in data:
    #     # await Rates.create(cargo_type=data.data[i][0].cargo_type,
    #     #                    rate=float(data.data[i][0].rate),
    #     #                    date=i)
    #     print(i[1].keys())
    #     # print(data.data[i][0].cargo_type)
    #     # print(data.data[i][0].rate)
    return {'status': 200}


register_tortoise(
    app,
    db_url="sqlite://DB_FILE",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
