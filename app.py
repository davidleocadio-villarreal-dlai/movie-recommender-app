import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
from models import MovieRecommendation

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': 'Please provide a movie request'}), 400
    
    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a movie recommendation expert. Provide accurate movie recommendations with ratings and details."
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            response_format=MovieRecommendation
        )
        
        recommendation = completion.choices[0].message.parsed
        return jsonify(recommendation.model_dump())
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
