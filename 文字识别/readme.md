# Tesseract-OCR的Python实现

**前提：**

- 安装[Tesseract-OCR Windows版](https://github.com/UB-Mannheim/tesseract/wiki)（例如安装到D:\Program Files\Tesseract-OCR）
- 安装的时候勾选中文和Math选项
- pip install pytesseract
- pip install Pillow

1. 添加 `lang='chi_sim'` 以识别中文
2. 识别英文则不用加lang参数
3. 加 `r` 表示禁用转义字符
4. 准备图片 `txt.jpg` 以供识别（名称随意，图片格式随意）

网络帮助文档：https://www.cnblogs.com/zhangxinqi/p/9297292.html
