# Color-Model-Image-Manipulation
The Advanced Image Manipulation Tool is a user-friendly application designed to provide quick and easy image adjustments such as brightness, contrast, saturation, hue, grayscale conversion, and RGB to CMYK transformation. Built using OpenCV, Tkinter, and NumPy, this tool offers real-time feedback and simple controls for users to manipulate 

## **Features**

- **Load Image**: Load and display any image from your local storage.
- **Grayscale Conversion**: Convert images to grayscale instantly.
- **RGB to CMYK Conversion**: Transform the image’s color space from RGB to pseudo-CMYK.
- **Brightness Adjustment**: Easily adjust the brightness of the image.
- **Contrast Adjustment**: Modify contrast levels for sharper or softer visuals.
- **Saturation & Hue**: Fine-tune color saturation and hue to create vibrant or muted effects.
- **Reset Image**: Revert the image to its original state with a single click.
- **Save Image**: Save the edited image in PNG or JPEG format.

---

## **Technologies Used**

- **Python**: The core programming language used for logic and functionality.
- **OpenCV**: Image processing and manipulation library.
- **Tkinter**: Provides the graphical user interface (GUI) components.
- **NumPy**: Used for efficient numerical calculations.
- **Pillow (PIL)**: For image handling and displaying within Tkinter.

---

## **Installation**

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/image-manipulation-tool.git
   ```
2. Install the required dependencies:
   ```bash
   pip install opencv-python numpy pillow
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## **How to Use**

1. **Load Image**: Click the "Load Image" button to select an image from your device.
2. **Edit Image**: Use the provided sliders and buttons to adjust brightness, contrast, saturation, hue, or convert the image to grayscale or CMYK.
3. **Reset Image**: Revert to the original image anytime by clicking "Reset Image."
4. **Save Image**: After making changes, save the edited image by clicking the "Save Image" button.


## **Future Scope**

- Add advanced filters like blur and sharpen.
- Implement undo/redo functionality for non-linear editing.
- Introduce layer support for non-destructive edits.
- Enable batch processing to handle multiple images at once.
- Integrate AI-based enhancements for automatic editing.
- Expand support for additional color spaces like Lab and YUV.

---

## **Contributing**

Contributions are welcome! Feel free to submit pull requests or report issues. Please ensure any pull requests pass existing tests and are aligned with the project’s objectives.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**

- Thanks to **OpenCV** and **Tkinter** for providing powerful libraries to build this application.
- Special thanks to the Python community for their valuable tutorials and resources.
