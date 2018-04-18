from PIL import Image

if __name__ == '__main__':
    #打开原图
    cat = Image.open('cat.jpeg')
    #设置缩略图大小
    size = (128, 128)
    #生成缩略图
    cat.thumbnail(size)
    #保存缩略图
    cat.save('thumbnail.jpeg')
    #打开原图
    cat = Image.open('cat.jpeg')
    #设置剪切大小
    coordinate = (100,200,600,400)
    #剪切图片
    region = cat.crop(coordinate)
    #保存剪切图片
    region.save('region.jpeg')
    #设置粘贴位置
    coordinate2 = (100,0,600,200)
    #粘贴图片
    cat.paste(region, coordinate2)
    #保持粘贴图片
    cat.save('cat2.jpeg')




