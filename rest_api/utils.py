from io import BytesIO
import traceback

from PIL import Image


def check_image(file):
    """
    Checks if the give file is image and corrupted or not.

    Args:
        file (ioBuffer): InMemoryUploadedFile object

    Returns:
        bool: Return true if image is not corrupted.
    """
    try:
        if not file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            return False
        temp_image = Image.open(file)
        temp_image.verify()
        temp_image_second = Image.open(file)
        temp_image_second.transpose(Image.FLIP_LEFT_RIGHT)
        return True
    except Exception as err:
        print(err)
        traceback.print_exc()
        return False


def generate_image():
    """
    Generates a in memory image for unit testing.

    Returns:
        image: Returns in memory image
    """
    try:
        file = BytesIO()
        image = Image.new('RGB', size=(4355, 5543), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
    except Exception as err:
        print(err)
        traceback.print_exc()
