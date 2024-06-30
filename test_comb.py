import unittest
from color_comparator.color_combiner import combine_colors
from PIL import Image
import numpy as np
import os

class TestColorCombiner(unittest.TestCase):
    def setUp(self):
        self.image1_path = "tests/test_image1.png"
        self.image2_path = "tests/test_image2.png"
        self.output_path = "tests/test_output.png"
        
       
        image1 = Image.new('RGB', (100, 100), color = 'red')
        image2 = Image.new('RGB', (100, 100), color = 'blue')
        image1.save(self.image1_path)
        image2.save(self.image2_path)
    
    def test_combine_colors(self):
        combine_colors(self.image1_path, self.image2_path, self.output_path)
                
        self.assertTrue(os.path.exists(self.output_path))
              
        output_image = Image.open(self.output_path)
        output_array = np.array(output_image)
        expected_color = np.array([127, 0, 127])  # Média de vermelho e azul
        
        self.assertTrue(np.all(output_array == expected_color))
    
    def tearDown(self):
        
        os.remove(self.image1_path)
        os.remove(self.image2_path)
        os.remove(self.output_path)

if __name__ == '__main__':
    unittest.main()
