import client
import OpenCV

color = client.client_socket()
print(color)

print("Enter image directory: (Like Assets\hands.jpg)")
img_location = input()
OpenCV.color_highlight(img_location, color)
