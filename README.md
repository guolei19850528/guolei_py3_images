## 介绍

**郭磊 Images API**

## 软件架构

~python 3.*

## 安装教程

```shell
pip install guolei-py3-images
```

## 目录说明

### imgkit Api 示例

[官方文档](https://github.com/jarrekk/imgkit)

```python
import os
import random
import string
from guolei_py3_images.imgkit import str_to_image

output_path = str_to_image(
    output_path=os.path.join(os.path.dirname(__file__), "runtime", 'test.png'),
    content="".join(random.choices(string.ascii_letters,k=100))
)
print(output_path)
```