from flask import current_app, jsonify
from flask import make_response
from flask import request

from info import constants
from info import redis_store
from info.utils.captcha.captcha import captcha
from . import passport_blu


@passport_blu.route("/image_code")
def get_image_code():
    """获取图片验证码"""

    # 1.获取当前的图片编号id
    code_id = request.args.get("code_id")
    # 2.生成验证码
    name, text, image = captcha.generate_captcha()
    try:
        # 保存当前生成的图片验证码内容
        redis_store.setex("ImageCode_" + code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
    except Exception as e:
        current_app.logger.error(e)
        return make_response(jsonify(errno=RET.DATAERR, errmsg="保存图片验证码失败"))
    # 返回相应内容
    resp = make_response(image)
    # 设置内容类型
    resp.headers["Content-Type"] = "image/jpg"
    return resp
