from flask import Blueprint, request, jsonify


audio_routes = Blueprint("audio", __name__)


@audio_routes.route("/process-text", methods=["POST"])
def process_audio():
    data = request.get_json()
    text = data.get("text")
    trimmed_text, message = trim_text_for_audio(text)
    return jsonify({"message": message, "text": trimmed_text}), 200


def trim_text_for_audio(text, words_per_second=3, max_audio_length=60):
    words = text.split()
    total_words = len(words)
    audio_length = total_words / words_per_second

    if audio_length <= max_audio_length:
        message = "Audio length is acceptable"
        return text, message
    else:
        message = "Audio trimmed"
        excess_length = audio_length - max_audio_length
        excess_words = int(excess_length * words_per_second)
        trim_words = excess_words // 2

        trimmed_text = " ".join(words[trim_words : total_words - trim_words])
        return trimmed_text, message
