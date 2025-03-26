
import streamlit as st


def convert_units(value, unit_from, unit_to):

    conversions={
         # Length
        "meter_kilometer": 0.001, "kilometer_meter": 1000,
        "meter_centimeter": 100, "centimeter_meter": 0.01,
        "centimeter_inch": 0.393701, "inch_centimeter": 2.54,
        "inch_foot": 1/12, "foot_inch": 12,
        "foot_yard": 1/3, "yard_foot": 3,
        "yard_meter": 0.9144, "meter_yard": 1.09361,
        "mile_kilometer": 1.60934, "kilometer_mile": 0.621371,
        "kilometer_centimeter": 100000, "centimeter_kilometer": 0.00001,
        "kilometer_millimeter": 1000000, "millimeter_kilometer": 0.000001,
        "kilometer_inch": 39370.1, "inch_kilometer": 0.0000254,
        "kilometer_foot": 3280.84, "foot_kilometer": 0.0003048,
        "kilometer_yard": 1093.61, "yard_kilometer": 0.0009144,
        "mile_meter": 1609.34, "meter_mile": 0.000621371,
        "mile_centimeter": 160934, "centimeter_mile": 0.00000621371,
        "mile_millimeter": 1609340, "millimeter_mile": 0.000000621371,
        
        # Weight
        "gram_kilogram": 0.001, "kilogram_gram": 1000,
        "gram_milligram": 1000, "milligram_gram": 0.001,
        "kilogram_milligram": 1000000, "milligram_kilogram": 0.000001,
        
        
        # Volume
        "liter_milliliter": 1000, "milliliter_liter": 0.001,
        
        # Temperature (Handled Separately)
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        conversion = conversions[key]
        return conversion(value) if callable(conversion) else value * conversion
    else:
        return "Conversion not supported"

st.title("Unit Converter")

value = st.number_input("Enter the Value:", min_value=1.0, step=1.0)

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "centimeter", "inch", "foot", "yard", "mile",
                                           "gram", "kilogram", "milligram",
                                           "liter", "milliliter", "celsius", "fahrenheit"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "centimeter", "inch", "foot", "yard", "mile",
                                       "gram", "kilogram", "milligram",
                                       "liter", "milliliter", "celsius", "fahrenheit"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result} ")