""" Contains some functions required for some of the exercises """


def car_info_builder(manufacturer, model_name, **car_info):
    """ Builds a dictionary with info about a car """

    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info
