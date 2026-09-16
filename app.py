import streamlit as st
import os
import re
from PIL import Image
from barcode_generator import generate_barcode
from label_generator import create_label

st.set_page_config(page_title="IndiaPost Barcode Generator", page_icon="📮", layout="centered")

st.title("📮 IndiaPost Barcode Generator")
st.markdown("**Version 2.0 (Web) | © Navdeep Singh SA D Dn**")
st.divider()

# Input Type Selection outside form
input_type = st.radio("Select Number Type:", ("Article Number", "Bag Number"), horizontal=True)

# Form to enable Enter key submission
with st.form("barcode_form"):
    data = st.text_input("Enter 13-Character Number (e.g., AY847874894IN):", max_chars=13).strip().upper()
    submitted = st.form_submit_button("Generate & Download PDF", type="primary")

if submitted:
    if len(data) != 13:
        st.error("⚠️ Error: Number must be exactly 13 characters long.")
    else:
        # Condition Check: First 2 letters, middle 9 digits, last 2 letters (for Article Number format)
        pattern = r"^[A-Z]{2}\d{9}[A-Z]{2}$"
        
        if input_type == "Article Number" and not re.match(pattern, data):
            st.error("⚠️ Invalid Format! Article number must start with 2 letters, followed by 9 digits, and end with 2 letters (e.g., AY847874894IN).")
        else:
            actual_mode = "portrait_half" if input_type == "Article Number" else "bag_small"
            
            with st.spinner("Generating official label..."):
                try:
                    barcode_img = generate_barcode(data)
                    img, pdf_path, layout_mode = create_label(barcode_img, data, actual_mode)
                    
                    st.success("✅ Label Generated Successfully!")
                    
                    with open(pdf_path, "rb") as pdf_file:
                        st.download_button(
                            label="⬇️ Download Label (PDF)",
                            data=pdf_file,
                            file_name=f"{data}_Label.pdf",
                            mime="application/pdf"
                        )
                    
                    st.markdown("### Label Preview")
                    st.image(img, use_container_width=True)
                    
                except Exception as e:
                    st.error(f"An error occurred: {e}")