class InvalidImageError(Exception):
    """
    This exception is raised when the file is invalid image
    """
    error_code = 400
    error_message = "Invalid or corrupt image"
