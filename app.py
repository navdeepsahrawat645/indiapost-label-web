import streamlit as st
import os
from PIL import Image
from barcode_generator import generate_barcode
from label_generator import create_label

# Website ki setting
st.set_page_config(page_title="IndiaPost Barcode Generator", page_icon="📮", layout="centered")

st.title("📮 IndiaPost Barcode Generator")
st.markdown("**Version 2.0 (Web) | © Navdeep Singh SA D Dn**")
st.divider()

# Input Type Selection
input_type = st.radio("Select Number Type:", ("Article Number", "Bag Number"), horizontal=True)

# Text Box
data = st.text_input("Enter 13-Character Number:", max_chars=13).strip().upper()

# Generate Button
if st.button("Generate & Download PDF", type="primary"):
    if len(data) != 13:
        st.error("⚠️ Please enter exactly 13 characters.")
    else:
        # Backend logic setup
        actual_mode = "portrait_half" if input_type == "Article Number" else "bag_small"
        
        with st.spinner("Generating official label..."):
            try:
                # Same old backend functions!
                barcode_img = generate_barcode(data)
                img, pdf_path, layout_mode = create_label(barcode_img, data, actual_mode)
                
                st.success("✅ Label Generated Successfully!")
                
                # PDF Download Button
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="⬇️ Download Label (PDF)",
                        data=pdf_file,
                        file_name=f"{data}_Label.pdf",
                        mime="application/pdf"
                    )
                
                # Image Preview (Fixed container width attribute)
                st.markdown("### Label Preview")
                st.image(img, use_container_width=True)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
                