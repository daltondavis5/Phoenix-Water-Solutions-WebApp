from core.models.property import Unit, Meter, MeterRead


def get_units_for_property(property_id):
    """ Method to fetch all units for a property_id """
    return Unit.objects.filter(property=property_id)


def get_meters_for_unit_utility(unit, utility_id):
    """ Method to fetch all meters for a unit object and utility_id """
    return Meter.objects.filter(unit=unit, utility=utility_id)


# TODO : make this for a specific day, fetch the latest read
def get_meter_reads_for_dates(meter,from_date, to_date):
    """ Method to fetch all meters for a unit object and utility_id """
    return MeterRead.objects.filter(meter=meter,
                                    read_date__range=[from_date, to_date])


def get_property_amount(property_id, utility_id, from_date, to_date):
    """ Method to fetch all meter amounts for all units in a single property"""
    unit_list = get_units_for_property(property_id)
    unit_amount = 0

    # For loop to iterate through all units
    for unit in unit_list:
        meter_list = get_meters_for_unit_utility(unit, utility_id)
        # print("meter list : ", meter_list)

        meter_amount = 0
        # For loop to check amount for every meter
        for meter in meter_list:
            meter_read_list = get_meter_reads_for_dates(meter,
                                                        from_date, to_date)

            # print("meterread_list : ", meterread[0].amount)
            if meter_read_list:
                for m in meter_read_list:
                    meter_amount += m.amount
        print("Total amount for this meter: ", meter_amount)
        unit_amount += meter_amount
    print("Total Unit Amount: ", unit_amount)
    return unit_amount
