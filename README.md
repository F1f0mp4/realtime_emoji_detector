# Real-Time Emoji Detector

A Python application that uses computer vision to detect facial expressions and body poses in real-time, displaying corresponding emojis based on the detected state (smiling, straight face, or hands up). The project leverages MediaPipe for pose and face landmark detection and OpenCV for webcam capture and image processing.

## Features
- **Real-Time Detection**: Detects smiles and raised hands using a webcam feed.
- **Emoji Display**: Shows appropriate emojis (`smile.jpg`, `plain.png`, `air.jpg`) in a separate window based on detected gestures or expressions.
- **Landmark Visualization**: Includes a secondary script (`Landmarks Tracking.py`) to visualize pose, face, and hand landmarks.
- **User-Friendly Interface**: Displays camera feed and emoji output side by side with on-screen instructions.

## Prerequisites
- Python 3.8 or higher
- Webcam connected to your device
- Emoji image files (`smile.jpg`, `plain.png`, `air.jpg`) in the project directory

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/realtime_emoji_detector.git
   cd realtime_emoji_detector
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the following emoji images are in the project root directory:
   - `smile.jpg` (smiling face emoji)
   - `plain.png` (straight face emoji)
   - `air.jpg` (hands up emoji)

   If these files are missing, the program will exit with an error message indicating the required files.

## Usage
1. Run the main emoji detector script:
   ```bash
   python realtime_emoji_detector.py
   ```

2. The application will open two windows:
   - **Camera Feed**: Shows the webcam feed with the detected state (e.g., SMILING, STRAIGHT_FACE, HANDS_UP) and instructions.
   - **Emoji Output**: Displays the corresponding emoji based on the detected state.

3. Controls:
   - **Smile**: Displays the smiling emoji (`😊`).
   - **Straight Face**: Displays the straight face emoji (`😐`).
   - **Raise Hands**: Raise hands above shoulders to display the hands-up emoji (`🙌`).
   - **Quit**: Press `q` to exit the application.

4. To visualize landmarks (pose, face, hands), run the landmark tracking script:
   ```bash
   python "Landmarks Tracking.py"
   ```

   - **Toggle Landmarks**: Press `l` to turn landmark visualization on/off.
   - **Quit**: Press `q` to exit.

## Project Structure
- `realtime_emoji_detector.py`: Main script for real-time emoji detection.
- `Landmarks Tracking.py`: Script for visualizing pose, face, and hand landmarks.
- `requirements.txt`: List of required Python packages.
- `requirements-lock.txt`: Exact versions of installed packages for reproducibility.
- `smile.jpg`, `plain.png`, `air.jpg`: Emoji images (must be provided by the user).

## Requirements
See `requirements.txt` for the list of dependencies. Key packages include:
- `opencv-python>=4.8.0`
- `mediapipe>=0.10.13`
- `numpy>=1.24.0`
- `Pillow>=10.0.0`

For exact versions, refer to `requirements-lock.txt`.

## Notes
- The `SMILE_THRESHOLD` in `realtime_emoji_detector.py` can be adjusted to fine-tune smile detection sensitivity.
- Ensure your webcam is not being used by another application.
- The application is optimized for a display resolution of approximately 720x450 pixels, suitable for most laptop screens.
- The landmark tracking script (`Landmarks Tracking.py`) is a separate utility to help debug or visualize MediaPipe landmarks.

## Troubleshooting
- **Webcam not working**: Ensure your webcam is connected and not in use by other applications.
- **Emoji images not found**: Verify that `smile.jpg`, `plain.png`, and `air.jpg` are in the project directory.
- **Dependency issues**: Use `requirements-lock.txt` for exact package versions or ensure compatibility with your Python version.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details (if applicable).

## Acknowledgments
- Built with [MediaPipe](https://google.github.io/mediapipe/) for pose and face detection.
- Uses [OpenCV](https://opencv.org/) for webcam handling and image processing.
