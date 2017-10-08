from datetime import date
from datetime import timedelta

buscarfecha = date.today() - timedelta(days=20)
print buscarfecha.day
