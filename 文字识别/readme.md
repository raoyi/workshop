# Tesseract-OCR的Python实现

**前提：**

- 安装[Tesseract-OCR Windows版](https://github.com/UB-Mannheim/tesseract/wiki)（例如安装到D:\Program Files\Tesseract-OCR）
- 安装的时候勾选中文和Math选项

1. 添加 `lang='chi_sim'` 以识别中文
2. 识别英文则不用加lang参数
3. 加 `r` 表示禁用转义字符