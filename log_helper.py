def log_error(error):
    import logging
    logger = logging.getLogger('django')
    logger.exception(error)
