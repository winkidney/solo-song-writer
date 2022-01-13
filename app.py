from io import StringIO
import re

from flask import Flask, render_template, request
import pypinyin


app = Flask(__name__)


def get_rhyme(input_strs: str):
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


def number2rhythm(number: int):
    if number in (1, 2):
        return "平"
    else:
        return "仄"


def get_rhythm(input_strs: str):
    string = StringIO(input_strs)
    lines = []
    for line in string.readlines():
        line = line.strip()
        if len(line) <= 0:
            lines.append("")
            continue
        translated = pypinyin.pinyin(line, style=pypinyin.Style.TONE3)
        translated_chars = ""
        translated_numbers = ""
        for r in translated:
            found = re.findall(r"\d+", r[0])
            if len(found) > 0:
                number = found[0]
                translated_numbers += number
                translated_chars += number2rhythm(int(number))
            else:
                translated_numbers += " "
                translated_chars += " "
        lines.append(
            " ".join([translated_chars, translated_numbers])
        )
    return lines


def process(process_rhythm=False):
    original = request.form.get("original")
    context = {
        "original": original,
        "out": "",
    }
    if request.method == "POST":
        rhymes = get_rhyme(original)
        if not process_rhythm:
            context['out'] = "\n".join(rhymes)
        else:
            rhythms = get_rhythm(original)
            context['out'] = "\n".join(
                [f"{rhyme.ljust(5)} {rhythm}" for rhythm, rhyme in zip(rhythms, rhymes)]
            )
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


@app.route('/rhythm', methods=["POST", "GET"])
def handle_rhythm():
    return process(True)


@app.route('/', methods=["POST", "GET"])
def handle_rhyme():
    return process(False)


if __name__ == '__main__':
    app.run(debug=True)
