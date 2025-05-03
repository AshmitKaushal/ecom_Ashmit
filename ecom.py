import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mat


def main():
    st.title('This is the app for the excel file')
    st.sidebar.title('You can upload the file from here')
    upload_file = st.sidebar.file_uploader("Upload your file",type=['csv','xlsx'])
    if upload_file is not None:
        try:
            if upload_file.name.endswith('.csv'):
                data = pd.read_csv(upload_file)
            else:
                data = pd.read_excel(upload_file)
            st.sidebar.success('File is uploaded successfully')

            st.subheader('I am going to show you data details')
            st.dataframe(data.head())

            st.subheader('Let see some more details')
            st.write("The shape of the data is",data.shape)
            st.write("The columns inside the data is",data.columns)
            st.write("The missing values inide the data is",data.isnull().sum())

            st.subheader("Let see the some Statistical Data")
            st.write(data.describe())
        except Exception as e:
            print(e)
        else:
            print("The file is not upload")
    
if __name__=="__main__":
    main()
