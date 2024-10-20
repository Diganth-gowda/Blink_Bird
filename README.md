Blink Bird

Blink Bird is a unique twist on the popular Flappy Bird, where instead of pressing a keyboard key, players use computer vision to detect their blinks, which make the bird jump. It's an interactive and engaging experience, powered by Python and Unity.

Features
-Hands-free Gameplay: Control the bird by blinking!
-Uses MediaPipe for blink detection.
-Integrated with Unity for game mechanics.

Requirements
-Python version: 3.10.5
#Libraries:
*mediapipe
*pyautogui
*keyboard
*opencv-python
#Unity Game Engine: Ensure you have Unity installed to run the game.

Installation
Clone the repository:
Copy code
git clone https://github.com/Diganth-gowda/Blink_Bird.git

Navigate to the directory:
Copy code
cd Blink_Bird

Install the required Python libraries:
Copy code
pip install mediapipe pyautogui keyboard opencv-python

Open the batch file start.bat

#How It Works
-The game detects blinks using MediaPipe and OpenCV.
-PyAutoGUI sends a signal to make the bird jump upon detecting a blink.
-Unity handles the game logic and visual rendering.

#How to Play
-Start the game through Unity.
-Blink to make the bird jump and avoid obstacles.

#Troubleshooting
-Ensure your webcam is properly connected and accessible.
Check if all the Python libraries are installed correctly.
License
This project is open-source under the MIT License.

