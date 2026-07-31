def format_city_country(city: str, country: str, population: str | None = None) -> str:
    if population is None:
        return f"{city}, {country}"
    else:
        return f"{city}, {country} - population {population}"
