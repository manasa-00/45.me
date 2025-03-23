import cv2
import os
img = cv2.imread("sky.jpeg")
if img is None:
    print("Error: Image not found!")
    exit()
msg = input("Enter a secret message: ")
password = input("Enter a passcode: ")
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}
n, m, z = 0, 0, 0
msg_len = len(msg)
img[n, m, z] = msg_len
m += 1  
for char in msg:
    img[n, m, z] = d[char]
    m += 1
    if m >= img.shape[1]: 
        m = 0
        n += 1
        if n >= img.shape[0]: 
            print("Error: Message too long for the image!")
            exit()
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  
message = ""
n, m, z = 0, 0, 0
pas = input("Enter passcode for Decryption: ")
if password == pas:
    msg_len = img[n, m, z]
    m += 1  
    for _ in range(msg_len):
        message += c[img[n, m, z]]
        m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1
            if n >= img.shape[0]:  
                print("Error: Image does not contain a valid message!")
                exit()
    print("Decrypted message:", message)
else:
    print("You are not authenticated.")