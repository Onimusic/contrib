def get_default_response_dict() -> dict:
    """ Returns the default api response as {data:{items:[], message:str}, status:str}
    """
    return {'data': {'items': [], 'message': 'n/a'}, 'status': get_success_status()}


def get_success_status() -> str:
    """ Returns the success status.
    """
    return 'success'


def get_generic_error_status() -> str:
    """ Returns the generic error status.
    """
    return 'error'


def get_generic_error_message() -> str:
    """ Returns the generic error message.
    """
    return 'Unknown error.'


def get_generic_error404_message() -> str:
    """ Returns the generic error message.
    """
    return 'Object not found.'
