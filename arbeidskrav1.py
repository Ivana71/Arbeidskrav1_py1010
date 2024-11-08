# Generelt
antall_kjørte_km = 10_000
trafikkforsikring_kr_per_dag = 8.38
dager_per_ar = 365

# Kalkulerer trafikkforsikringsavgift for begge biltyper
trafikkforsikringsavgift_aar = trafikkforsikring_kr_per_dag * dager_per_ar
print("Trafikkforsikringsavgift per år:", trafikkforsikringsavgift_aar)

# Elbil
elbil_forsikring_kr_per_ar = 5000
elbil_forbruk_kwh_per_km = 0.2
strompris_kr_per_kwh = 2.0
elbil_bom_kr_per_km = 0.1

# Beregner elbilkostnader
drivstoffkostnad_elbil = elbil_forbruk_kwh_per_km * strompris_kr_per_kwh * antall_kjørte_km
bomkostnad_elbil = elbil_bom_kr_per_km * antall_kjørte_km
totalkostnad_elbil = elbil_forsikring_kr_per_ar + trafikkforsikringsavgift_aar + drivstoffkostnad_elbil + bomkostnad_elbil

# Skriver ut elbilkostnader
print("Totalkostnad for elbil per år:", totalkostnad_elbil)

# Bensinbil
bensin_forsikring_kr_per_ar = 7500
bensin_forbruk_kr_per_km = 1.0
bensin_bom_kr_per_km = 0.3

# Beregner bensinbilkostnader
drivstoffkostnad_bensinbil = bensin_forbruk_kr_per_km * antall_kjørte_km
bomkostnad_bensinbil = bensin_bom_kr_per_km * antall_kjørte_km
totalkostnad_bensinbil = bensin_forsikring_kr_per_ar + trafikkforsikringsavgift_aar + drivstoffkostnad_bensinbil + bomkostnad_bensinbil

# Skriver ut bensinbilkostnader
print("Totalkostnad for bensinbil per år:", totalkostnad_bensinbil)

# Beregner og skriver ut kostnadsdifferansen
kostnadsdifferanse = abs(totalkostnad_elbil - totalkostnad_bensinbil)
print("Kostnadsdifferanse per år mellom elbil og bensinbil:", kostnadsdifferanse)
