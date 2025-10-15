import cv2
import mediapipe as mp

# --- SETUP ---
mp_pose = mp.solutions.pose
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# --- CONFIGURATION ---
SHOW_LANDMARKS = 1  # 0 = off, 1 = on
WINDOW_WIDTH, WINDOW_HEIGHT = 720, 450

# --- CAMERA INIT ---
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Error: Could not open webcam.")
    exit()

cv2.namedWindow('Camera Feed', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Camera Feed', WINDOW_WIDTH, WINDOW_HEIGHT)
cv2.moveWindow('Camera Feed', 100, 100)

print("🎥 Starting landmark tracking...")
print("📋 Controls:")
print("   - Press 'L' to toggle landmarks on/off")
print("   - Press 'Q' to quit")

# --- MEDIAPIPE MODELS ---
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose, \
     mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.5) as face_mesh, \
     mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("⚠️ Ignoring empty frame.")
            continue

        # Mirror the frame
        frame = cv2.flip(frame, 1)
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False

        # --- PROCESSING ---
        results_pose = pose.process(image_rgb)
        results_face = face_mesh.process(image_rgb)
        results_hands = hands.process(image_rgb)

        # --- VISUALIZATION ---
        camera_frame = cv2.resize(frame, (WINDOW_WIDTH, WINDOW_HEIGHT))

        if SHOW_LANDMARKS == 1:
            # Pose
            if results_pose.pose_landmarks:
                mp_drawing.draw_landmarks(
                    camera_frame,
                    results_pose.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
                )

            # Face
            if results_face.multi_face_landmarks:
                for face_landmarks in results_face.multi_face_landmarks:
                    mp_drawing.draw_landmarks(
                        camera_frame,
                        face_landmarks,
                        mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style()
                    )

            # Hands
            if results_hands.multi_hand_landmarks:
                for hand_landmarks in results_hands.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        camera_frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles.get_default_hand_landmarks_style(),
                        connection_drawing_spec=mp_drawing_styles.get_default_hand_connections_style()
                    )

        # --- HUD ---
        cv2.putText(camera_frame, f'Landmarks: {"ON" if SHOW_LANDMARKS else "OFF"}',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(camera_frame, 'Press L to toggle, Q to quit',
                    (10, WINDOW_HEIGHT - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)

        # Show the frame
        cv2.imshow('Camera Feed', camera_frame)

        # --- KEY CONTROLS ---
        key = cv2.waitKey(5) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('l'):
            SHOW_LANDMARKS = 1 - SHOW_LANDMARKS  # toggle

# --- CLEANUP ---
print("👋 Exiting...")
cap.release()
cv2.destroyAllWindows()
print("✅ Done.")
