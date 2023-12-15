import random

while True:
    choice = int(input("Enter a choice for difficulty (1-3): "))

    if 1 <= choice <= 3:
        break
    else:
        choice = int(input("Enter a choice for difficulty (1-3): "))

acronyms = [
    {
        "AV1ATE": [
            {"A": 'Anuual inspection'},
            {"V": "VOR check"},
            {"1": "100 Hour inspection"},
            {"A": "Airworthiness Directives"},
            {"T": "Transponder check"},
            {"E": "Emergency Location Transmitter"},
            {"S": "Static system check"}
        ],
        "ARROW" : [
            {'A': 'Airworthiness Certificate'},
            {'R': 'Registration Certificate'},
            {"O": "Operation Limitations"},
            {"W": "Weight and Balance"}
        ],
        "SAFETY": [
            {"S": "Seat Belts"},
            {"A": "Air Ventilation"},
            {"F": "Fire Extinguisher"},
            {"E": "Emergency Procedure"},
            {"T": "Traffic"},
            {"Y": "Your Questions"}
        ],
        "NWKRAFT": [
            {"N": "NOTAMs"},
            {"W": "Weather"},
            {"K": "Known ATC Delays"},
            {"R": "Runway Lengths"},
            {"A": "Alternate Airport"},
            {"F": "Fuel"},
            {"T": "Takeoff and Landing Distances"}
        ],
        "A TOMATO FLAMES": [
            {"A": "Altimeter"},
            {"T": 'Tachometer'},
            {'O': "Oil Pressure Gauge"},
            {'M': 'Magnetic Compass'},
            {'A': "Airspeed Indicator"},
            {"T": "Temperature Gague"},
            {"O": "Oil Temperature Gauge"},
            {"F": "Fuel Gauge"},
            {"L": "Landing Gear Indicator"},
            {"A": "Anti Collision Lights"},
            {"M": "Manifold Pressure Gauge"},
            {"E": "Emergency Equipment"},
            {"S": "Seat Belts"}
        ],
        "FLAPS": [
            {"F": "Fuses"},
            {"L": "Landing Lights"},
            {"A": "Anti-Collision Lights"},
            {"P": "Position Lights"},
            {"S": "Source of Power"}
        ],
        "PAVE": [
            {"P": "Pilot"},
            {"A": "Aircraft"},
            {"V": "Environment"},
            {"E": "External Pressures"}
        ],
        "IM SAFE": [
            {"I": "Illness"},
            {"M": "Medication"},
            {"S": "Stress"},
            {"A": "Alcohol"},
            {"F": "Fatigue"},
            {"E": "Emotions"}
        ],
        "ANC": [
            {"A": "Aviate"},
            {"N": "Navigate"},
            {"C": "Communicate"}
        ],
        "The 5 T's": [
            {"T": "Twist"},
            {"T": "Turn"},
            {"T": "Time"},
            {"T": "Throttle"},
            {"T": "Talk"}
        ],
        "The 5 P's": [
            {"P": "Plane"},
            {"P": "Pilot"},
            {"P": "Plan"},
            {"P": "Programming"},
            {"P": "Passengers"}
        ],
        "DECIDE": [
            {"D": "Detect"},
            {"E": "Estimate"},
            {"C": "Choose"},
            {"I": "Identify"},
            {"D": "Do"},
            {"E": "Evaluate"}
        ]
    }
]

if choice == 1:
    rand = random.randint(0, 2)
elif choice == 2:
    rand = random.randint(0, 6)
else:
    rand = random.randint(0, 11)

test = list(acronyms[0].values())[1]

hold = []

print(rand)

if rand == 0:
    rand = 1

for i in range(rand):
    rand2 = random.randint(0, 11)
    print(rand2)
    print(list(acronyms[0].values())[rand2])
    
