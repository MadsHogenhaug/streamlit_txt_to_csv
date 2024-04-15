import streamlit as st
import pandas as pd

def process_txt_to_csv(txt_file):
    data = txt_file.read().decode("utf-8")  # Read uploaded file
    lines = data.splitlines()

column_names = [
    "Identifier", 
    "Allocating RU", 
    "RU Receiving the Statement", 
    "Year", 
    "Month", 
    "Period Within Month",
    "Reserved",
    "Type of Service", 
    "Type of Transaction",  
    "Distribution Channel", 
    "Travel Organization Code", 
    "Requesting Terminal RU to Which It Belongs",  
    "Requesting Terminal number", 
    "Statement Currency", 
    "Currency Period",  
    "Class or Category",
    "Unit Price",
    "Train number",
    "Coach number",
    "Day of travel",
    "Depature location (RU)",
    "Depature location (Station)",
    "In reserve",
    "Destination location (RU)",
    "Destination location (Station)",
    "In reserve 2 (PH)",
    "Reference number",
    "Dialogue number",
    "Issue date",
    "Number of services",
    "Adjustment",
    "Gross amount to be debited",
    "Gross amount to be credited",
    "Service-providing RU",
    "Recovery state",
    "Tariff code",
    "Type of journey",
    "Primary route code 1st section",
    "Passenger category",
    "Amount/unit share",
    "Gross amount to be debited 2 (PH)",
    "Gross amount to be credited 2 (PH)",
    "Percentage commission rate of service- providing RU",
    "Amount of commission to be debited to the service-providing RU",
    "Amount of commission to be credited to the service-providing RU",
    "Country code",
    "Train category"
] 

data_list = []

for line in lines[1:-1]:
    data_list.append([
        line[0:9], 
        line[9:13], 
        line[13:17], 
        line[17:19], 
        line[19:21], 
        line[21:23],
        line[23],
        line[24:26], 
        line[26],
        line[27], 
        line[28:33], 
        line[33:37],
        line[37:44], 
        line[44:47], 
        line[47:49],
        line[49:52],
        line[52-60],
        line[60:65],
        line[65:68],
        line[68:74],
        line[74:78],
        line[78:83],
        line[83],
        line[84:88],
        line[88:93],
        line[93],
        line[94:108],
        line[108:113],
        line[113:119],
        line[119:124],
        line[124],
        line[125:135],
        line[135:145],
        line[145:149],
        line[149:151],
        line[151:156],
        line[156],
        line[157:166],
        line[166:168],
        line[168:176],
        line[176:185],
        line[186:196],
        line[196:200],
        line[200:210],
        line[210:220],
        line[220:225],
        line[225:229]
    ])

    df = pd.DataFrame(data_list, columns=column_names)
        return df

def main():
    st.title("TXT to CSV Converter")

    # File uploader
    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

    if uploaded_file is not None:
        st.write("File uploaded successfully!")

        # Process file
        df = process_txt_to_csv(uploaded_file)

        # Display processed dataframe
        st.write(df)

        # Download button for CSV file
        st.download_button(
            label="Download CSV",
            data=df.to_csv().encode(),
            file_name="output.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
