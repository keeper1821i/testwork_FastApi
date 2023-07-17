from typing import List, Dict

from tortoise import fields, Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Rates(Model):
    cargo_type = fields.CharField(max_length=15, description='Тип груза')
    rate = fields.DecimalField(max_digits=10, decimal_places=2, null=True)
    date = fields.CharField(max_length=10)


Rates_Pydantic = pydantic_model_creator(Rates, name='Rates')
RatesIn_Pydantic = pydantic_model_creator(Rates, name="RatesIn", exclude_readonly=True)
