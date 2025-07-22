ESP32 Camera Web Server
This project uses the ESP32 microcontroller along with a camera module to build a web server that captures and streams images. The system is designed to capture images from the camera and send them over an HTTP server to be viewed on a web browser. Additionally, it supports LED control for enhanced lighting when taking photos or streaming.

Features
Camera Capture: Capture images from an ESP32 camera module (support for multiple models).

MJPEG Streaming: Provides continuous video stream over HTTP.

Snapshot Feature: Take snapshots from the camera and serve them in various formats (JPEG, BMP).

LED Control: Optional control for an LED to illuminate the scene during low-light conditions.

Web Interface: Access the camera stream and snapshots through a simple web interface.

Hardware Requirements
ESP32 or ESP32-S3 with a camera module (e.g., ESP32-CAM).

Micro-USB cable for powering the ESP32.

Optional LED for illumination during low-light conditions (controlled via GPIO pin).

Software Requirements
Arduino IDE with the ESP32 board installed.

ESP32 Camera library (esp_camera.h).

ESP32 HTTP Server library (esp_http_server.h).

FPDF library for generating flashcards (Python script included).

Installation
Step 1: Set Up Development Environment
Install the Arduino IDE if you haven't already.

Install the ESP32 board package via Arduino’s Board Manager:

Go to File > Preferences and add the following URL in the “Additional Boards Manager URLs” field:
https://dl.espressif.com/dl/package_esp32_index.json

Open Tools > Board > Boards Manager, search for esp32, and install it.

Install the required libraries:

ESP32 Camera library (esp_camera.h).

ESP32 HTTP Server library (esp_http_server.h).

FPDF (used for generating flashcards in Python).

Step 2: Clone the Repository
Clone the project to your local machine:

bash
Copy
git clone https://github.com/your-username/ESP32-Camera-WebServer.git
cd ESP32-Camera-WebServer
Step 3: Upload the Code to the ESP32
Open the CameraWebServer.ino file in Arduino IDE.

Select the ESP32 board that corresponds to your hardware:

Tools > Board > ESP32 Dev Module (or the specific ESP32 model you're using).

Select the correct COM port under Tools > Port.

Click Upload to upload the code to the ESP32.

Step 4: Configure GPIO Settings for Your Camera
In camera_pins.h, ensure the GPIO settings match your camera module’s wiring. Different models have different pin configurations, such as:

cpp
Copy
#if defined(CAMERA_MODEL_WROVER_KIT)
    #define XCLK_GPIO_NUM 21
    #define SIOD_GPIO_NUM 26
    #define SIOC_GPIO_NUM 27
    // Define other pins here...
#endif
You can find the correct pin mappings for your specific ESP32 camera module in the file.

Step 5: Access the Web Server
Once the ESP32 is running, the serial monitor will display the IP address of the ESP32. Open a browser and enter the IP address to access the camera stream.

Example: http://192.168.x.x

Stream: /stream

Capture Image: /capture

Get BMP Image: /bmp

Usage
Live Streaming: You can access the camera’s live feed through a browser by navigating to the /stream endpoint.

Image Capture: Use /capture to capture an image and receive it in JPEG format.

BMP Image: Access the /bmp endpoint for a BMP-formatted image capture.

LED Control
The system supports an optional LED for illumination. If enabled, it will light up when the camera is capturing images or streaming.

You can control the LED from app_httpd.cpp by modifying the following section:

cpp
Copy
#if CONFIG_LED_ILLUMINATOR_ENABLED
#define LED_LEDC_GPIO 22
#define CONFIG_LED_MAX_INTENSITY 255
Flashcard Generation (Optional)
You can also use the Python script (py.py) to generate a set of flashcards for computer engineering terminology:

Ensure you have Python installed along with the fpdf library:

bash
Copy
pip install fpdf
Run the script:

bash
Copy
python py.py
This will generate a PDF of flashcards in the Computer_Engineering_Flashcards_Day5.pdf format.

Customization
GPIO Pins: Modify the GPIO pins in camera_pins.h based on the camera module you're using.

LED Intensity: You can adjust the LED intensity and behavior by modifying LED_LEDC_GPIO and the duty cycle in app_httpd.cpp.

HTML Interface: Customize the camera feed display in index_ov2640.html.gz for a more personalized web interface.
