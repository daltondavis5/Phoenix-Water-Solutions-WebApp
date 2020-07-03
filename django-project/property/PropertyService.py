from core.models.property import Unit, Meter, MeterRead
import datetime


def get_meters_for_property(property_id, utility_type):
    """ Method to fetch all meters for a property_id """
    unit_list = Unit.objects.filter(property=property_id)
    return Meter.objects.filter(unit__in=unit_list, utility=utility_type)


def get_meter_reads_for_unitlist_utility(meter_list, date):
    """ Method to fetch all meters for a unit object and utility_id """
    d = datetime(date)
    return MeterRead.objects.filter(meter__in=meter_list, read_date=d)


def get_property_amount(property_id, from_date, to_date, utility_type):
    """ Method to fetch all meter amounts for all units in a single property"""
    meter_list = get_meters_for_property(property_id, utility_type)
    meter_read_list_old = get_meter_reads_for_unitlist_utility(meter_list, from_date)
    meter_read_list_new = get_meter_reads_for_unitlist_utility(meter_list, to_date)
    print("meter_read_list_old : ", meter_read_list_old)

    total_amount = 0
    if meter_read_list_old and meter_read_list_new:
        for meter_old, meter_new in meter_read_list_old, meter_read_list_new:
            total_amount += meter_old.amount - meter_new
    return total_amount
