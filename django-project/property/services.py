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


def get_meters_for_unit(unit_id):
    """
    Method to retrieve all meters in a unit
    :param unit_id: unit_id
    :return: queryset of all meters in a unit.
    """
    try:
        unit = Unit.objects.get(id=unit_id)
        queryset = Meter.objects.filter(unit=unit.id)
        return queryset
    except ObjectDoesNotExist:
        raise Exception("Enter a valid ID")
    except ValueError:
        raise Exception("Enter a numerical value for ID")


def get_meter_reads_for_meter(meter_id):
    """
    Method to retrieve all meter reads of a meter
    :param meter_id: meter_id
    :return: queryset of all meter reads of a meter
    """
    try:
        meter = Meter.objects.get(id=meter_id)
        queryset = MeterRead.objects.filter(meter=meter.id)
        return queryset
    except ObjectDoesNotExist:
        raise Exception("Enter a valid ID")
    except ValueError:
        raise Exception("Enter a numerical value for ID")


def get_meter_errors_for_meter(meter_id):
    """
    Method to retrieve all meter errors of a meter
    :param meter_id: meter_id
    :return: queryset of all meter reads of a meter
    """
    try:
        meter = Meter.objects.get(id=meter_id)
        queryset = MeterError.objects.filter(meter=meter.id)
        return queryset
    except ObjectDoesNotExist:
        raise Exception("Enter a valid ID")
    except ValueError:
        raise Exception("Enter a numerical value for ID")


def get_units_for_property(property_id):
    """
    Method to retrieve all units of a property
    :param property_id: property_id
    :return: queryset of all units of a property
    """
    try:
        property = Property.objects.get(id=property_id)
        queryset = Unit.objects.filter(property=property.id)
        return queryset
    except ObjectDoesNotExist:
        raise Exception("Enter a valid ID")
    except ValueError:
        raise Exception("Enter a numerical value for ID")
