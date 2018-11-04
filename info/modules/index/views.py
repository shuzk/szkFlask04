from . import index_blu


@index_blu.route("/")
def index():
    # current_app.logger.debug("debug")
    # current_app.logger.error("error")
    return "hello"
