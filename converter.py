import base64 as b64
from PIL import Image
import pyperclip

def check_skin(skin_path):
    '''проверка работает с путем!'''
    try:
        with Image.open(skin_path) as img:
            width, height = img.size
            if width == 64 and height == 64:
                return True, width, height, None
            else:
                return False, width, height, f"Размер {width}x{height}, ожидается 64x64"

    except FileNotFoundError:
        return False, 0, 0, "Файл не найден"
    except Exception as e:
        return False, 0, 0, f"Ошибка открытия файла: {e}"


def convert_skin(file):
    with open(file,"rb")as skin:
        content = skin.read()
        result, width, height, error = check_skin(skin)
        if result:
            b64skin = b64.b64encode(content).decode('utf-8')
            print(b64skin)
            pyperclip.copy(b64skin)
            return str('\n'.join([b64skin[i:i+64] for i in range(0, len(b64skin), 64)]))
        else : str("ошибка импорта файла")
