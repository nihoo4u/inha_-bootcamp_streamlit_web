import streamlit as st
import pandas as pd
st.write('#괄호')
view=[100,150,30]
view
st.write('## barcart')
st.bar_chart(view)
sview= pd.Series(view)
st.write('## gogo')
data=pd.DataFrame({'index':['A','B','C'],
                   'values':[10,20,30]})
st.write('## chart2')
st.bar_chart(data,x='index',y='values',use_container_width=True)
