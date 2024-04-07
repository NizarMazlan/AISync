import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Page 1", page_icon="1️⃣")

st.markdown("# Page 1")
st.write("This is the first page to get information about a specific meter")
st.sidebar.header("Page 1")
st.sidebar.write("Description of what Page 1 is about")

# Connect to the database
conn = sqlite3.connect('air-selangor-hackathon.db')

# Query Getting Specific Meter Information
serial_input = st.text_input('Serial Number', '')

if serial_input:
    # Query data from meter info table
    ais_meter_info = conn.execute(f'''
                    SELECT meter_info.*, location.location_name
                    FROM meter_info
                    INNER JOIN location ON meter_info.location_id = location.location_id
                    WHERE meter_info.serial_num = ?''', (serial_input,))
    
    # Query data from meter movement table
    ais_meter_movement = conn.execute(f'''
                    SELECT 
                        move.movement_id,
                        L1.location_name AS move_from_full_name,
                        L2.location_name AS move_to_full_name,
                        move.serial_num,
                        move.purpose,
                        move.timestamp           
                    FROM meter_movement move
                    JOIN location L1 ON move.move_from = L1.location_id
                    JOIN location L2 ON move.move_to = L2.location_id
                    WHERE move.serial_num = ?''', (serial_input,))

    specific_meter_info = ais_meter_info.fetchall()
    specific_meter_movement = ais_meter_movement.fetchall()

    if specific_meter_info:
        df_specific_meter_info = pd.DataFrame(specific_meter_info)
        df_specific_meter_movement = pd.DataFrame(specific_meter_movement)

        # Display meter information
        st.markdown("### Meter Information")
        #st.dataframe(df_specific_meter_info)
        # Just an example to see how is the data
        st.write("Serial Number:", df_specific_meter_info.at[0, 0])
        st.write("Location:", df_specific_meter_info.at[0, 8])
        st.write("Meter Type:", df_specific_meter_info.at[0, 2])
        st.write("Manufacturer:", df_specific_meter_info.at[0, 3])
        st.write("Model:", df_specific_meter_info.at[0, 4])
        st.write("Manufactured Year:", df_specific_meter_info.at[0, 5])
        st.write("Meter Size:", df_specific_meter_info.at[0, 6])
        st.write("Warranty Info:", df_specific_meter_info.at[0, 7])

        # Display meter movements
        st.markdown("### Meter Movements")
        st.dataframe(df_specific_meter_movement)
    else:
        st.error("Meter information not found. Please check the serial number.")
