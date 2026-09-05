import math


def solar_inverter_simulator():

    print("=" * 70)
    print("          GRID-CONNECTED SOLAR INVERTER SIMULATOR")
    print("=" * 70)

    # --------------------------------------------------
    # INPUTS
    # --------------------------------------------------

    pv_voltage = float(input("Enter PV DC voltage (V): "))
    pv_current = float(input("Enter PV DC current (A): "))
    inverter_efficiency = float(
        input("Enter inverter efficiency (%): ")
    )
    grid_voltage = float(
        input("Enter three-phase grid line voltage (V): ")
    )
    power_factor = float(
        input("Enter grid power factor: ")
    )
    inverter_rating = float(
        input("Enter inverter rated power (kW): ")
    )
    operating_hours = float(
        input("Enter operating time (hours): ")
    )

    # --------------------------------------------------
    # VALIDATION
    # --------------------------------------------------

    if pv_voltage <= 0:
        print("PV voltage must be greater than zero.")
        return

    if pv_current < 0:
        print("PV current cannot be negative.")
        return

    if not 0 < inverter_efficiency <= 100:
        print("Efficiency must be between 0 and 100%.")
        return

    if grid_voltage <= 0:
        print("Grid voltage must be greater than zero.")
        return

    if not 0 < power_factor <= 1:
        print("Power factor must be between 0 and 1.")
        return

    if inverter_rating <= 0:
        print("Inverter rating must be greater than zero.")
        return

    if operating_hours < 0:
        print("Operating hours cannot be negative.")
        return

    # --------------------------------------------------
    # DC SIDE
    # --------------------------------------------------

    dc_power = pv_voltage * pv_current
    dc_power_kw = dc_power / 1000

    # --------------------------------------------------
    # INVERTER
    # --------------------------------------------------

    efficiency_decimal = inverter_efficiency / 100

    ac_power = dc_power * efficiency_decimal
    ac_power_kw = ac_power / 1000

    inverter_loss = dc_power - ac_power

    # --------------------------------------------------
    # INVERTER RATING CHECK
    # --------------------------------------------------

    if ac_power_kw > inverter_rating:
        status = "OVERLOAD"
        usable_ac_power_kw = inverter_rating
        overload_power = ac_power_kw - inverter_rating
    else:
        status = "NORMAL"
        usable_ac_power_kw = ac_power_kw
        overload_power = 0

    # --------------------------------------------------
    # GRID SIDE
    # --------------------------------------------------

    grid_current = (
        usable_ac_power_kw * 1000
        / (
            math.sqrt(3)
            * grid_voltage
            * power_factor
        )
    )

    apparent_power = (
        math.sqrt(3)
        * grid_voltage
        * grid_current
    )

    apparent_power_kva = apparent_power / 1000

    # --------------------------------------------------
    # ENERGY
    # --------------------------------------------------

    energy_generated = usable_ac_power_kw * operating_hours

    # --------------------------------------------------
    # DISPLAY RESULTS
    # --------------------------------------------------

    print("\n" + "-" * 70)
    print("SOLAR PV INPUT")
    print("-" * 70)

    print(f"PV DC Voltage       : {pv_voltage:.2f} V")
    print(f"PV DC Current       : {pv_current:.2f} A")
    print(f"PV DC Power         : {dc_power:.2f} W")
    print(f"PV DC Power         : {dc_power_kw:.3f} kW")

    print("\n" + "-" * 70)
    print("INVERTER ANALYSIS")
    print("-" * 70)

    print(f"Inverter Efficiency : {inverter_efficiency:.2f} %")
    print(f"AC Output Power     : {ac_power_kw:.3f} kW")
    print(f"Inverter Loss       : {inverter_loss:.2f} W")
    print(f"Inverter Rating     : {inverter_rating:.2f} kW")

    print("\n" + "-" * 70)
    print("GRID CONNECTION")
    print("-" * 70)

    print(f"Grid Voltage        : {grid_voltage:.2f} V")
    print(f"Power Factor        : {power_factor:.2f}")
    print(f"Grid Current        : {grid_current:.2f} A")
    print(f"Apparent Power      : {apparent_power_kva:.3f} kVA")

    print("\n" + "-" * 70)
    print("ENERGY ANALYSIS")
    print("-" * 70)

    print(f"Operating Time      : {operating_hours:.2f} hours")
    print(f"Energy Generated    : {energy_generated:.3f} kWh")

    print("\n" + "-" * 70)
    print("SYSTEM STATUS")
    print("-" * 70)

    if status == "OVERLOAD":
        print("Inverter Status     : OVERLOAD")
        print(f"Excess Power       : {overload_power:.3f} kW")
    else:
        print("Inverter Status     : NORMAL")

    if power_factor >= 0.95:
        print("Grid Power Quality  : GOOD")
    elif power_factor >= 0.85:
        print("Grid Power Quality  : ACCEPTABLE")
    else:
        print("Grid Power Quality  : LOW")

    print("\nGrid-connected solar inverter simulation completed.")

    print("=" * 70)


if __name__ == "__main__":
    solar_inverter_simulator()
