class AudioProcessor:
    def trim_audio(self, audio_length, audio_data):
        if audio_length > 60:
            # Logic to trim the audio to its middle segment
            mid_point = audio_length // 2
            start = max(0, mid_point - 30)  # 30 seconds before the midpoint
            end = min(audio_length, mid_point + 30)  # 30 seconds after the midpoint
            trimmed_audio = audio_data[start:end]
            return trimmed_audio
        return audio_data  # Return original audio if length is 60 seconds or less