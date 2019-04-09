"""
=======================================
Constants for Tests and active debugger
=======================================
"""
ENV = ""
DEBUG = True
TESTING = True
LIVESERVER_PORT = 8943
LIVESERVER_TIMEOUT = 10

MSG_TEST_NO_RESULT = [
    "Salut Grandpy Bot, c'est quoi l'adresse ?",
    "C'est quoi la rue",
    "peux-tu me données le lieu ?",
    "comment vas-tu ?",
    "comment ca va ?",
    "salur",
]

MSG_TEST_OC = [
    "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?",
    "Je cherche la rue d'OpenClassrooms",
    "Peux-tu me donner le lieu ou se trouve OpenClassrooms ?",
    "Je souhaiterais connaître les coordonnées d'OpenClassrooms",
    "Ou se trouve OpenClassrooms ?",
]

"""
Parameters for OpenClassrooms and Liberty Statue
"""
KEY_WORDS_TEST = [["adresse", "openclassrooms"], ["adresse", "statue", "libertée"]]

FORMATTED_ADDRESS = [
    "7 Cité Paradis, 75010 Paris, France", "Statue of Liberty National Monument, New York, NY 10004, USA"
]

LOCATION = [
    {
        'geometry': {'lng': 2.3505517, 'lat': 48.8747265},
        'route': 'Cité Paradis',
        'city': 'Paris',
        'country': 'FR'
    },
    {
        'geometry': {'lng': -74.04450039999999, 'lat': 40.6892494},
        'route': 'Statue of Liberty National Monument',
        'city': 'New York',
        'country': 'US'
    }
]

RESULT = [
    [{
        "address_components": [
            {
                "long_name": "7",
                "short_name": "7",
                "types": [
                    "street_number"
                ]
            },
            {
                "long_name": "Cité Paradis",
                "short_name": "Cité Paradis",
                "types": [
                    "route"
                ]
            },
            {
                "long_name": "Paris",
                "short_name": "Paris",
                "types": [
                    "locality",
                    "political"
                ]
            },
            {
                "long_name": "Arrondissement de Paris",
                "short_name": "Arrondissement de Paris",
                "types": [
                    "administrative_area_level_2",
                    "political"
                ]
            },
            {
                "long_name": "Île-de-France",
                "short_name": "Île-de-France",
                "types": [
                    "administrative_area_level_1",
                    "political"
                ]
            },
            {
                "long_name": "France",
                "short_name": "FR",
                "types": [
                    "country",
                    "political"
                ]
            },
            {
                "long_name": "75010",
                "short_name": "75010",
                "types": [
                    "postal_code"
                ]
            }
        ],
        "formatted_address": "7 Cité Paradis, 75010 Paris, France",
        "geometry": {
            "location": {
                "lat": 48.8747265,
                "lng": 2.3505517
            },
            "location_type": "ROOFTOP",
            "viewport": {
                "northeast": {
                    "lat": 48.8760754802915,
                    "lng": 2.351900680291502
                },
                "southwest": {
                    "lat": 48.8733775197085,
                    "lng": 2.349202719708498
                }
            }
        },
    }],
    [{
        "address_components": [
            {
                "long_name": "Statue of Liberty National Monument",
                "short_name": "Statue of Liberty National Monument",
                "types": [
                    "establishment",
                    "park",
                    "point_of_interest"
                ]
            },
            {
                "long_name": "Manhattan",
                "short_name": "Manhattan",
                "types": [
                    "political",
                    "sublocality",
                    "sublocality_level_1"
                ]
            },
            {
                "long_name": "New York",
                "short_name": "New York",
                "types": [
                    "locality",
                    "political"
                ]
            },
            {
                "long_name": "New York County",
                "short_name": "New York County",
                "types": [
                    "administrative_area_level_2",
                    "political"
                ]
            },
            {
                "long_name": "New York",
                "short_name": "NY",
                "types": [
                    "administrative_area_level_1",
                    "political"
                ]
            },
            {
                "long_name": "United States",
                "short_name": "US",
                "types": [
                    "country",
                    "political"
                ]
            },
            {
                "long_name": "10004",
                "short_name": "10004",
                "types": [
                    "postal_code"
                ]
            }
        ],
        "formatted_address": "Statue of Liberty National Monument, New York, NY 10004, USA",
        "geometry": {
            "location": {
                "lat": 40.6892494,
                "lng": -74.04450039999999
            },
            "location_type": "GEOMETRIC_CENTER",
            "viewport": {
                "northeast": {
                    "lat": 40.6905983802915,
                    "lng": -74.04315141970848
                },
                "southwest": {
                    "lat": 40.6879004197085,
                    "lng": -74.04584938029149
                }
            }
        },
    }]
]
