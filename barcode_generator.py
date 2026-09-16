from barcode import Code39
from barcode.writer import ImageWriter
from PIL import Image
import io

def generate_barcode(article_number):
    barcode = Code39(
        article_number,
        writer=ImageWriter(),
        add_checksum=False 
    )
    
    memory_file = io.BytesIO()
    
    options = {
        "write_text": False,
        # ====== GAP KO 0.8 SE 1.0 KAR DIYA HAI ======
        "module_width": 1.0,    
        # ============================================
        "module_height": 18.0,  
        "quiet_zone": 5.0,      
        "dpi": 300              
    }
    
    barcode.write(memory_file, options=options)
    memory_file.seek(0)
    
    img = Image.open(memory_file)
    return img