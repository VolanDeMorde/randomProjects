import pygame
import sys
import random
from enum import IntEnum

# Initialize Pygame
pygame.init()

# Constants
FPS = 30
BUTTON_COUNT = 5
BUTTON_WIDTH = 130
BUTTON_HEIGHT = 40
BUTTON_Y = 300
HOVER_OFFSET = 5  # Offset for hover effect

# Define Actions
class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

# Define winning conditions
victories = {
    Action.Rock: [Action.Scissors, Action.Lizard],
    Action.Paper: [Action.Rock, Action.Spock],
    Action.Scissors: [Action.Paper, Action.Lizard],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}

# Setup the screen
def create_screen(width, height):
    return pygame.display.set_mode((width, height))

def display_message(message, x, y, color=(255, 255, 255)):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)

def play(user_action):
    computer_action = Action(random.randint(0, len(Action) - 1))
    defeats = victories[user_action]

    if user_action == computer_action:
        return "tie", f"Both players selected {user_action.name}. It's a tie!"
    elif computer_action in defeats:
        return "win", f"{user_action.name} beats {computer_action.name}! You win!"
    else:
        return "lose", f"{computer_action.name} beats {user_action.name}! You lose."

def main():
    global screen, font
    screen_width, screen_height = 800, 600
    screen = create_screen(screen_width, screen_height)
    pygame.display.set_caption("Rock Paper Scissors Lizard Spock")
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 48)  # Larger font for the title
    clock = pygame.time.Clock()
    
    running = True
    result_message = ""
    result_type = ""
    
    # Initialize scores
    wins = 0
    losses = 0
    ties = 0

    # Create buttons with their corresponding actions
    buttons = []
    actions = [Action.Rock, Action.Paper, Action.Scissors, Action.Lizard, Action.Spock]
    
    for i, action in enumerate(actions):
        x_pos = (screen_width - BUTTON_COUNT * BUTTON_WIDTH) // 2 + i * (BUTTON_WIDTH + 10)
        buttons.append({'action': action, 'rect': pygame.Rect(x_pos, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)})

    while running:
        screen.fill((0, 0, 0))  # Clear the screen

        # Display title
        title_message = "Rock Paper Scissors Lizard Spock"
        display_message(title_message, screen_width // 2, 100)  # Position it near the top

        display_message("Select an action:", screen_width // 2, 200)

        # Draw buttons
        for button in buttons:
            # Check for mouse hover
            mouse_pos = pygame.mouse.get_pos()
            if button['rect'].collidepoint(mouse_pos):
                # Draw button rectangle with hover effect
                hover_rect = pygame.Rect(button['rect'].x, button['rect'].y - HOVER_OFFSET, button['rect'].width, button['rect'].height)
                pygame.draw.rect(screen, (200, 200, 200), hover_rect)  # Lighter gray for hover
            else:
                # Draw button rectangle without hover effect
                pygame.draw.rect(screen, (255, 255, 255), button['rect'])  # White for normal state

            # Render button text
            text = font.render(button['action'].name, True, (0, 0, 0))  # Use the action name for the button
            if button['rect'].collidepoint(mouse_pos):
                # Adjust text position for hover effect
                text_rect = text.get_rect(center=(button['rect'].centerx, button['rect'].centery - HOVER_OFFSET))
            else:
                text_rect = text.get_rect(center=button['rect'].center)  # Center text in the button
            screen.blit(text, text_rect)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button['rect'].collidepoint(event.pos):
                        result_type, result_message = play(button['action'])
                        if result_type == "win":
                            wins += 1
                        elif result_type == "lose":
                            losses += 1
                        else:
                            ties += 1

        # Display result message with color
        if result_message:
            if result_type == "win":
                display_message(result_message, screen_width // 2, 400, (0, 255, 0))  # Green for win
            elif result_type == "lose":
                display_message(result_message, screen_width // 2, 400, (255, 0, 0))  # Red for lose
            else:
                display_message(result_message, screen_width // 2, 400, (173, 216, 230))  # light blue for tie

        # Display scores
        score_message = f"Wins: {wins} | Losses: {losses} | Ties: {ties}"
        display_message(score_message, screen_width // 2, 450)  # Display scores below the result message

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Control the frame rate

if __name__ == "__main__":
    main()