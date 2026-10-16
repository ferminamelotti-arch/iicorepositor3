import streamlit as st
preciosAlfajor=1000
st.title("Kiosco Cristo obrero 4c")
cliente = st.text_input("ingrese el nombre del cliente:   ")
cantidad = st.number_input("Cantidad de alfajores",

min_value=0, step=1)
total= cantidad*preciosAlfajor
st.write(f"gracias {cliente} su total es: {total}   $")
