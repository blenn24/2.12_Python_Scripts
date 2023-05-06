import cv2
from apriltag import apriltag

def find_apriltags():
    # Open the camera
    cap = cv2.VideoCapture(0)  # Change the argument to the appropriate camera index if needed

    # Create an AprilTag detector
    detector = apriltag("tagStandard41h12")  # Change the tag family according to your AprilTag setup

    while True:
        # Read frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame from camera.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect AprilTags in the frame
        result = detector.detect(gray)

        # Process the detection results
        if result:
            for detection in result:
                # Get the tag ID and corners
                tag_id = detection["id"]
                corners = detection["lb-rb-rt-lt"].astype(int)

                # Draw the tag ID and boundary
                cv2.putText(frame, str(tag_id), (corners[0][0], corners[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0), 2)
                cv2.polylines(frame, [corners], True, (0, 255, 0), 2)

        # Display the frame with AprilTags
        cv2.imshow("AprilTags", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to find and locate AprilTags from the camera
find_apriltags()
