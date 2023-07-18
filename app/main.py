import datetime

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from schemas import RateList
from services import get_cost_of_insurance, create_tariff

app = FastAPI()




@app.get("/rates")
async def get_rates(cargo_type, cost, date):
    return {'status': 200, ' Cтоимость страхования': await get_cost_of_insurance(cargo_type, cost, date)}


@app.post("/rates")
async def add_body(data: RateList):
    for key, value in data.data.items():
        for i in value:
            await create_tariff(i.cargo_type, i.rate, datetime.datetime.strptime(key, '%Y-%m-%d'))
    return {'status': 200}


register_tortoise(
    app,
    db_url="sqlite://DB_FILE",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
