import csv

with open('logbook.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Date", "Aircraft Type", "Aircraft Ident", "Route of Flight", "Remarks and Endorsements", "Single-Engine Land", "Multi-Engine Land", "Night", "Actual Instrument", "Simulated Instrument", "Flight Simulator", "Cross Country", "Solo", "Dual Recieved", "Pilot In Command"]