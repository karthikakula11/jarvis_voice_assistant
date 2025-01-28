import cv2
import os  # Import the os module to work with file directories

# Create the "samples" directory if it doesn't exist
if not os.path.exists("samples"):
    os.makedirs("samples")

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #create a video capture object which is helpful to capture videos through webcam
cam.set(3, 640) # set video FrameWidth
cam.set(4, 480) # set video FrameHeight


detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Haar Cascade classifier is an effective object detection approach

face_id = input("Enter a Numeric user ID  here:  ")
#Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)

count=int(input("enter number of samples to be taken: "))
print("Taking samples, look at camera ....... ")
num=0



while True:

    ret, img = cam.read() #read the frames using the above created object
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #The function converts an input image from one color space to another
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) #used to draw a rectangle on any image
        num += 1

        
        cv2.imwrite("samples/face." + str(face_id) + '.' + str(num) + ".jpg", converted_image[y:y+h,x:x+w])
        # To capture & Save images into the datasets folder

        cv2.imshow('image', img) #Used to display an image in a window

    k = cv2.waitKey(100) & 0xff # Waits for a pressed key

    if k == ord("q") or k == ord("Q"):  # press q to close camera
        break
    elif num == count: # Take 50 sample (More sample --> More accuracy)
         break

print("Samples taken now closing the program....")
cam.release()
cv2.destroyAllWindows()