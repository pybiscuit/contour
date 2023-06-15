from classes.contour_map import ContourMap
from classes.player import Player
from classes.app import App

if __name__ == '__main__':

    app = App(
        map_list = ContourMap,
        player = Player,
        )
    app.run()