# Created by: Khoa Le
# Created on November 13 2017
# Created for ICS3U
# This program picks 10 random numbers and calculates average.

import ui

def calculate_button_touch_up_inside(sender):
    # When user presses the button, picks 10 random and calculates average.
    from numpy import random
    random_number = []
    average_number = 0
    for count in range(11):
        random_number.append(random.randint(10,100))
    view['random_number_label'].text = str(random_number)
    for sum in random_number:
        average_number = average_number + sum
    average_number = average_number / 10
    view['average_number_label'].text = str(average_number)

view = ui.load_view()
view.present('sheet')
