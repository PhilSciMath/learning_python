"""
    Test for the modified version of city_country()
"""

from city_functions import  city_country


def test_city_country_population():
    """ Does 'Santiago, Chile - Population: 500000' work? """
    result = city_country('santiago', 'chile', 500000)
    assert result == "Santiago, Chile - Population: 500000"
