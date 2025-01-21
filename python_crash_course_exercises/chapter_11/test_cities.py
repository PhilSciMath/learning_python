"""
    Test for the city_country() function
"""

from city_functions import city_country

def test_city_country():
    """ Does names like 'Santiago, Chile' work. """
    formatted_name = city_country('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'