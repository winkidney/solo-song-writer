from io import StringIO

from flask import Flask, render_template, request
import pypinyin


app = Flask(__name__)


def get_results(input_strs: str):
    string = StringIO(input_strs)
    lines = []
    for line in string.readlines():
        line = line.strip()
        if len(line) <= 0:
            lines.append("")
            continue
        translated = pypinyin.pinyin(line[-1], style=pypinyin.Style.FINALS_TONE)
        lines.append(
            translated[-1][0]
        )
    return lines


@app.route('/', methods=["POST", "GET"])
def hello_world():  # put application's code here
    original = request.form.get("original")
    context = {
        "original": original,
        "out": "",
    }
    if request.method == "POST":
        context['out'] = "\n".join(get_results(original))
        return render_template(
            "index.html",
            **context
        )
    else:
        context['original'] = "在这里输入歌词"
    return render_template(
        "index.html",
        **context,
    )


if __name__ == '__main__':
    app.run(debug=True)
