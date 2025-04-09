import streamlit as st
import requests

# Set up the app
st.title("Currency Converter")

# User inputs
amount = st.number_input("Enter amount", min_value=0.01)
from_currency = st.selectbox("From", ["USD", "EUR", "PKR", "GBP"])
to_currency = st.selectbox("To", ["USD", "EUR", "PKR", "GBP"])

# Conversion button
if st.button("Convert"):
    try:
        # Get exchange rates from API
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        response.raise_for_status()  # Check for API errors
        
        data = response.json()
        rate = data['rates'][to_currency]
        converted_amount = amount * rate
        
        # Display result
        st.success(f"💰 {amount:,.2f} {from_currency} = {converted_amount:,.2f} {to_currency}")
        
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching exchange rates: {str(e)}")
    except KeyError:
        st.error("Currency conversion failed. Please try again.")