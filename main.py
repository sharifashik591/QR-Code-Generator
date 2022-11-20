import pyautogui
import time
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

st.title('QR code generator')

# Colour picker
col1, col2 = st.columns(2)
with col1:
    b_color = st.color_picker('Pick Background Color', '#00f900')
    st.write('Background color code is', b_color)
with col2:
    f_color = st.color_picker('Pick fill Color', '#0e0e0e')
    st.write('The current color code is', f_color)

# input with streamlit
text_input = st.text_input("Enter URL 👇",)
st.write("You entered: ", text_input)

if text_input:
    # generate QR code
    qr.add_data(str(text_input))
    qr.make(fit=True)
    img = qr.make_image(back_color=b_color, fill_color=f_color)

    # Save image in custom directory
    img.save("QR img file/some_file.png")
    # show image
    image = Image.open('QR img file/some_file.png')
    col1, col2, col3 = st.columns(3)
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
        if btn:
            st.success('Download Complete!', icon="✅")
            # Sleep for 3 second
            time.sleep(3)
            # refresh the page
            pyautogui.press('f5')
        # st.success("Success")





