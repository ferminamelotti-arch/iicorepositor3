import streamlit as st

PRECIO_ALFAJOR = 1500
PRECIO_GASEOSA = 2800

def calcular_total(cantidad, precio):
    return cantidad * precio

st.title("Kiosco Carlos Paz")

cliente = st.text_input("Nombre del cliente")
cant_alfajores = st.number_input("Cantidad de alfajores", min_value=0, step=1)
cant_gaseosas = st.number_input("Cantidad de gaseosas", min_value=0, step=1)

subtotal_alfajores = calcular_total(cant_alfajores, PRECIO_ALFAJOR)
subtotal_gaseosas = calcular_total(cant_gaseosas, PRECIO_GASEOSA)
total = subtotal_alfajores + subtotal_gaseosas

if cliente:
    st.write(f"Pedido de {cliente}")

st.write(f"Subtotal alfajores: ${subtotal_alfajores}")
st.write(f"Subtotal gaseosas: ${subtotal_gaseosas}")
st.write(f"**TOTAL A PAGAR: ${total}**")