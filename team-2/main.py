import client
import OpenCV

color = client.client_socket()
print("The Choosen color was ",color)

print("Press Esc to quit...")
OpenCV.img_process(color)

