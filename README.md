# 📸 ESP32 Camera Web Server

<div align="center">

![ESP32](https://img.shields.io/badge/ESP32-000000?style=for-the-badge&logo=espressif&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

*Transform your ESP32 into a powerful camera web server with live streaming capabilities*

[🚀 Quick Start](#-quick-start) • [📋 Features](#-features) • [🔧 Installation](#-installation) • [📖 Usage](#-usage) • [⚙️ Customization](#️-customization)

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 📷 **Camera Operations**
- 📸 High-quality image capture
- 🎥 Real-time MJPEG streaming
- 📷 Instant snapshot functionality
- 🖼️ Multiple format support (JPEG, BMP)

</td>
<td width="50%">

### 🌐 **Web Interface**
- 🖥️ Clean, responsive web UI
- 📱 Mobile-friendly design
- ⚡ Real-time streaming view
- 🎛️ Easy camera controls

</td>
</tr>
<tr>
<td width="50%">

### 💡 **Smart Features**
- 🔆 LED illumination control
- 🌙 Low-light enhancement
- ⚙️ GPIO customization
- 📊 Multiple camera model support

</td>
<td width="50%">

### 🔧 **Developer Tools**
- 📚 Flashcard generation (Python)
- 🛠️ Modular architecture
- 📖 Comprehensive documentation
- 🔌 Easy hardware integration

</td>
</tr>
</table>

---

## 🛠️ Hardware Requirements

| Component | Description | Status |
|-----------|-------------|---------|
| **ESP32/ESP32-S3** | Main microcontroller with camera module | ✅ Required |
| **Camera Module** | ESP32-CAM or compatible | ✅ Required |
| **Micro-USB Cable** | For power and programming | ✅ Required |
| **LED** | Optional illumination (GPIO controlled) | 🔸 Optional |

### 📋 Supported Camera Models
- 📹 ESP32-CAM
- 📹 WROVER-KIT Camera
- 📹 AI-Thinker ESP32-CAM
- 📹 Custom GPIO configurations

---

## 💻 Software Requirements

```bash
# Required Software Stack
Arduino IDE          # Main development environment
ESP32 Board Package  # ESP32 support for Arduino
ESP32 Camera Library # Camera functionality
HTTP Server Library  # Web server capabilities
Python + FPDF       # For flashcard generation (optional)
```

---

## 🚀 Quick Start

### 1️⃣ **Development Environment Setup**

**Install Arduino IDE:**
- Download from [arduino.cc](https://www.arduino.cc/en/software)

**Add ESP32 Board Support:**
1. Go to `File` → `Preferences`
2. Add this URL to "Additional Boards Manager URLs":
   ```
   https://dl.espressif.com/dl/package_esp32_index.json
   ```
3. Open `Tools` → `Board` → `Boards Manager`
4. Search for "esp32" and install

### 2️⃣ **Clone & Setup**

```bash
# Clone the repository
git clone https://github.com/your-username/ESP32-Camera-WebServer.git
cd ESP32-Camera-WebServer
```

### 3️⃣ **Upload to ESP32**

1. Open `CameraWebServer.ino` in Arduino IDE
2. Select your board: `Tools` → `Board` → `ESP32 Dev Module`
3. Select the correct port: `Tools` → `Port`
4. Click **Upload** 🚀

### 4️⃣ **Configure GPIO Settings**

Edit `camera_pins.h` to match your camera module:

```cpp
#if defined(CAMERA_MODEL_WROVER_KIT)
    #define XCLK_GPIO_NUM 21
    #define SIOD_GPIO_NUM 26
    #define SIOC_GPIO_NUM 27
    // Define other pins here...
#endif
```

---

## 🌐 Usage

Once your ESP32 is running, check the **Serial Monitor** for the IP address:

### 📡 **Endpoints**

| Endpoint | Function | Example |
|----------|----------|---------|
| `/` | 🏠 Main interface | `http://192.168.1.100/` |
| `/stream` | 🎥 Live video stream | `http://192.168.1.100/stream` |
| `/capture` | 📸 Capture JPEG image | `http://192.168.1.100/capture` |
| `/bmp` | 🖼️ Capture BMP image | `http://192.168.1.100/bmp` |

### 💡 **LED Control**

The system includes smart LED illumination:

```cpp
#if CONFIG_LED_ILLUMINATOR_ENABLED
#define LED_LEDC_GPIO 22
#define CONFIG_LED_MAX_INTENSITY 255
```

- ✅ Automatic low-light detection
- ⚙️ Adjustable intensity
- 🔧 GPIO customization

---

## 📚 Flashcard Generation (Bonus Feature)

Generate computer engineering flashcards with the included Python script:

```bash
# Install dependencies
pip install fpdf

# Generate flashcards
python py.py
```

**Output:** `Computer_Engineering_Flashcards_Day5.pdf`

---

## ⚙️ Customization

### 🔧 **GPIO Configuration**
- **File:** `camera_pins.h`
- **Purpose:** Match your specific camera module wiring

### 💡 **LED Settings**
- **File:** `app_httpd.cpp`
- **Options:** Intensity, behavior, GPIO pin

### 🎨 **Web Interface**
- **File:** `index_ov2640.html.gz`
- **Customize:** Layout, styling, functionality

---

## 🏗️ Project Structure

```
ESP32-Camera-WebServer/
├── 📄 CameraWebServer.ino    # Main Arduino sketch
├── 📄 camera_pins.h          # GPIO pin definitions
├── 📄 app_httpd.cpp          # HTTP server implementation
├── 📄 index_ov2640.html.gz   # Web interface
├── 📄 py.py                  # Flashcard generator
└── 📄 README.md              # This beautiful documentation
```

---

## 🎯 Getting Help

<div align="center">

### 🤝 **Community & Support**

[![GitHub Issues](https://img.shields.io/badge/Issues-GitHub-red?style=for-the-badge&logo=github)](https://github.com/Masih-Roughani/ESP32-Camera-WebServer/issues)
[![Discussions](https://img.shields.io/badge/Discussions-GitHub-blue?style=for-the-badge&logo=github)](https://github.com/Masih-Roughani/ESP32-Camera-WebServer/discussions)

**Found a bug?** Open an issue  
**Have a question?** Start a discussion  
**Want to contribute?** Submit a pull request

</div>

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">

**⭐ If this project helped you, please give it a star! ⭐**

Made with ❤️ for the maker community

</div>
