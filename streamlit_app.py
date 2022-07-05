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

streamlit.dataframe(my_fruit_list.loc(Fruit_selected))
