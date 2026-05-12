import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Page configuration
st.set_page_config(page_title="QR Code Generator", page_icon="🎯")

st.title("🔗 Link to QR Code Generator")
st.write("Enter a URL below to generate a custom QR code.")

# User Input
url = st.text_input("Enter your link:", placeholder="https://example.com")

if url:
    try:
        # 1. Generate QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # 2. Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 3. Convert PIL image to bytes for Streamlit and Downloading
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # 4. Display the QR Code
        st.image(byte_im, caption="Your Generated QR Code", use_container_width=True)

        # 5. Download Button
        st.download_button(
            label="Download QR Code",
            data=byte_im,
            file_name="qrcode.png",
            mime="image/png"
        )
        
        st.success("✨ QR Code generated successfully!")

    except Exception as e:
        st.error(f"Ouch! Something went wrong: {e}")
else:
    st.info("Waiting for a link... 👆")
