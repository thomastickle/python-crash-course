from chapter11.city_functions import format_city_country


def test_city_country():
    formatted_city_country = format_city_country("Santiago", "Chile")
    assert formatted_city_country == "Santiago, Chile"


def test_city_country_population():
    formatted_city_country = format_city_country("Santiago", "Chile", "5000000")
    assert formatted_city_country == "Santiago, Chile - population 5000000"
