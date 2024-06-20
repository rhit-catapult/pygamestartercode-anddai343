import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    # TODO 4: Return the actual distance between point 1 and point 2.
    #  Hint: you will need the math library for the sqrt function.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)
    # TODO 8: Load the "drums.wav" file into the pygame music mixer
    pygame.mixer.music.load("drums.wav")
    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)
    msg = ""
    circle_color = (154, 58, 212)
    circle_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle_radius = 50
    circle_border_width = 3
    play = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                dist_circ = distance(pygame.mouse.get_pos(), circle_center)
                if dist_circ > circle_radius:
                    msg = "misfire"
                    pygame.mixer.music.stop()
                else:
                    msg = "bullseye"
                    pygame.mixer.music.play(-1)
            # TODO 2: For a MOUSEBUTTONDOWN event get the click position.
                # TODO 3: Determine the distance between the click position and the circle_center using the distance
                # TODO 3:   function and save the result into a variable called distance_from_circle
                # TODO 5: If distance_from_circle is less than or equal to circle_radius, set message_text to 'Bullseye!'
                # TODO 5: If distance_from_circle is greater than the circle_radius, set the message_text to 'You missed!'
                # TODO 9: Start playing the music mixer looping forever if the click is within the circle
                # TODO 10: Stop playing the music if the click is outside the circle

        screen.fill(pygame.Color("Black"))
        pygame.draw.circle(screen, "blue", circle_center, circle_radius, circle_border_width)
        # TODO 1: Draw the circle using the screen, circle_color, circle_center, circle_radius, and circle_border_width
        # TODO 6: Create a text image (render the text) based on the message_text with the color (122, 237, 201)
        cap = font.render(msg, True, (122, 237, 200))
        screen.blit(instructions_image, (25, 25))
        # TODO 7: Draw (blit) the message to the user that says 'Bullseye!' or 'You missed!'
        screen.blit(cap, (300, 25))
        pygame.display.update()


main()
