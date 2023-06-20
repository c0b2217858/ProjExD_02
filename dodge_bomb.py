import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

# 演習1{
    bomb_img = pg.Surface((20,20))
    pg.draw.circle(bomb_img,(255, 0, 0), (10, 10), 10)
    bomb_img.set_colorkey((0,0,0))
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT)
    bomb_rct = bomb_img.get_rect()  # 爆弾Surfaceに対応する画像Rectを取得する
    bomb_rct.center = x,y  # 爆弾の中心座標を乱数で指定する
# }演習1

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
# 演習1{
        #screen.blit(bomb_img, [800, 400])
        screen.blit(bomb_img, bomb_rct)
# }演習1

        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()