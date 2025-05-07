from flask import Flask, render_template, request, jsonify
from main import generate_image
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    
    # Generate image
    image = generate_image(prompt)
    
    # Convert image to base64 for web display
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return jsonify({'image': f'data:image/png;base64,{img_str}'})

if __name__ == '__main__':
    app.run(debug=True)