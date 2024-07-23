# Watermark App

## Goal
The Watermark App is a desktop application with a Graphical User Interface (GUI) developed using Tkinter, enabling users to upload an image and automatically add a watermark or text using Python. This eliminates the need for manual image editing software and streamlines the process of adding watermarks to multiple images.

**Use Case:** For instance, users who want to share photos on social media platforms like Instagram can use this application to automatically add their website URL or logo to each image, enhancing brand visibility.

**Similar Online Service:** [Watermarkly](https://watermarkly.com/)

## Prerequisites
Install the required libraries:
- [Pillow](https://pypi.org/project/Pillow/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

## Implementation
The GUI is designed using Tkinter, the standard GUI toolkit for Python. The interface includes buttons for uploading an image and adding a watermark. It also features a label to display the uploaded and watermarked images.

### Image Processing
Pillow (PIL) is used for image processing tasks. The **Image** module is employed to open, resize, and manipulate the images, while the **ImageDraw** module is used for adding text watermarks.

### Code Structure
The code is organized into a class-based structure. The **WatermarkApp** class encapsulates the Tkinter application. Methods within the class handle image uploads, watermarking, and GUI interactions.

### File Handling
The application utilizes the **filedialog** module from Tkinter to prompt users for image selection. Watermarked images are saved in the same directory as the original images with the filename appended with "_watermarked".

## How to Use
1. Run the program.
2. Click on the "Upload Image" button to select an image.
3. Click on the "Add Watermark" button to add a watermark (text) to the image.
4. The watermarked image will be displayed, and a new watermarked image file will be saved in the same directory as the original image.

## Reflection Time
I started by designing a simple Tkinter-based GUI to facilitate image uploads and watermarking. Utilizing the Pillow library, I incorporated image processing functionalities to handle image uploads, resize images, and add watermarks.

The initial challenge involved integrating Tkinter and Pillow for a seamless user experience. Understanding the coordination between Tkinter widgets and Pillow image processing functions was crucial.

### Today's learnings
- Gained familiarity with Tkinter for GUI development.
- Learned to use Pillow for image processing tasks.
- Improved understanding of handling file dialogs and managing image assets.

### Potential improvements for the future
- Enhance the user interface for a more user-friendly experience.
- Implement error handling for cases like invalid image formats or failed watermarking.
- Explore additional features, such as options for logo watermarks and customizable text placements.
- Allow users to customize watermark properties like color, transparency, and size.
