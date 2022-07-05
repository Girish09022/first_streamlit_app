import streamlit

streamlit.title('My ParentsNew Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🍞 Omega 3 & Blueberry Oatmeal')

streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')

streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Without setting index
#streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))

#Setting Index as Fruit Name
my_fruit_list = my_fruit_list.set_index('Fruit')

#Setting Fruits Name in Multi-select list (with Defualt value)
Fruit_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado'])

streamlit.dataframe(my_fruit_list.loc[Fruit_selected])

import requests

streamlit.header("Fruityvice Fruit Advice!")



fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
