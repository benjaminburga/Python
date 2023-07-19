import cv2

def load_classifier(classifier_path):
    try:
        cascade_faces = cv2.CascadeClassifier(classifier_path)
        return cascade_faces
    except Exception as e:
        print(f"Error loading the classifier: {e}")
        return None

def detect_faces(image, cascade_faces):
    if cascade_faces is None:
        return image, 0

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = cascade_faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return image, len(faces)  # Return the image with faces and the number of faces detected

def main():
    # Load the Haar Cascade classifier
    classifier_path = 'C:/Users/burga/OneDrive/Escritorio/PRACTICES/clasificador.xml'
    cascade_faces = load_classifier(classifier_path)

    if cascade_faces is None:
        return

    # Use the real-time camera feed
    capture = cv2.VideoCapture(0)

    while True:
        ret, image = capture.read()
        if not ret:
            break

        # Detect faces and get the number of people
        image_with_faces, num_faces = detect_faces(image, cascade_faces)

        # Display the number of people detected
        cv2.putText(image_with_faces, f"Number of people: {num_faces}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Display the image with faces and the number of people
        cv2.imshow('Facial Detector', image_with_faces)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
