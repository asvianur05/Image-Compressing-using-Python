import PIL
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

file_path = askopenfilename()

if file_path: 
    img = Image.open(file_path)
    myWidth, myHeight = img.size

    newWidth, newHeight = myWidth // 10, myHeight // 10
    img = img.resize((newWidth, newHeight), Image.LANCZOS)

    save_path = asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])

    if save_path:  
        img.save(save_path + "_compressed.jpg", quality=85)
