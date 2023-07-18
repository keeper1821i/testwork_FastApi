import datetime
import decimal

from models import Rates


async def get_cost_of_insurance(cargo_type, cost, date):
    queryset = await Rates.filter(date__lte=datetime.datetime.strptime(date, '%Y-%m-%d')).filter(cargo_type=cargo_type). \
        order_by('-date').first()
    return queryset.rate * decimal.Decimal(cost)


async def create_tariff(cargo_type, rate, date):
    await Rates.create(cargo_type=cargo_type,
                       rate=rate,
                       date=date)
