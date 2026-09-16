import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

OUTPUT_FOLDER = "Generated_Labels"

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def create_label(barcode_img, article, layout_mode="portrait_half"):
    
    if layout_mode == "bag_small":
        LABEL_WIDTH, LABEL_HEIGHT = 960, 560
        label = Image.new("RGB", (LABEL_WIDTH, LABEL_HEIGHT), "white")
        
        bc_width, bc_height = 420, 100
        bc_resized = barcode_img.resize((bc_width, bc_height), Image.Resampling.NEAREST)
        
        x_bc = LABEL_WIDTH - bc_width - 40
        y_bc = 90
        label.paste(bc_resized, (x_bc, y_bc))
        
        draw = ImageDraw.Draw(label)
        try:
            font = ImageFont.truetype("arialbd.ttf", 35)
        except IOError:
            font = ImageFont.load_default()
            
        bbox = draw.textbbox((0, 0), article, font=font)
        text_width = bbox[2] - bbox[0]
        x_text = x_bc + (bc_width - text_width) // 2
        y_text = y_bc + bc_height + 15
        draw.text((x_text, y_text), article, fill="black", font=font)

    else:
        # SMALL MODE (DEFAULT ARTICLE): 70x120 mm Label
        LABEL_WIDTH, LABEL_HEIGHT = 826, 1417
        label = Image.new("RGB", (LABEL_WIDTH, LABEL_HEIGHT), "white")
        
        # ====== BARCODE SIZE (ORIGINAL JAISA WIDE AUR STRIP TYPE) ======
        bc_width, bc_height = 720, 180
        # ===============================================================
        bc_resized = barcode_img.resize((bc_width, bc_height), Image.Resampling.NEAREST)
        x_bc = (LABEL_WIDTH - bc_width) // 2
        y_bc = 180 
        label.paste(bc_resized, (x_bc, y_bc))
        
        draw = ImageDraw.Draw(label)
        try:
            # ====== ARIAL BOLD AUR CHHOTA SIZE (IMAGE KI TARAH) ======
            font = ImageFont.truetype("arialbd.ttf", 50)
        except IOError:
            font = ImageFont.load_default()
            
        bbox = draw.textbbox((0, 0), article, font=font)
        text_width = bbox[2] - bbox[0]
        x_text = (LABEL_WIDTH - text_width) // 2
        
        # Text ko barcode ke thoda aur paas kiya hai
        y_text = y_bc + bc_height + 25 
        draw.text((x_text, y_text), article, fill="black", font=font)
        
        # Sabse Neeche QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=1)
        qr.add_data(article)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        
        qr_img = qr_img.resize((450, 450), Image.Resampling.NEAREST)
        x_qr = (LABEL_WIDTH - 450) // 2
        y_qr = y_text + 300 
        
        label.paste(qr_img, (x_qr, y_qr))

    pdf_filename = os.path.join(OUTPUT_FOLDER, f"{article}.pdf")
    label.save(pdf_filename, "PDF", resolution=300.0)

    return label, pdf_filename, layout_mode