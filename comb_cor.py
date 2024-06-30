from PIL import Image
import numpy as np

def combine_colors(image1_path, image2_path, output_path):
    
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    
        if image1.size != image2.size:
        raise ValueError("As imagens devem ter o mesmo tamanho.")
        
    image1_array = np.array(image1)
    image2_array = np.array(image2)
        
    combined_array = (image1_array.astype(np.float32) + image2_array.astype(np.float32)) / 2
    combined_array = combined_array.astype(np.uint8)
        
    combined_image = Image.fromarray(combined_array)
        
    combined_image.save(output_path)

    print(f"Imagem combinada salva em {output_path}")
