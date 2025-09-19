import streamlit as st

# Dictionary mapping Tamil Nadu districts to their UNESCO heritage sites
unesco_sites = {
    "Chennai": [],
    "Coimbatore": [],
    "Madurai": [],
    "Thanjavur": ["Great Living Chola Temples (Brihadeeswarar Temple)"],
    "Tiruchirappalli": [],
    "Kanchipuram": [],
    "Dharmapuri": [],
    "Dindigul": [],
    "Erode": [],
    "Kanyakumari": [],
    "Karur": [],
    "Krishnagiri": [],
    "Namakkal": [],
    "Perambalur": [],
    "Pudukkottai": [],
    "Ramanathapuram": [],
    "Salem": [],
    "Sivaganga": [],
    "Theni": [],
    "Thoothukudi": [],
    "Tirunelveli": [],
    "Tirupattur": [],
    "Tiruppur": [],
    "Tiruvallur": [],
    "Tiruvannamalai": [],
    "Tiruvarur": [],
    "Vellore": [],
    "Viluppuram": [],
    "Virudhunagar": [],
    "Nagapattinam": ["Great Living Chola Temples (Gangaikonda Cholapuram Temple)"],
    "Ariyalur": ["Great Living Chola Temples (Airavatesvara Temple, Darasuram)"],
    "Mayiladuthurai": []
}

# Streamlit app
st.title("🏛️ UNESCO Heritage Sites in Tamil Nadu Districts")

# Dropdown to select district
selected_district = st.selectbox("Select a district:", list(unesco_sites.keys()))

# Display UNESCO sites
st.subheader(f"UNESCO Heritage Sites in {selected_district}:")
sites = unesco_sites[selected_district]
if sites:
    for site in sites:
        st.write(f"- {site}")
else:
    st.write("No UNESCO heritage sites listed for this district.")
