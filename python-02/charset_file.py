# python中的字符编码

def file_gbk(filePath):
    with open(file=filePath, mode="r", encoding="gbk") as f:
        return f.read()


def file_utf8(filePath):
    with open(file=filePath, mode="r", encoding="utf8") as f:
        return f.read()


def file_write(filePath, content):
    with open(file=filePath, mode="w", encoding="utf8") as f:
        f.write(content)


if __name__ == "__main__":
    file1 = "file/gbk编码.txt"
    file2 = "file/utf8编码.txt"

    content = file_gbk(file1) + "\n" + file_utf8(file2)
    filePath = input("请输入文件名称：")
    file_write(filePath,content)