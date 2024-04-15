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
        "Requesting Terminal Number", 
        "Statement Currency", 
        "Currency Period",  
        "Class or Category"
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
            line[49:52]
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