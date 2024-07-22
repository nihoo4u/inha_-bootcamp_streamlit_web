# import streamlit as st
# import pandas as pd
# from streamlit_folium import st_folium
# import folium

# st.write('#괄호')
# view=[100,150,30]
# view
# st.write('## barcart')
# st.bar_chart(view)
# sview= pd.Series(view)
# st.write('## gogo')
# data=pd.DataFrame({'index':['A','B','C'],
#                    'values':[10,20,30]})
# st.write('## chart2!!')
# st.bar_chart(data,x='index',y='values',use_container_width=True)
# # m=folium.Map(location=[37.42637222,126.9898],zoom_start=16)
# # folium.Marker([37.42637222,126.9898],
# #               popup='junyeon',
# #               tooltip='junyeon').add_to(m)
# # st_data=st_folium(m,width=725)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = 'weather_real대전.csv'
df = pd.read_csv(file_path)

# Convert '시간' column to datetime format
df['시간'] = pd.to_datetime(df['시간'])

# Sidebar for user input
st.sidebar.title("Weather Data Visualization")
selected_columns = st.sidebar.multiselect('Select columns to plot', df.columns, default=['기온', '강수량', '풍속', '습도'])

# Main panel
st.title("Weather Data Analysis")

if selected_columns:
    st.write(f"## Plotting columns: {', '.join(selected_columns)}")

    for column in selected_columns:
        st.write(f"### {column}")
        plt.figure(figsize=(10, 4))
        plt.plot(df['시간'], df[column])
        plt.xlabel('Time')
        plt.ylabel(column)
        plt.title(f"{column} over Time")
        st.pyplot(plt)
else:
    st.write("Please select at least one column to plot from the sidebar.")

if __name__ == '__main__':
    st.run()
