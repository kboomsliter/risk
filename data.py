# landmap holds only the names and relationships of the 
# map items.  objects will be created from this data.
# continent -> territory -> adjoining territories
landmap = {
        'North America': {
            'Alaska': [
                'Kamchatka',
                'NW Territory',
                'Alberta'
                ],
            'Alberta': [
                'NW Territory',
                'Alaska',
                'Ontario',
                'Western US',
                ],
            'Ontario': [
                'Alberta',
                'NW Territory',
                'Western US',
                'Eastern US',
                'Eastern Canada',
                'Greenland',
                ],
            'Eastern Canada': [
                'Eastern US',
                'Greenland',
                'Ontario',
                ],
            'NW Territory': [
                'Alaska',
                'Alberta',
                'Ontario',
                'Greenland',
                ],
            'Greenland': [
                'NW Territory',
                'Ontario',
                'Eastern Canada',
                'Iceland',
                ],
            'Western US': [
                'Ontario',
                'Alberta',
                'Eastern US',
                'Central America',
                ],
            'Eastern US': [
                'Ontario',
                'Eastern Canada',
                'Western US',
                'Central America',
                ],
            'Central America': [
                'Eastern US',
                'Western US',
                'Venezuela',
                ],
            },
        'South America': {
                'Venezuela': [
                    'Central America',
                    'Brazil',
                    'Peru',
                    ],
                'Brazil': [
                    'Venezuela',
                    'Peru',
                    'North Africa',
                    'Argentina',
                    ],
                'Peru': [
                    'Venezuela',
                    'Brazil',
                    'Argentina',
                    ],
                'Argentina': [
                    'Peru',
                    'Brazil',
                    ],
            },
        'Africa': {
                'North Africa': [
                    'Brazil',
                    'Western Europe',
                    'Southern Europe',
                    'Egypt',
                    'East Africa',
                    'Central Africa',
                    ],
                'Egypt': [
                    'Southern Europe',
                    'North Africa',
                    'East Africa',
                    'Middle East',
                    ],
                'East Africa': [
                    'North Africa',
                    'Egypt',
                    'Central Africa',
                    'South Africa',
                    'Madagascar',
                    'Middle East',
                    ],
                'Central Africa': [
                    'North Africa',
                    'East Africa',
                    'South Africa',
                    ],
                'South Africa': [
                    'East Africa',
                    'Central Africa',
                    'Madagascar',
                    ],
                'Madagascar': [
                    'South Africa',
                    'East Africa',
                    ],
            },
        'Europe': {
                'Iceland': [
                    'Greenland',
                    'Skandinavia',
                    'Great Britain',
                    ],
                'Great Britain': [
                    'Iceland',
                    'Skandinavia',
                    'Northern Europe',
                    'Western Europe',
                    ],
                'Skandinavia': [
                    'Iceland',
                    'Great Britain',
                    'Northern Europe',
                    'Russia',
                    ],
                'Russia': [
                    'Skandinavia',
                    'Northern Europe',
                    'Southern Europe',
                    'Ural',
                    'Afghanistan',
                    'Middle East',
                    ],
                'Northern Europe': [
                    'Skandinavia',
                    'Western Europe',
                    'Southern Europe',
                    'Russia',
                    'Great Britain',
                    ],
                'Southern Europe': [
                    'Western Europe',
                    'Northern Europe',
                    'Russia',
                    'Middle East',
                    'Egypt',
                    'North Africa',
                    ],
                'Western Europe': [
                    'Northern Europe',
                    'Southern Europe',
                    'Great Britain',
                    'North Africa',
                    ],
            },
        'Asia': {
                'Siberia': [
                    'Ural',
                    'China',
                    'Mongolia',
                    'Irkutsk',
                    'Yakutsk',
                    ],
                'Yakustk': [
                    'Siberia',
                    'Irkutsk',
                    'Kamchatka',
                    ],
                'Kamchatka': [
                    'Yakutsk',
                    'Irkutsk',
                    'Mongolia',
                    'Japan',
                    'Alaska',
                    ],
                'Ural': [
                    'Russia',
                    'Afghanistan',
                    'China',
                    'Siberia',
                    ],
                'Irkutsk': [
                    'Siberia',
                    'Yakutsk',
                    'Kamchatka',
                    'Mongolia',
                    ],
                'Mongolia': [
                    'Siberia',
                    'Irkutsk',
                    'Kamchatka',
                    'Japan',
                    'China',
                    ],
                'Japan': [
                    'Kamchatka',
                    'Mongolia',
                    ],
                'Afghanistan': [
                    'Russia',
                    'Ural',
                    'China',
                    'India',
                    'Middle East',
                    ],
                'China': [
                        'Ural',
                        'Siberia',
                        'Mongolia',
                        'Southeast Asia',
                        'India',
                        'Afghanistan',
                        ],
                'Middle East': [
                        'Southern Europe',
                        'Russia',
                        'Afghanistan',
                        'India',
                        'Egypt',
                        'East Africa',
                        ],
                'India': [
                        'Afghanistan',
                        'China',
                        'Southeast Asia',
                        'Middle East',
                        ],
                'Southeast Asia': [
                        'China',
                        'India',
                        'Indonesia',
                        ],
            },
        'Australia': {
                'New Guinea': [
                    'Indonesia',
                    'Eastern Australia',
                    ],
                'Indonesia': [
                    'Southeast Asia',
                    'New Guinea',
                    'Western Australia',
                    ],
                'Western Australia': [
                    'Indonesia',
                    'Eastern Australia',
                    ],
                'Eastern Australia': [
                    'New Guinea',
                    'Western Australia',
                    ],
                },
        }

continentProperties = {
        'North America': {
            'color': 'yellow',
            'troopBonus': 5,
            },
        'South America': {
            'color': 'orange',
            'troopBonus': 2,
            },
        'Europe': {
            'color': 'blue',
            'troopBonus': 5,
            },
        'Africa': {
            'color': 'red',
            'troopBonus': 3,
            },
        'Asia': {
            'color': 'green',
            'troopBonus': 7,
            },
        'Australia': {
            'color': 'purple',
            'troopBonus': 2,
            },
        }
