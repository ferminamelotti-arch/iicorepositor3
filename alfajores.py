import streamlit as st

PRECIO_ALFAJOR = 1500

st.title("Kiosco Carlos Paz")

cliente = st.text_input("Nombre del cliente")
cantidad = st.number_input("Cantidad de alfajores", min_value=0, step=1)

if cliente:
    st.write(f"Pedido de {cliente}")

total = cantidad * PRECIO_ALFAJOR
st.write(f"Total a pagar: ${total}")