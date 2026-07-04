import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


with st.sidebar:
    num_toss = st.slider('num_toss',min_value = 1,max_value = 10000000,
              step = 1,value=500)
x = np.random.randint(1,7,size = num_toss)
y = np.random.randint(1,7,size = num_toss)

num_toss_array = np.arange(1,num_toss + 1)

sum_6 = np.cumsum((x+y) == 6)

prob_sum_6 = sum_6 / num_toss_array

fig,ax = plt.subplots()
plt.plot(num_toss_array,prob_sum_6)

ax.set_xscale('log')
plt.xlabel('Number of tosses')
plt.ylabel('Probability')

ax.grid(linestyle = '--',linewidth = .25,color = '0.5')

st.pyplot(fig)