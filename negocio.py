
import streamlit as st
from fpdf import FPDF
import os

PRECIO_ALFAJOR = 1500
PRECIO_GASEOSA = 2800

st.set_page_config(page_title="Kiosco KCO4")

if os.path.exists("logo.png"):
    st.image("logo.png", width=180)

st.title("Kiosco KCO4")
st.write("Sistema de ventas")

cliente = st.text_input("Nombre del cliente")

st.subheader("Productos")

cant_alf = st.number_input(
    "Alfajores - $1500 c/u",
    min_value=0,
    step=1
)

cant_gas = st.number_input(
    "Gaseosas - $2800 c/u",
    min_value=0,
    step=1
)

sub_alf = cant_alf * PRECIO_ALFAJOR
sub_gas = cant_gas * PRECIO_GASEOSA
total = sub_alf + sub_gas

st.subheader("Resumen")

st.write(f"Alfajores: ${sub_alf}")
st.write(f"Gaseosas: ${sub_gas}")

st.markdown(f"### Total: ${total}")


def generar_pdf():
    pdf = FPDF()
    pdf.add_page()

    if os.path.exists("logo.png"):
        pdf.image("logo.png", x=80, y=10, w=50)
        pdf.set_y(65)
    else:
        pdf.set_y(15)

    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Kiosco KCO4", new_x="LMARGIN",
             new_y="NEXT", align="C")

    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "Comprobante de compra",
             new_x="LMARGIN", new_y="NEXT", align="C")

    pdf.ln(8)

    nombre = cliente.strip() if cliente.strip() else "Consumidor Final"

    pdf.cell(0, 8, f"Cliente: {nombre}",
             new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)
    pdf.set_font("Helvetica", "", 11)

    if cant_alf > 0:
        pdf.cell(0, 8, f"{cant_alf} alfajor(es): ${sub_alf}",
                 new_x="LMARGIN", new_y="NEXT")

    if cant_gas > 0:
        pdf.cell(0, 8, f"{cant_gas} gaseosa(s): ${sub_gas}",
                 new_x="LMARGIN", new_y="NEXT")

    pdf.ln(5)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, f"TOTAL: ${total}",
             new_x="LMARGIN", new_y="NEXT")

    return bytes(pdf.output())


if total > 0:
    st.download_button(
        label="Descargar PDF",
        data=generar_pdf(),
        file_name="comprobante_kco4.pdf",
        mime="application/pdf"
    )
else:
    st.button("Descargar PDF", disabled=True)
