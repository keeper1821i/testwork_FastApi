from tortoise import fields, Model


class Rates(Model):
    cargo_type = fields.CharField(max_length=15, description='Тип груза')
    rate = fields.DecimalField(max_digits=10, decimal_places=3, null=True)
    date = fields.DateField()


