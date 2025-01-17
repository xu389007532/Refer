
def spell():
    potion = "魔法药水" # 我是局部变量
    print(potion)
spell()

def forest():
    secret = "隐藏的秘密"
    def grove():
        print(secret) # 我能看见森林的秘密
    grove()
forest()


galaxy = "宇宙"

def stargaze():
    print(galaxy) # 星空，我来了！

stargaze()

def change_universe():
    global galaxy # 告诉Python，我要修改全局的星星
    galaxy = "新的宇宙"
change_universe()
print(galaxy) # 宇宙已变？


x = "外面的世界"
def mystery():
    x = "内心的独白" # 遮挡了外面的x
    print(x)
mystery()
print(x) # 这两个x，不是同一个世界

outer = "外围区域"


def outer_function():
    middle = "中间地带"

    def inner_function():
        local = "核心机密"
        print(local)
        print(middle)
        print(outer)

    inner_function()

outer_function()


def create_maze():
    path = "起点"

    def reveal_path():
        nonlocal path # 指明我要修改外面的path
        path = "终点"
    reveal_path()
    print(path) # 从起点到终点

create_maze()


def maze():
    clue1 = "第一关"

    def next_clue():
        clue2 = "第二关"

        def final_clue():
            print(clue1, clue2)  # 穿越迷宫

        final_clue()

    next_clue()

maze()
