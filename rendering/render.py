import pygame
import asyncio
from pathlib import Path
from settings.world_settings import frame_height, frame_width

# ------------------------------
# Base project directory
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------
# Sprite paths
# ------------------------------
PLAYER_SPRITE_PATH = BASE_DIR / 'sprites' / 'Tech Dungeon Roguelite - Asset Pack (DEMO)' / 'Players' / 'No Outlines' / 'players blue x3.png'
BRICK_PATH = BASE_DIR / 'sprites' / '128x128' / 'Brick' / 'Brick_20-128x128.png'


# ------------------------------
# Helper function to load images
# ------------------------------
def load_sprite(path: Path, alpha=True):
    if not path.exists():
        raise FileNotFoundError(f"Sprite not found: {path}")

    image = pygame.image.load(str(path))
    if alpha:
        return image.convert_alpha()
    return image.convert()


# ------------------------------
# Sprite getters (loaded AFTER display exists)
# ------------------------------
def get_player_sprite():
    return load_sprite(PLAYER_SPRITE_PATH)

def get_brick_sprite():
    return load_sprite(BRICK_PATH, alpha=False)


# ------------------------------
# Frame extraction
# ------------------------------
def player_idle(sprite_sheet):
    return sprite_sheet.subsurface((0, 0, frame_width, frame_height))


def player_move(sprite_sheet):
    running_frames = []
    for x in range(4):
        frame = sprite_sheet.subsurface(
            (x * frame_width, 0, frame_width, frame_height)
        )
        running_frames.append(frame)
    return running_frames

def idle_animation(screen, stop):
    screen.blit(stop, (screen.get_width()//2, screen.get_height()//2))

async def moving_animation(screen, move):
    for x in range(4):
        screen.blit(move[x], (screen.get_width()//2, screen.get_height()//2))
        await asyncio.sleep(0,2)