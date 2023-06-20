import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900

# 演習3{
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}
# }演習3

# 演習4{
def check_bound(rect: pg.Rect) -> tuple[bool,bool]:
    yoko, tate = True,True
    if rect.left < 0 or WIDTH < rect.right:  # 横方向判定
        yoko = False
    if rect.top < 0 or HEIGHT < rect.bottom:  # 縦方向判定
        tate = False
    return yoko,tate
# }演習4

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

# 演習3{
    # こうかとんSurface（kk_img）からこうかとんRect（kk_rct）を抽出する
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
# }演習3

# 演習1{
    bomb_img = pg.Surface((20,20))
    pg.draw.circle(bomb_img,(255, 0, 0), (10, 10), 10)
    bomb_img.set_colorkey((0,0,0))
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    bomb_rct = bomb_img.get_rect()  # 爆弾Surfaceに対応する画像Rectを取得する
    bomb_rct.center = x,y  # 爆弾の中心座標を乱数で指定する
# }演習1

    vx,vy = +5,+5  # 演習2

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

# 演習3{            
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 合計移動量
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)
# }演習3

# 演習4{ 
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
# }演習4 


        screen.blit(bg_img, [0, 0])
        #screen.blit(kk_img, [900, 400])
        screen.blit(kk_img, kk_rct)  # 演習3
        bomb_rct.move_ip(vx,vy)  # 演習2

# 演習4{         
        yoko,tate = check_bound(bomb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
# }演習4 

# 演習1{
        #screen.blit(bomb_img, [800, 400])
        screen.blit(bomb_img, bomb_rct)
# }演習1

        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()