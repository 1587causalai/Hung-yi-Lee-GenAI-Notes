# Linux Basics


## less 命令笔记

less 是一个很棒的命令行工具，我经常用它来查看文本文件。它比 more 命令强大多了，可以自由地前后滚动浏览文件内容。

使用起来很简单，只需要输入：

```bash
less filename
``` 

我最常用的几个快捷键：

- 空格键：向下翻页
- b：向上翻页
- g 和 G：跳到文件开头和末尾
- /和?：向前和向后搜索
- n 和 N：下一个和上一个搜索结果
- q：退出

为什么我喜欢用
less？它灵活，搜索功能强大，而且不会一次性加载整个文件，对大文件很友好。我还经常用它来查看命令输出，比如 `ls -l | less`。

有两个小技巧我觉得特别有用：

1. `less +F` 可以实时查看不断更新的日志文件
2. `less -N` 可以显示行号

总之，less 让我的命令行使用体验更加流畅。多用用，你也会喜欢上它的！

## argparse in terminal


argparse 是 Python 标准库中用于解析命令行参数的模块。它提供了一种简单而强大的方式来处理脚本的命令行选项。

基本使用步骤：

1. 创建解析器：
```python
import argparse
parser = argparse.ArgumentParser(description="Test Reward Model")
```

2. 添加参数：
```python
parser.add_argument("--model_name_or_path", type=str, default="merged-sft", help="Path to pretrained model")
parser.add_argument("--use_fast_tokenizer", action="store_true", help="Whether to use fast tokenizer")
parser.add_argument("--use_gpu", action="store_true", help="Whether to use GPU")
```

3. 解析参数：
```python
args = parser.parse_args()
```

4. 使用解析后的参数：
```python
print("Parsed arguments:", args)
tokenizer, model = setup_reward_model(args)
```

特殊用法：
- `action="store_true"`：创建一个无需额外值的命令行开关选项。当该选项出现时（如 `--use_gpu`），相应参数被设置为 True，否则为 False。

示例命令：
```
python script.py --model_name_or_path custom-model --use_gpu
```
这个命令会使用自定义模型路径，启用 GPU，而 `use_fast_tokenizer` 保持默认的 False。

argparse 的优势：
1. 自动生成帮助信息（使用 -h 或 --help）
2. 参数验证和类型转换
3. 支持短格式（如 -v）和长格式（如 --verbose）参数
4. 可以设置参数的默认值和帮助文本
5. 灵活性高，可以处理复杂的命令行接口需求

通过使用 argparse，可以显著提高 Python 脚本的可用性、可读性和可维护性，使得命令行工具的开发变得更加高效和专业。