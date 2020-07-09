from core.models.property import Unit, Meter, MeterRead


def get_meters_for_property(property_id, utility_type):
    """ Method to fetch all meters for a property_id """
    return Meter.objects.filter(unit__in=Unit.objects.filter(
        property=property_id), utility=utility_type)


def get_meter_reads_for_meterlist(meter_list, date):
    """ Method returns all meter reads for a meter in meter list and date """
    return list(MeterRead.objects.filter(
        meter__in=meter_list, read_date__contains=date).order_by('read_date'))


def get_amount_from_meter_reads(meter_read_list, meter):
    """ Method to fetch the read value of a meter from meter read list"""
    if not meter_read_list:
        return None

    for read in meter_read_list:
        if read.meter.name == meter.name:
            return read.amount
    return None


def get_utility_usage_amount_for_property(property_id, from_date,
                                          to_date, utility_type):
    """
    Method to calculate usage amount for a
    property for a date range and utility type
    """
    meters = get_meters_for_property(property_id, utility_type)

    meter_read_list_old = get_meter_reads_for_meterlist(meters, from_date)
    meter_read_list_new = get_meter_reads_for_meterlist(meters, to_date)
    total_amount = 0
    meter_read_error_old = []
    meter_read_error_new = []
    for meter in meters:
        old_amount = get_amount_from_meter_reads(meter_read_list_old, meter)
        new_amount = get_amount_from_meter_reads(meter_read_list_new, meter)

        if not old_amount:
            meter_read_error_old.append(str(meter))

        if not new_amount:
            meter_read_error_new.append(str(meter))

        if old_amount and new_amount:
            total_amount += new_amount - old_amount

    result = {"amount": total_amount, "from_date_error": meter_read_error_old,
              "to_date_error": meter_read_error_new}
    return result
