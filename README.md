
# YOLOV_PLANE_DETECTION_BOT

## Overview

YOLOV_PLANE_DETECTION_BOT is an object detection bot based on YOLO (You Only Look Once) architecture. The bot is designed to detect airplanes in images and sort them into different directories based on the detection results. Additionally, it generates corresponding label files for each detected airplane, providing object coordinates and other relevant information.

## Prerequisites

Before using this code, ensure that you have the following prerequisites installed/downloaded on your system:

1. **Python**: Make sure you have Python installed on your machine.

2. **OpenCV**: Install the OpenCV library for image processing. You can install it using pip:
   ```
   pip install opencv-python
   ```

3. **YOLOv4 Configuration and Weights**: The YOLOv4 model configuration file and weights file are essential for object detection. You can download them from the official YOLO website or other reputable sources.

4. **COCO Labels**: The bot uses COCO labels to identify objects. Ensure the 'coco.names' file is present in the repository, containing the class names.

## Usage

1. **Clone the Repository**: Clone this GitHub repository to your local machine.

2. **Directory Setup**: Organize your image files in the 'images' directory. Create the following empty directories to facilitate sorting:
   - 'labels': The bot will store the label files here.
   - 'images2': Detected airplanes will be moved to this directory.
   - 'replaced': Images without airplanes will be moved here.
   - 'must_be_delete': Problematic or damaged images will be moved to this directory.

3. **Configurations**: Set the 'modelConfiguration' and 'modelWeights' variables in the Python script ('plane_detection_bot.py') to point to the location of your YOLOv4 configuration and weights files.

4. **Execution**: Run the Python script 'plane_detection_bot.py':
   ```
   python plane_detection_bot.py
   ```

5. **Output**: The bot will process the images, detect airplanes, and move them to the 'images2' directory along with their label files. Images without airplanes will be moved to the 'replaced' directory, and problematic images will be moved to the 'must_be_delete' directory.

6. **Customization**: If you want to detect objects other than airplanes, modify the 'classNames' list in the script with the appropriate class names.

7. **Backup**: It is recommended to keep backup copies of your images before running the script to prevent accidental data loss.

8. **Handling Problematic Images**: Check the 'must_be_delete' directory for problematic images and decide how to proceed with them manually.

9. **Stopping the Script**: The script will continue processing images until all images in the 'images' directory have been processed. You can stop it manually if needed.

## Important Notes

- Please ensure that you have all necessary permissions and rights to use the YOLOv4 model, COCO labels, and any other resources used in this project.

- The script has been set up to detect airplanes by default. To detect different objects, you can modify the 'classNames' list accordingly.

- Be cautious when running the script, especially if you're processing a large number of images. Review the sorting results and make necessary adjustments if needed.

- Any feedback or contributions to improve this project are welcomed.
