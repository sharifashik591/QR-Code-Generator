
import streamlit as st
from PIL import Image
import qrcode
from function import handle_upsert
# Setupr QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2)

# input with streamlit
text_input = st.text_input("Enter URL 👇",)
st.write("You entered: ", text_input)
col1, col2, col3 = st.columns(3)

if text_input:
    # generate QR code
    qr.add_data(str(text_input))
    qr.make(fit=True)
    img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))

    # Save image in custom directory
    img.save("QR img file/some_file.png")
    # show image
    image = Image.open('QR img file/some_file.png')

    with col2:
        st.image(image, caption='QR Code')

# download img
if text_input:
    with open("QR img file/some_file.png", "rb") as file:
        with col2:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name='QR img file/some_file.png',
                mime="image/png",
                on_click=handle_upsert(),
            )






