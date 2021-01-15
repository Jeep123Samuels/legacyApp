
airtime: str = 'Airtime'
db_transfer: str = 'DB Transfer'
engen_riebeek: str = 'Engen Riebeek'
geard_malmesbury: str = 'Geard Pharmacy'
heyns_pharmacy: str = 'Heyns Pharmacy'
overberg_moor: str = 'Overberg Agri Moorreesburg'
pnp_riebeeck: str = 'PnP Family Riebeeck'
spar_moor: str = 'Spar Moorrees'
steam: str = 'Steam Game'
tops_moor: str = 'Tops Moorrees'
transfer_debit: str = 'Transfer from DB'
wife: str = 'Wife'

specie_data: dict = {
    'credit_events': [
        # storage_id is the index of the key-value under storage.
        # So we need to take the description of that index object and add to db.
        dict(description='SARS Payment', amount=44.43, occurred_on='17-12-20', storage_id=2),
        dict(description=wife, amount=10000, occurred_on='21-12-20', storage_id=2),
        dict(description='Herotel', amount=1099, occurred_on='21-12-20', storage_id=2),
        dict(description='Home Loan', amount=300, occurred_on='21-12-20', storage_id=2),
        dict(description=transfer_debit, amount=500, occurred_on='21-12-20', storage_id=2),
        dict(description=transfer_debit, amount=10323, occurred_on='21-12-20', storage_id=2),
        dict(description=transfer_debit, amount=800, occurred_on='28-12-20', storage_id=2),
        dict(description='Account Fee', amount=219, occurred_on='29-12-20', storage_id=2),
        dict(description='Added Serv Fee', amount=2.25, occurred_on='29-12-20', storage_id=2),
        dict(description='Atm Cash', amount=150, occurred_on='30-12-20', storage_id=2),
        dict(description='H loan paid', amount=7541.81, occurred_on='31-12-20', storage_id=2),
        dict(description=transfer_debit, amount=1000, occurred_on='02-01-21', storage_id=2),
        dict(description=transfer_debit, amount=2716, occurred_on='02-01-21', storage_id=2),
        dict(description='Brolink', amount=859.95, occurred_on='02-01-21', storage_id=2),
        dict(description='MTN Sp', amount=560, occurred_on='02-01-21', storage_id=2),
        dict(description=transfer_debit, amount=400, occurred_on='02-01-21', storage_id=2),
        dict(description='Atm Cash', amount=250, occurred_on='06-01-21', storage_id=2),
        dict(description='School', amount=3000, occurred_on='07-01-21', storage_id=2),
        dict(description='School', amount=846, occurred_on='11-01-21', storage_id=2),

        # CD events related
        dict(description=airtime, amount=15, occurred_on='18-12-20', storage_id=1),
        dict(description=spar_moor, amount=342.67, occurred_on='18-12-20', storage_id=1),
        dict(description=overberg_moor, amount=490.98, occurred_on='18-12-20', storage_id=1),
        dict(description=spar_moor, amount=108.23, occurred_on='19-12-20', storage_id=1),
        dict(description='Netflix', amount=169, occurred_on='21-12-20', storage_id=1),
        dict(description='Petrol', amount=350, occurred_on='21-12-20', storage_id=1),
        dict(description=pnp_riebeeck, amount=51.87, occurred_on='21-12-20', storage_id=1),
        dict(description=pnp_riebeeck, amount=160.99, occurred_on='21-12-20', storage_id=1),
        dict(description=heyns_pharmacy, amount=1261.46, occurred_on='22-12-20', storage_id=1),
        dict(description=steam, amount=257.95, occurred_on='22-12-20', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='23-12-20', storage_id=1),
        dict(description=pnp_riebeeck, amount=195.65, occurred_on='23-12-20', storage_id=1),
        dict(description=airtime, amount=200, occurred_on='24-12-20', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='28-12-20', storage_id=1),
        dict(description='Dischem Kuilsriver', amount=92.65, occurred_on='28-12-20', storage_id=1),
        dict(description='Computer Mania', amount=599, occurred_on='28-12-20', storage_id=1),
        dict(description='Fuel', amount=46, occurred_on='29-12-20', storage_id=1),
        dict(description='Mcd Malmesbury', amount=60, occurred_on='29-12-20', storage_id=1),
        dict(description='Showmax', amount=99, occurred_on='29-12-20', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='30-12-20', storage_id=1),
        dict(description=spar_moor, amount=273.70, occurred_on='30-12-20', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='31-12-20', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='31-12-20', storage_id=1),
        dict(description='Petrol', amount=250, occurred_on='31-12-20', storage_id=1),
        dict(description=spar_moor, amount=265.73, occurred_on='31-12-20', storage_id=1),
        dict(description=spar_moor, amount=394.19, occurred_on='31-12-20', storage_id=1),
        dict(description='Takelot Online', amount=1199, occurred_on='31-12-20', storage_id=1),
        dict(description='Shoewax', amount=278, occurred_on='01-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='02-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='04-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='04-01-21', storage_id=1),
        dict(description=heyns_pharmacy, amount=89.90, occurred_on='04-01-21', storage_id=1),
        dict(description=engen_riebeek, amount=200, occurred_on='04-01-21', storage_id=1),
        dict(description=spar_moor, amount=160.53, occurred_on='04-01-21', storage_id=1),
        dict(description='Petrol', amount=300.06, occurred_on='04-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='05-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='05-01-21', storage_id=1),
        dict(description=geard_malmesbury, amount=89.90, occurred_on='05-01-21', storage_id=1),
        dict(description=geard_malmesbury, amount=105.71, occurred_on='05-01-21', storage_id=1),
        dict(description=spar_moor, amount=87.54, occurred_on='05-01-21', storage_id=1),
        dict(description='Steam', amount=120, occurred_on='05-01-21', storage_id=1),
        dict(description='Midas', amount=147.40, occurred_on='05-01-21', storage_id=1),
        dict(description='Fuels', amount=119.75, occurred_on='05-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='06-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='06-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='06-01-21', storage_id=1),
        dict(description=spar_moor, amount=88.96, occurred_on='06-01-21', storage_id=1),
        dict(description='shops', amount=166, occurred_on='06-01-21', storage_id=1),
        dict(description='transfer school', amount=3000, occurred_on='07-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='07-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='07-01-21', storage_id=1),
        dict(description='Shoprite', amount=119.43, occurred_on='07-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='08-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='08-01-21', storage_id=1),
        dict(description=airtime, amount=15, occurred_on='08-01-21', storage_id=1),
        dict(description='Deb protect', amount=26.79, occurred_on='08-01-21', storage_id=1),
        dict(description='Interest', amount=7.35, occurred_on='08-01-21', storage_id=1),
        # dict(description=steam, amount=68.38, occurred_on='08-01-21', storage_id=1),
        dict(description=spar_moor, amount=515.14, occurred_on='09-01-21', storage_id=1),
        # dict(description=spar_moor, amount=515.14, occurred_on='09-01-21', storage_id=1),
    ],
    'debit_events': [
        dict(description=db_transfer, amount=500, occurred_on='21-12-20', storage_id=0),
        dict(description=db_transfer, amount=1.63, occurred_on='24-12-20', storage_id=0),

        dict(description='Payment', amount=230, occurred_on='23-12-20', storage_id=2),
        dict(description='Payment', amount=400, occurred_on='02-01-21', storage_id=2),
        dict(description='School', amount=3000, occurred_on='07-01-21', storage_id=2),
        dict(description='Payment', amount=715, occurred_on='09-01-21', storage_id=2),

        # CD events related
        dict(description=db_transfer, amount=10323, occurred_on='21-12-20', storage_id=1),
        dict(description=db_transfer, amount=1000, occurred_on='02-01-21', storage_id=1),
        dict(description=db_transfer, amount=2716, occurred_on='02-01-21', storage_id=1),
        dict(description=db_transfer, amount=400, occurred_on='02-01-21', storage_id=1),
        dict(description=db_transfer, amount=846, occurred_on='11-01-21', storage_id=1),

    ],
    'storages': [
        dict(description='Money Call', total=6000.39),
        dict(description='CD', total=-16490.50),
        dict(description='DB', total=36466.47),
    ],
}

users: list = [
    dict(username='jp', email='jeep123samuels@gmail.com', password='cGFzc3dvcmQ='),
]
