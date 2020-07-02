from core.models.property import Meter, Property, Unit, \
    PropertyUtilityProviderInfo, MeterRead, MeterError
from django.core.exceptions import ObjectDoesNotExist


def get_last_read_info_for_meter(meter_obj):
    """
    Method to retrieve Last Read Info for a given meter
    :param meter_obj: object of model: Meter
    :return: list of last read info: [amount, read date]
    """
    try:
        last_read_obj = meter_obj.meterread_set.latest('read_date')
        last_read_info = [last_read_obj.amount, last_read_obj.read_date]
        return last_read_info
    except ObjectDoesNotExist:
        return None
