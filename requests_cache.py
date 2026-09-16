import requests
from requests import Response
import requests_cache  # pip install requests-cache


requests_cache.install_cache("country_cache", expire_after=300)


def get_country_info(country_name):
    url = f"https://rescountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        country_data = response.json()[0]
        source = "CACHE" if getattr(response, "from_cache", False) else "API"

        return {
            "Source": source,
            "Name": country_data.get("name", {}).get("common", "N/A"),
            "Capital": country_data.get("capital", ["N/A"])[0],
        }
    except Exception as e:
        return {"Error": f"{e}"}


def main():
    while True:
        country = input("Enter a country name:  ").lower().strip()
        info = get_country_info(country)

        print("\nCountry Information:")
        print("------------------------")
        for key, value in info.items():
            print(f"{key}, {value}")
        print()


if __name__ == "__main__":
    main()


# ---------- getattr() method -------------
# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role

# person = User("Alice", "Admin")

# # Traditional dot notation
# print(person.name)  # Output: Alice

# # Dynamic lookup using getattr()
# field_to_get = "role"
# print(getattr(person, field_to_get))  # Output: Admin
#
#
# Parameters
# object: The object whose attribute you want to access.
# name: A string representing the exact name of the attribute.
# default (Optional): The value returned if the attribute does not exist. If omitted and the attribute is missing, Python raises an AttributeError
