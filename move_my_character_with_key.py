from pico2d import *

open_canvas()
character = load_image('animation_sheet_link.png')

def handle_events():
    global running, dir_LR

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_LR += 1
            elif event.type == SDLK_LEFT:
                dir_LR -= -1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_LR -= 1
            elif event.key == SDLK_LEFT:
                dir_LR += 1

running = True
window_x = 800 // 2
frame = 0
dir_LR = 0

while running:
    clear_canvas()
    if dir_LR == 0: # IDLE 상태
        character.clip_draw(0, 728, 96, 104, window_x, 50)
    elif dir_LR == +1:  # 오른쪽 이동 상태
        character.clip_draw(frame * 96, 0, 96, 104, window_x, 50)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    window_x += dir_LR * 5
    delay(0.05)

close_canvas()