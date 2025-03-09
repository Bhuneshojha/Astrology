import streamlit as st
import requests

# Streamlit UI
st.title("🔮 Kundli (Birth Chart) Generator")
st.write("Enter your birth details to generate your Kundli.")

# User input fields
name = st.text_input("Your Name")
dob = st.date_input("Date of Birth")
birth_time = st.time_input("Time of Birth")
latitude = st.number_input("Latitude (e.g., 28.7041 for Delhi)", format="%.4f")
longitude = st.number_input("Longitude (e.g., 77.1025 for Delhi)", format="%.4f")

API_KEY = "YOUR_API_KEY"  # Replace with your API Key

if st.button("Generate Kundli"):
    if name and dob and birth_time and latitude and longitude:
        url = "https://api.example.com/kundli"
        params = {
            "date": dob.strftime("%Y-%m-%d"),
            "time": birth_time.strftime("%H:%M:%S"),
            "lat": latitude,
            "lon": longitude,
            "api_key": API_KEY
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            st.subheader(f"📝 Kundli for {name}")
            st.write(f"📅 Birth Date: {dob}, ⏰ Time: {birth_time}")
            st.write(f"📍 Location: {latitude}, {longitude}")

            st.subheader("📊 Planetary Positions:")
            for planet, details in data["planets"].items():
                st.write(f"**{planet}**: {details['position']}° in {details['rashi']}")

            st.success("✅ Kundli Generated Successfully!")
        else:
            st.error("⚠️ Error fetching data. Check your API key!")
    else:
        st.error("⚠️ Please enter all details!")
