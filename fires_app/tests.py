from datetime import datetime
from decimal import Decimal

# Create your tests here.
def main():
    acq_datetime = ''.join(['2018-09-06', '0000'])
    print (acq_datetime)
    print (datetime.strptime(acq_datetime, '%Y-%m-%d%H%M'))

main()