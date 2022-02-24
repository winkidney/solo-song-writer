# solo-song-writer

特性：

- 支持歌词韵脚提取
- 支持歌词平仄输出并提供1234声标注

你可以用它干什么：

- 协助你分析别人的歌词韵脚
- 协助你分析别人的歌词平仄和旋律线的关系
- 辅助你作词，可以实时查看自己的歌词是否押韵，和旋律线的关系是什么样的

# 在线体验

请使用现代浏览器访问：[https://pinyin.37soloist.com](https://pinyin.37soloist.com)

# 部署你自己的实例
首先你需要自行配置一个 Python3.x 的环境，然后

```
pip install poetry
poetry install
./start_gunicorn.sh
```

访问`http://127.0.0.1:5678`即可访问服务

# 以后
也许会做成先IDE一样，可以为你自动补全或智能标注歌词内容呢？
