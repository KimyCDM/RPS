"""
tp 5
Par Yul Kim
Groupe:405
roche papier sciseaux
"""
import arcade

from game_state import GameState
from attack_animation import AttackType, AttackAnimation
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, Papier, Sciseaux!"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.game_state = None
        self.winner = None
        self.player_image = None
        self.computer_image = None
        self.player_attack_type = None
        self.computer_attack_type = None
        self.list_computer_attack_type = ["Roche", "Papier", "Sciseaux"]
        self.player_victory = 0
        self.computer_victory = 0

        self.permanent_asset_list = arcade.SpriteList()
        self.center_y_image = 145

        self.rock = AttackAnimation(AttackType.ROCK)
        self.rock_computer = AttackAnimation(AttackType.ROCK)
        self.rock_list = arcade.SpriteList()
        self.rock_list_computer = arcade.SpriteList()
        self.rock_list.append(self.rock)
        self.rock_list_computer.append(self.rock_computer)

        self.paper = AttackAnimation(AttackType.PAPER)
        self.paper_computer = AttackAnimation(AttackType.PAPER)
        self.paper_list = arcade.SpriteList()
        self.paper_list_computer = arcade.SpriteList()
        self.paper_list.append(self.paper)
        self.paper_list_computer.append(self.paper_computer)

        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.scissors_computer = AttackAnimation(AttackType.SCISSORS)
        self.scissors_list = arcade.SpriteList()
        self.scissors_list_computer = arcade.SpriteList()
        self.scissors_list.append(self.scissors)
        self.scissors_list_computer.append(self.scissors_computer)

        self.game_state = GameState.NOT_STARTED
        self.player_image = arcade.Sprite("assets/faceBeard.png", 0.35, 220, 250)
        self.permanent_asset_list.append(self.player_image)
        self.computer_image = arcade.Sprite("assets/compy.png", 1.75, 600, 250)
        self.permanent_asset_list.append(self.computer_image)

        self.rock.center_x = 130
        self.rock.center_y = self.center_y_image
        self.rock_computer.center_x = 600
        self.rock_computer.center_y = self.center_y_image

        self.paper.center_x = 215
        self.paper.center_y = self.center_y_image
        self.paper_computer.center_x = 600
        self.paper_computer.center_y = self.center_y_image

        self.scissors.center_x = 290
        self.scissors.center_y = self.center_y_image
        self.scissors_computer.center_x = 600
        self.scissors_computer.center_y = self.center_y_image

    def setup(self):
        pass

    def winner_check(self):
        if self.player_attack_type == "Roche" and self.computer_attack_type == "Sciseaux":
            self.player_victory = self.player_victory + 1
            self.winner = "Player"
        elif self.player_attack_type == "Papier" and self.computer_attack_type == "Roche":
            self.player_victory = self.player_victory + 1
            self.winner = "Player"
        elif self.player_attack_type == "Sciseaux" and self.computer_attack_type == "Papier":
            self.player_victory = self.player_victory + 1
            self.winner = "Player"

        elif self.player_attack_type == "Sciseaux" and self.computer_attack_type == "Roche":
            self.computer_victory = self.computer_victory + 1
            self.winner = "Ordi"
        elif self.player_attack_type == "Roche" and self.computer_attack_type == "Papier":
            self.computer_victory = self.computer_victory + 1
            self.winner = "Ordi"
        elif self.player_attack_type == "Papier" and self.computer_attack_type == "Sciseaux":
            self.computer_victory = self.computer_victory + 1
            self.winner = "Ordi"

        elif self.player_attack_type == self.computer_attack_type:
            self.winner = "Nule"

        print(f"Vous {self.player_attack_type}")
        print(f"L'ordi {self.computer_attack_type}")
        self.game_state = GameState.ROUND_DONE

    def draw_deck(self):
        if self.game_state != GameState.ROUND_DONE:
            self.rock_list.draw()
            self.paper_list.draw()
            self.scissors_list.draw()
        elif self.game_state == GameState.ROUND_DONE:
            if self.player_attack_type == "Roche":
                self.rock_list.draw()
            elif self.player_attack_type == "Papier":
                self.paper_list.draw()
            elif self.player_attack_type == "Sciseaux":
                self.scissors_list.draw()

    def computer_deck(self):
        if self.game_state == GameState.ROUND_DONE:
            if self.computer_attack_type == "Roche":
                self.rock_list_computer.draw()
            elif self.computer_attack_type == "Papier":
                self.paper_list_computer.draw()
            elif self.computer_attack_type == "Sciseaux":
                self.scissors_list_computer.draw()

    def affichage_text(self):
        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text('Appuyer sur Espace pour commencer!', 150, 450, arcade.color.LIGHT_BLUE, 25)
        elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text('Appuyer sur une image pour faire une attaque!', 100, 450, arcade.color.LIGHT_BLUE, 25)
        elif self.game_state == GameState.ROUND_DONE and self.player_victory != 3 and self.computer_victory != 3:
            arcade.draw_text('Appuyer sur Espace pour commencer une nouvelle ronde!',
                             10, 400, arcade.color.LIGHT_BLUE, 25)
        if self.game_state == GameState.ROUND_DONE:
            if self.winner == "Player":
                arcade.draw_text('Vous avez gagné la ronde!', 220, 450, arcade.color.LIGHT_BLUE, 25)
            elif self.winner == "Ordi":
                arcade.draw_text("L'ordinateur a gagné la ronde! ", 220, 450, arcade.color.LIGHT_BLUE, 25)
            elif self.winner == "Nule":
                arcade.draw_text('Partie Nulle!', 300, 450, arcade.color.LIGHT_BLUE, 25)
            if self.player_victory == 3 or self.computer_victory == 3:
                arcade.draw_text('Appuyer sur Espace!', 250, 400, arcade.color.LIGHT_BLUE, 25)
        elif self.game_state == GameState.GAME_OVER:
            if self.player_victory == 3:
                arcade.draw_text('Vous avez gagné la partie!', 240, 450, arcade.color.LIGHT_BLUE, 25)
                arcade.draw_text('Appuyer sur Espace pour une nouvelle partie!', 120, 400, arcade.color.LIGHT_BLUE, 25)
            elif self.computer_victory == 3:
                arcade.draw_text("L'ordinateur a gagné la partie :(", 200, 450, arcade.color.LIGHT_BLUE, 25)
                arcade.draw_text('Appuyer sur Espace pour une nouvelle partie!', 120, 400, arcade.color.LIGHT_BLUE, 25)

    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.DAVY_GREY)
        arcade.draw_text('Roche, Papier, Ciseaux', 100, 500, arcade.color.RED_DEVIL, 50)
        arcade.draw_text(f'Le pointage du joueur est {self.player_victory}', 100, 80, arcade.color.LIGHT_BLUE, 15)
        arcade.draw_text(f"Le pointage de l'ordinateur est {self.computer_victory}", 450, 80, arcade.color.LIGHT_BLUE,
                         15)
        for i in [1, 2, 3]:
            arcade.draw_rect_outline(arcade.rect.XYWH(50 + i*80, 150, 60, 60), arcade.color.RED)
        arcade.draw_rect_outline(arcade.rect.XYWH(600, 150, 60, 60), arcade.color.RED)

        self.permanent_asset_list.draw()

        self.draw_deck()
        self.computer_deck()

        self.affichage_text()

    def on_update(self, delta_time):
        self.rock.on_update(delta_time)
        self.paper.on_update(delta_time)
        self.scissors.on_update(delta_time)
        self.rock_computer.on_update(delta_time)
        self.paper_computer.on_update(delta_time)
        self.scissors_computer.on_update(delta_time)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.game_state == GameState.NOT_STARTED:
            self.game_state = GameState.ROUND_ACTIVE
            self.computer_attack_type = random.choice(self.list_computer_attack_type)
        elif key == arcade.key.SPACE and self.game_state == GameState.ROUND_DONE:
            if self.computer_victory == 3 or self.player_victory == 3:
                self.game_state = GameState.GAME_OVER
            else:
                self.computer_attack_type = "None"
                self.player_attack_type = "None"
                self.game_state = GameState.ROUND_ACTIVE
                self.computer_attack_type = random.choice(self.list_computer_attack_type)
        elif key == arcade.key.SPACE and self.game_state == GameState.GAME_OVER:
            self.player_victory = 0
            self.computer_victory = 0
            self.game_state = GameState.NOT_STARTED

    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.rock.collides_with_point((x, y)) and self.game_state == GameState.ROUND_ACTIVE:
            self.player_attack_type = "Roche"
            self.winner_check()
        elif self.paper.collides_with_point((x, y)) and self.game_state == GameState.ROUND_ACTIVE:
            self.player_attack_type = "Papier"
            self.winner_check()
        elif self.scissors.collides_with_point((x, y)) and self.game_state == GameState.ROUND_ACTIVE:
            self.player_attack_type = "Sciseaux"
            self.winner_check()


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
