Digital Inline Holographic Microscopy (DIHM)
===========================================

Here we want to present an easy to use digital inline holographic microscope employing 3D printed parts, a Raspberry Pi and Pi Cam, as well as a high-power LED and a 15 micron pinhole. For details see (link to publication following).

# Assembly

1. Print the required parts (.stl files) with a 3D printer or a 3D-printing service of your choice. We used PLA as printer material. 
2. Using pliers, remove the lens in front of the Raspberry Pi Cam v2. Assemble the Raspberry Pi 3 and the Raspberry Pi Cam.  
3. Fix the pinhole on the upper side of the pinhole holder. We used black tape to prevent residual light from passing. 
4. Connect the LED to a current source providing a current of 125 mA. Run the cables through the hole in the lower box. Fix the LED on the lower side of the pinhole holder.
5. Assemble lower box, pinhole holder and upper box. Connect the Raspberry Pi Cam to the upper box. Connect a monitor, mouse and power source to the Raspberry Pi. Power it on.

# Image Acquisition

1. Open Camera_DIHM.py and insert the experimental parameters. If you run the file, a folder with the name YY.MM.DD_hh.mm will be created and all following files will be saved here. 
ATTENTION: Run Camera_DIHM.py only once every minute, or the previous files will be overwritten!
2. If you control the LED with the Raspberry Pi's GPIO, it will now be turned on. If not, turn on the LED. 
3. Insert an object on a standard microscope slide. You will now see its hologram in the preview.
4. By pressing ENTER an image of the object is captured. If you want to capture a higher number of images, you can enter the number in range(N).
5. Remove the object slide. By pressing ENTER again, N in range(N) background images are captured.

# Reconstruction

1. Move the images to a PC with Fiji and the following plugin installed https://unal-optodigital.github.io/NumericalPropagation/
2. Open Fiji and the plugin.
3. Open the object image and choose Image>Type>32-Bit to convert it to a greyscale image.
4. In the Plugin choose the image as real image. Let imaginary image empty. Enter the required parameters.
5. Press propagate. After that, you can reconstruct several image planes at once by using Batch. To increase the reconstructed image's contrast you can use Process>Enhance Contrast with (0.2, normalize, prozess whole stack).
