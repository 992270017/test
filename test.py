import random

# 地图大小
MAP_WIDTH = 10
MAP_HEIGHT = 6

# 玩家初始位置
player_x = random.randint(0, MAP_WIDTH - 1)
player_y = random.randint(0, MAP_HEIGHT - 1)

# 游戏循环
while True:
    # 渲染地图
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if x == player_x and y == player_y:
                print("P ", end="")
            else:
                print("_ ", end="")
        print()
    
    # 获取玩家输入
    move = input("请输入移动方向（w上，s下，a左，d右，q退出）：")
    
    # 处理玩家输入
    if move == "w":
        player_y -= 1
    elif move == "s":
        player_y += 1
    elif move == "a":
        player_x -= 1
    elif move == "d":
        player_x += 1
    elif move == "q":
        break
    
    # 边界检查
    player_x = max(0, min(player_x, MAP_WIDTH - 1))
    player_y = max(0, min(player_y, MAP_HEIGHT - 1))

print("游戏结束")
