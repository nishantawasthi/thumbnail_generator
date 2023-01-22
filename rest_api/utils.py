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
