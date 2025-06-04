def auto_capture_photo(img_path="visa_photo.jpg"):
    import cv2
    import base64

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open camera")
    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise Exception("Failed to capture image")
    cv2.imwrite(img_path, frame)
    
    with open(img_path, "rb") as f:
        photo_b64 = base64.b64encode(f.read()).decode()
    return img_path, photo_b64