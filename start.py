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


# # Main panel
# st.title("Weather Data Analysis")

# if selected_columns:
#     st.write(f"## Plotting columns: {', '.join(selected_columns)}")

#     for column in selected_columns:
#         st.write(f"### {column}")
#         plt.figure(figsize=(10, 4))
#         plt.plot(df['시간'], df[column])
#         plt.xlabel('Time')
#         plt.ylabel(column)
#         plt.title(f"{column} over Time")
#         st.pyplot(plt)
# else:
#     st.write("Please select at least one column to plot from the sidebar.")

# if __name__ == '__main__':
#     st.run()

# import sys
# import matplotlib

# print("Python executable:", sys.executable)
# print("Matplotlib version:", matplotlib.__version__)

import streamlit as st
import matplotlib.pyplot as plt

xdata = [1, 2, 3, 4]
ydata = [10, 5, 20, 35]

fig, ax = plt.subplots()
ax.plot(xdata, ydata)
st.pyplot(fig)


