import pygame
import player
import os
import json
import tile

current_path = os.path.dirname(__file__)

pygame.init()
PLAYER = (500, 220)

scr = pygame.display.set_mode((640,320))
pygame.display.set_caption("Survivals")

font = pygame.font.Font(current_path + "\\assets\\fonts\\main.ttf", 16)

# drawmap
blitmap = open(current_path + "\\assets\\configs\\maps\\map1.json", "r")
mapd = json.load(blitmap)
blitmap.close()

all_sprites = pygame.sprite.Group()
player = player.Player(PLAYER)
map_tiles = pygame.sprite.Group()

clock = pygame.time.Clock()

all_sprites.add(player)

for i in mapd["value"]:
    tiletype = i.get("p", "place")
    if tiletype == "place":
        g_dynamic_map_tile = tile.Tile(i["n"], i["v"])
        map_tiles.add(g_dynamic_map_tile)
        all_sprites.add(g_dynamic_map_tile)
    elif tiletype == "fill":
        dat = i["v"].split(sep = " ")   
        rangex = int(dat[2]) - int(dat[0])
        rangey = int(dat[3]) - int(dat[1])
        
        for y in range(rangey):
            for x in range(rangex):
                g_dynamic_map_tile = tile.Tile(i["n"], str(int(dat[0]) + x) + " " + str(int(dat[1]) + y))
                map_tiles.add(g_dynamic_map_tile)
                all_sprites.add(g_dynamic_map_tile)



while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                player.move_y = 1
            if e.key == pygame.K_UP:
                player.move_y = -1
            if e.key == pygame.K_LEFT:
                player.move_x = -1
            if e.key == pygame.K_RIGHT:
                player.move_x = 1

        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_DOWN:
                player.move_y = 0
            if e.key == pygame.K_UP:
                player.move_y = 0
            if e.key == pygame.K_LEFT:
                player.move_x = 0
            if e.key == pygame.K_RIGHT:
                player.move_x = 0


    all_sprites.update()
    all_sprites.draw(scr)

    pygame.display.flip()
    clock.tick(60)

    pygame.display.update()
    
