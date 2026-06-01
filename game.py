import random
import time
import os
import keyboard  # pip install keyboard が必要

WIDTH = 20
HEIGHT = 10

player_x = WIDTH // 2
enemy_x = random.randint(0, WIDTH - 1)
enemy_y = 0

score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear()

    # 敵の移動
    enemy_y += 1
    if enemy_y >= HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - 1)
        score += 1

    # プレイヤーの移動
    if keyboard.is_pressed("left"):
        player_x = max(0, player_x - 1)
    if keyboard.is_pressed("right"):
        player_x = min(WIDTH - 1, player_x + 1)

    # 描画
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            if x == player_x and y == HEIGHT - 1:
                line += "P"
            elif x == enemy_x and y == enemy_y:
                line += "O"
            else:
                line += "."
        print(line)

    print(f"\nScore: {score}")

    # 当たり判定
    if enemy_x == player_x and enemy_y == HEIGHT - 1:
        print("\nGAME OVER!")
        break

    time.sleep(0.1)

