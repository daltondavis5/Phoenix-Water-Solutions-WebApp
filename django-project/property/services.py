from core.models.property import Meter, Property, Unit, \
    MeterRead, MeterError
from django.core.exceptions import ObjectDoesNotExist
from core.exceptions.exceptions import NonNumericalValueException,\
    InvalidIDException


def get_last_read_info_for_meter(meter_obj):
    """Retrieve Last Read Info for a given Meter object

        Keyword arguments:
        meter_obj -- an instance of Meter model
        
        Returns:
        list -- list of last read info [amount, read date]

        Exceptions:
        ObjectDoesNotExist -- if no associated meter object exists
        in the database, return None
    """
    try:
        last_read_obj = meter_obj.meterread_set.latest('read_date')
        last_read_info = [last_read_obj.amount, last_read_obj.read_date]
        return last_read_info
    except ObjectDoesNotExist:
        return None


def get_meters_for_unit(unit_id):
    """Retrieve all meters associated a Unit object

        Keyword arguments:
        unit_id (int) -- id of an existing Unit instance

        Returns:
        QuerySet -- queryset of Meters

        Exceptions:
        ObjectDoesNotExist -- if no associated meter object exists in the
        database, raise custom InvalidIDException
        ValueError -- if ValueError occurs, raise custom
        NonNumericalValueException
    """
    try:
        unit = Unit.objects.get(id=unit_id)
        queryset = Meter.objects.filter(unit=unit.id)
        return queryset
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException


def get_meter_reads_for_meter(meter_id):
    """Retrieve all Meter Reads associated with a Meter object

        Keyword arguments:
        meter_id (int) -- id of an existing Meter instance

        Returns:
        QuerySet -- queryset of MeterReads

        Exceptions:
        ObjectDoesNotExist -- if no associated meter object exists
        in the database, raise custom InvalidIDException
        ValueError -- if ValueError occurs, raise custom
        NonNumericalValueException
    """
    try:
        meter = Meter.objects.get(id=meter_id)
        queryset = MeterRead.objects.filter(meter=meter.id)
        return queryset
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException


def get_meter_errors_for_meter(meter_id):
    """Retrieve all MeterErrors associated with a Meter object

        Keyword arguments:
        meter_id (int) -- id of an existing Meter instance

        Returns:
        QuerySet -- queryset of all MeterErrors

        Exceptions:
        ObjectDoesNotExist -- if no associated meter object exists
        in the database, raise custom InvalidIDException
        ValueError -- if ValueError occurs, raise custom
        NonNumericalValueException
    """
    try:
        meter = Meter.objects.get(id=meter_id)
        queryset = MeterError.objects.filter(meter=meter.id)
        return queryset
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException


def get_units_for_property(property_id):
    """Retrieve all Units associated with a Property instance

        Keyword arguments:
        property_id (int) -- id of an existing Property instance

        Returns:
        QuerySet -- queryset of Units

        Exceptions:
        ObjectDoesNotExist -- if no associated meter object exists
        in the database, raise custom InvalidIDException
        ValueError -- if ValueError occurs, raise custom
        NonNumericalValueException
    """
    try:
        property = Property.objects.get(id=property_id)
        queryset = Unit.objects.filter(property=property.id)
        return queryset
    except ObjectDoesNotExist:
        raise InvalidIDException
    except ValueError:
        raise NonNumericalValueException
