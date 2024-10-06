#!/usr/bin/env python
# coding: utf-8

# # Color Model & Image Manipulation 🌟

# In[ ]:


import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Global variables to store images
img = None
img_original = None

# Function to load an image
def load_image():
    global img, img_original
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    img = cv2.imread(file_path)
    img_original = img.copy()
    display_image(img)
    status_label.config(text="Image Loaded")

# Function to display an image in the GUI
# def display_image(img):
#     img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img_pil = Image.fromarray(img_rgb)
#     img_tk = ImageTk.PhotoImage(img_pil)
#     img_display.config(image=img_tk)
#     img_display.image = img_tk

def resize_image_with_aspect_ratio(image, target_width, target_height):
    original_height, original_width = image.shape[:2]
    aspect_ratio = original_width / original_height

    # Determine new width and height maintaining aspect ratio
    if original_width > original_height:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:
        new_height = target_height
        new_width = int(target_height * aspect_ratio)

    # Adjust if the new dimensions exceed target dimensions
    if new_width > target_width:
        new_width = target_width
        new_height = int(new_width / aspect_ratio)
    if new_height > target_height:
        new_height = target_height
        new_width = int(new_height * aspect_ratio)

    return cv2.resize(image, (new_width, new_height))

def display_image(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = resize_image_with_aspect_ratio(img_rgb, 600, 400)  
    img_pil = Image.fromarray(img_resized)
    img_tk = ImageTk.PhotoImage(img_pil)
    img_display.config(image=img_tk)
    img_display.image = img_tk
    
# Function to convert to grayscale
def convert_to_grayscale():
    global img
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # Convert back to BGR for consistent display
    display_image(img)
    status_label.config(text="Converted to Grayscale")

# Function to adjust brightness
def adjust_brightness(value):
    global img
    value = int(value)
    img = cv2.convertScaleAbs(img_original, alpha=1, beta=value)
    display_image(img)
    status_label.config(text=f"Brightness adjusted to {value}")

# Function to adjust contrast
def adjust_contrast(value):
    global img
    value = float(value)
    img = cv2.convertScaleAbs(img_original, alpha=value, beta=0)
    display_image(img)
    status_label.config(text=f"Contrast adjusted to {value}")

# Function to adjust saturation
def adjust_saturation(value):
    global img
    value = float(value)
    img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
    img_hsv[..., 1] = cv2.multiply(img_hsv[..., 1], value)
    img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    display_image(img)
    status_label.config(text=f"Saturation adjusted to {value}")

# Function to adjust hue
def adjust_hue(value):
    global img
    value = int(value)
    img_hsv = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV)
    img_hsv[..., 0] = (img_hsv[..., 0] + value) % 180
    img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    display_image(img)
    status_label.config(text=f"Hue adjusted to {value}")

# Function to convert RGB to CMYK
def convert_to_cmyk():
    global img
    img_rgb = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
    img_rgb_norm = img_rgb.astype(float) / 255
    K = 1 - np.max(img_rgb_norm, axis=2)
    C = (1 - img_rgb_norm[..., 0] - K) / (1 - K + 1e-10)
    M = (1 - img_rgb_norm[..., 1] - K) / (1 - K + 1e-10)
    Y = (1 - img_rgb_norm[..., 2] - K) / (1 - K + 1e-10)
    
    # Scale back to 0-255 range and convert to uint8
    C = (C * 255).astype(np.uint8)
    M = (M * 255).astype(np.uint8)
    Y = (Y * 255).astype(np.uint8)
    K = (K * 255).astype(np.uint8)
    
    # Create a pseudo-color image for visualization (CMY channels combined)
    pseudo_cmyk = cv2.merge([C, M, Y])

    # Display the combined pseudo-color image
    display_image(pseudo_cmyk)
    status_label.config(text="Converted to CMYK")

# Function to reset the image to the original
def reset_image():
    global img
    img = img_original.copy()
    display_image(img)
    status_label.config(text="Image Reset to Original")

# Function to save the current image
def save_image():
    global img
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    if not file_path:
        return
    cv2.imwrite(file_path, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    messagebox.showinfo("Save Image", "Image saved successfully!")
    status_label.config(text="Image Saved")

# Initialize the main window
root = Tk()
root.title("Advanced Image Manipulation Tool")
root.geometry("900x600")

# Create and place widgets
frame_controls = Frame(root, padx=10, pady=10, bg="lightgray")
frame_controls.pack(fill=BOTH, side=TOP)

frame_image = Frame(root, padx=10, pady=10, bg="white")
frame_image.pack(fill=BOTH, expand=True)

load_btn = Button(frame_controls, text="Load Image", command=load_image, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
load_btn.grid(row=0, column=0, padx=5, pady=5)

gray_btn = Button(frame_controls, text="Grayscale", command=convert_to_grayscale, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
gray_btn.grid(row=0, column=1, padx=5, pady=5)

cmyk_btn = Button(frame_controls, text="RGB to CMYK", command=convert_to_cmyk, bg="#FF5722", fg="white", font=("Arial", 10, "bold"))
cmyk_btn.grid(row=0, column=2, padx=5, pady=5)

reset_btn = Button(frame_controls, text="Reset Image", command=reset_image, bg="#FFC107", fg="black", font=("Arial", 10, "bold"))
reset_btn.grid(row=0, column=3, padx=5, pady=5)

save_btn = Button(frame_controls, text="Save Image", command=save_image, bg="#9C27B0", fg="white", font=("Arial", 10, "bold"))
save_btn.grid(row=0, column=4, padx=5, pady=5)

brightness_scale = Scale(frame_controls, from_=-100, to=100, label="Brightness", orient=HORIZONTAL, command=adjust_brightness, length=200)
brightness_scale.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

contrast_scale = Scale(frame_controls, from_=0.5, to=3.0, resolution=0.1, label="Contrast", orient=HORIZONTAL, command=adjust_contrast, length=200)
contrast_scale.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

saturation_scale = Scale(frame_controls, from_=0.0, to=2.0, resolution=0.1, label="Saturation", orient=HORIZONTAL, command=adjust_saturation, length=200)
saturation_scale.grid(row=1, column=4, columnspan=2, padx=5, pady=5)

hue_scale = Scale(frame_controls, from_=-180, to=180, label="Hue", orient=HORIZONTAL, command=adjust_hue, length=200)
hue_scale.grid(row=1, column=6, columnspan=2, padx=5, pady=5)

img_display = Label(frame_image)
img_display.pack(expand=True)

# Status Bar
status_label = Label(root, text="Welcome to the Image Manipulation Tool!", bd=1, relief=SUNKEN, anchor=W)
status_label.pack(side=BOTTOM, fill=X)

# Run the GUI loop
root.mainloop()


# In[ ]:




