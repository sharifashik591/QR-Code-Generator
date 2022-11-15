
import streamlit as st

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4)

text_input = st.text_input("Enter URL 👇",)

if text_input:
    st.write("You entered: ", text_input)

qr.add_data(str(text_input))
qr.make(fit=True)
img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
img.save("some_file.png")

