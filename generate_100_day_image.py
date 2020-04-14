import cv2
import os

x_and_y = (470, 340)
font_color = (255, 255, 255)
font_scale = 2
font = cv2.FONT_HERSHEY_SIMPLEX
output_folder = './'

date = input("Enter the date to be added ") # Get Date to be added from user
im = cv2.imread('data/100_days_image_template.jpeg', 1)

cv2.putText(im, 'Day {}'.format(date), x_and_y,
            font, font_scale, font_color, 2)
cv2.imwrite(output_folder+date+".jpeg", im)
