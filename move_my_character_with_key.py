from pico2d import *

open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet_link.png')

def handle_events():
    global running, dir_LR, dir_UD

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_LR += 1
            elif event.key == SDLK_LEFT:
                dir_LR -= 1
            elif event.key == SDLK_UP:
                dir_UD += 1
            elif event.key == SDLK_DOWN:
                dir_UD -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_LR -= 1
            elif event.key == SDLK_LEFT:
                dir_LR += 1
            elif event.key == SDLK_UP:
                dir_UD -= 1
            elif event.key == SDLK_DOWN:
                dir_UD += 1


running = True
window_x = 800 // 2
window_y = 50
frame = 0
dir_LR = 0
dir_UD = 0

while running:
    clear_canvas()
    background.draw(400, 300)
    if dir_LR == 0 and dir_UD == 0: # IDLE 상태
        character.clip_draw(0, 728, 96, 104, window_x, window_y)
    elif dir_LR == 1:  # 오른쪽 이동 상태
        character.clip_draw(frame * 96, 0, 96, 104, window_x, window_y)
    elif dir_LR == -1:  # 왼쪽 이동 상태
        character.clip_draw(frame * 97, 208, 96, 104, window_x, window_y)
    elif dir_UD == 1:   # 위쪽 이동 상태
        character.clip_draw(frame * 96, 104, 96, 104, window_x, window_y)
    elif dir_UD == -1:  # 아래쪽 이동 상태
        character.clip_draw(frame * 96, 312, 96, 104, window_x, window_y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    window_x += dir_LR * 5
    window_y += dir_UD * 5
    delay(0.05)

close_canvas()