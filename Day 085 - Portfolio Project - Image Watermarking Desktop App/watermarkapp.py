import os
from tkinter import Label, Button, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WatermarkApp:
    def __init__(self, root):
        self.root = root

        # Format the window
        self.root.title("Watermark App")  # Set the title of the window
        self.root.minsize(width=500, height=300)  # Set the size of the window

        # Variables
        self.image_path = ""

        # GUI Elements
        self.label = Label(root, text="Select an option:")
        self.label.pack()

        self.upload_button = Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()

        self.watermark_button = Button(root, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack()

    def upload_image(self):
        # Open a file dialog to prompt the user to select an image file (supports PNG, JPG, JPEG, and GIF)
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        # Display the uploaded image
        if self.image_path:  # If the image path is not empty
            image = Image.open(self.image_path)  # Open the selected image using PIL (Python Imaging Library)
            image.thumbnail((300, 300))   # Resize the image
            photo = ImageTk.PhotoImage(image)   # Convert the PIL Image to a PhotoImage object for displaying in Tkinter

            # Check if the attribute 'image_label' already exists in the current object
            # The image_label attribute is an instance variable of the WatermarkApp class that represents a Tkinter
            # Label widget used for displaying an image in the graphical user interface (GUI).
            if hasattr(self, 'image_label'):
                self.image_label.configure(image=photo)  # Update its configuration with the new PhotoImage
                self.image_label.image = photo  # Update the 'image' attribute to prevent it from being garbage collected
            else:  # If 'image_label' doesn't exist
                self.image_label = Label(self.root, image=photo)  # create a new Label widget with the PhotoImage
                self.image_label.pack()  # Pack the Label widget into the Tkinter window
                self.image_label.image = photo   # Set the 'image' attribute of the 'image_label' to the new PhotoImage

    def add_watermark(self):
        # Check if the image_path is empty (no image has been selected/uploaded)
        if not self.image_path:
            return # Exit the function

        # Open the original image
        original_image = Image.open(self.image_path)

        # Create a drawing object
        draw = ImageDraw.Draw(original_image)

        # Set watermark text and font
        watermark_text = "Maialen's image"
        font = ImageFont.load_default()  # Load the default font

        # Text sizes
        text_width = draw.textlength(watermark_text, font=font)  # Width
        left, top, right, bottom = font.getmask(watermark_text).getbbox()
        text_height = bottom - top  # Height

        # Image sizes
        image_width, image_height = original_image.size

        # Calculate position for the watermark
        x = image_width - text_width - 10
        y = image_height - text_height - 10

        # Add the watermark to the image
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

        # Save the new image with watermark in the same path as the original image
        output_path = os.path.splitext(self.image_path)[0] + "_watermarked" + os.path.splitext(self.image_path)[1]
        original_image.save(output_path)

        # Display the watermarked image
        watermarked_image = Image.open(output_path)
        watermarked_image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(watermarked_image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
