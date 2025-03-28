from flask import json
from app import create_app

app = create_app()

def test_audio_processing_length():
    with app.test_client() as client:
        response = client.post('/process-audio', json={'length': 70})
        assert response.status_code == 200
        assert response.json['message'] == 'Audio trimmed to middle segment.'

        response = client.post('/process-audio', json={'length': 30})
        assert response.status_code == 200
        assert response.json['message'] == 'Audio length is acceptable, no trimming needed.'

        response = client.post('/process-audio', json={'length': -10})
        assert response.status_code == 400
        assert response.json['error'] == 'Invalid audio length.'