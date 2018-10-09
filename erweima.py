from MyQR import myqr
import os

version, level, qr_name = myqr.run(
    words = "https://open.weixin.qq.com/qr/code?username=agriplan",
    version = 1,
    level = 'L',
    picture = "123.gif",
    colorized = True,
    contrast = 1.0,
    brightness = 1.0,
    save_name = "3.gif",
    save_dir = os.getcwd()
)
#=====================================================
#参数解释
# Positional parameter
#     words: str
# Optional parameters
# version: int, from 1 to 40
# level: str, just one of('L', 'M', 'Q', 'H')
# picutre: str, a filename of a image
# colorized: bool
# constrast: float
# brightness: float
# 默认输出文件名是“ qrcode.png"，而默认存储位置是当前目录
# save_name: str, the output filename like 'example.png'
# save_dir: str, the output directory

#====================================================================
#生成带Logo的二维码
#====================================================================
# from PIL import Image
# import qrcode, os
#
# url = 'https://blog.csdn.net/qq_40949713/article/details/80512339'
# qrcodename = 'fut'
# def create_qrcode(url, qrcodename):
#     qr = qrcode.QRCode(
#         version=1,  # 设置容错率为最高
#         error_correction=qrcode.ERROR_CORRECT_H,  # 用于控制二维码的错误纠正程度
#         box_size=8,  # 控制二维码中每个格子的像素数，默认为10
#         border=1,  # 二维码四周留白，包含的格子数，默认为4
#         # image_factory=None,  保存在模块根目录的image文件夹下
#         # mask_pattern=None
#     )
#
#     qr.add_data(url)  # QRCode.add_data(data)函数添加数据
#     qr.make(fit=True)  # QRCode.make(fit=True)函数生成图片
#
#     img = qr.make_image()
#     img = img.convert("RGBA")  # 二维码设为彩色
#     logo = Image.open('futon.jpg')  # 传gif生成的二维码也是没有动态效果的
#
#     w, h = img.size
#     logo_w, logo_h = logo.size
#     factor = 4  # 默认logo最大设为图片的四分之一
#     s_w = int(w / factor)
#     s_h = int(h / factor)
#     if logo_w > s_w or logo_h > s_h:
#         logo_w = s_w
#         logo_h = s_h
#     logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)
#     l_w = int((w - logo_w) / 2)
#     l_h = int((h - logo_h) / 2)
#     logo = logo.convert("RGBA")
#     img.paste(logo, (l_w, l_h), logo)
#     # img.show()
#     img.save(os.getcwd() + '/' + qrcodename + '.png', quality=100)
# if __name__ == '__main__':
#     create_qrcode(url, qrcodename)
