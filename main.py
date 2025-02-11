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
SCREEN_TITLE = "RPS"


class MyGame(arcade.Window):
    """
    La classe principale de l'application

    NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """

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
        self.rock_list = arcade.SpriteList()
        self.rock_list.append(self.rock)

        self.paper = AttackAnimation(AttackType.PAPER)
        self.paper_list = arcade.SpriteList()
        self.paper_list.append(self.paper)

        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.scissors_list = arcade.SpriteList()
        self.scissors_list.append(self.scissors)

        self.game_state = GameState.NOT_STARTED
        self.player_image = arcade.Sprite("assets/faceBeard.png", 0.35, 220, 250)
        self.permanent_asset_list.append(self.player_image)
        self.computer_image = arcade.Sprite("assets/compy.png", 1.75, 600, 250)
        self.permanent_asset_list.append(self.computer_image)

    def setup(self):

        if self.computer_victory == 3 or self.player_victory == 3:
            self.game_state = GameState.GAME_OVER


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
        self.computer_attack_type = "None"
        self.player_attack_type = "None"
        self.game_state = GameState.ROUND_DONE
    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.DAVY_GREY)
        arcade.draw_text('Roche, Papier, Ciseaux', 100, 500, arcade.color.RED_DEVIL, 50)
        arcade.draw_text(f'Le pointage du joueur est {self.player_victory}', 100, 80, arcade.color.LIGHT_BLUE, 15)
        arcade.draw_text(f"Le pointage de l'ordinateur est {self.computer_victory}", 450, 80, arcade.color.LIGHT_BLUE, 15)
        for i in [1, 2, 3]:
            arcade.draw_rect_outline(arcade.rect.XYWH(50 + i*80, 150, 60, 60), arcade.color.RED)
        arcade.draw_rect_outline(arcade.rect.XYWH(600, 150, 60, 60), arcade.color.RED)

        self.permanent_asset_list.draw()

        self.rock.center_x = 130
        self.rock.center_y = self.center_y_image
        self.rock_list.draw()

        self.paper.center_x = 215
        self.paper.center_y = self.center_y_image
        self.paper_list.draw()

        self.scissors.center_x = 290
        self.scissors.center_y = self.center_y_image
        self.scissors_list.draw()

        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text('Appuyer sur Espace pour commencer!', 150, 450, arcade.color.LIGHT_BLUE, 25)
        elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text('Appuyer sur une image pour faire une attaque!', 100, 450, arcade.color.LIGHT_BLUE, 25)
        elif self.game_state == GameState.ROUND_DONE:
            arcade.draw_text('Appuyer sur Espace pour commencer une nouvelle ronde!',
                             10, 400, arcade.color.LIGHT_BLUE, 25)
            if self.winner == "Player":
                arcade.draw_text('Vous avez gagné la ronde!', 220, 450, arcade.color.LIGHT_BLUE, 25)
            elif self.winner == "Ordi":
                arcade.draw_text("L'ordinateur a gagné la ronde! ", 220, 450, arcade.color.LIGHT_BLUE, 25)
            elif self.winner == "Nule":
                arcade.draw_text('Partie Nulle!', 300, 450, arcade.color.LIGHT_BLUE, 25)




    def on_update(self, delta_time):
        """
        Toute la logique pour déplacer les objets de votre jeu et de
        simuler sa logique vont ici. Normalement, c'est ici que
        vous allez invoquer la méthode "update()" sur vos listes de sprites.
        Paramètre:
            - delta_time : le nombre de milliseconde depuis le dernier update.
        """
        self.rock.on_update(delta_time)
        self.paper.on_update(delta_time)
        self.scissors.on_update(delta_time)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE and self.game_state == GameState.NOT_STARTED:
            self.game_state = GameState.ROUND_ACTIVE
            self.computer_attack_type = random.choice(self.list_computer_attack_type)
        elif key == arcade.key.SPACE and self.game_state == GameState.ROUND_DONE:
            self.game_state = GameState.ROUND_ACTIVE
            self.computer_attack_type = random.choice(self.list_computer_attack_type)


    def on_key_release(self, key, key_modifiers):
        """
        Méthode invoquée à chaque fois que l'usager enlève son doigt d'une touche.
        Paramètres:
            - key: la touche relâchée
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

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




    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Méthode invoquée lorsque l'usager relâche le bouton cliqué de la souris.
        Paramètres:
            - x, y: coordonnées où le bouton a été relâché
            - button: le bouton de la souris relâché
            - key_modifiers: est-ce que l'usager appuie sur "shift" ou "ctrl" ?
        """
        pass


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
