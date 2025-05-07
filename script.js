document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    const promptInput = document.getElementById('prompt');
    const resultDiv = document.getElementById('result');
    const loadingDiv = document.getElementById('loading');

    generateBtn.addEventListener('click', function() {
        const prompt = promptInput.value.trim();

        if (!prompt) {
            alert('Please enter a prompt');
            return;
        }

        // Show loading message
        loadingDiv.classList.remove('hidden');
        resultDiv.innerHTML = '';

        // Send request to server
        fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'prompt': prompt
            })
        })
        .then(response => response.json())
        .then(data => {
            // Hide loading message
            loadingDiv.classList.add('hidden');

            // Display the image
            if (data.image) {
                resultDiv.innerHTML = `<img src="${data.image}" alt="Generated image">`;
            } else {
                resultDiv.innerHTML = '<p>Error generating image. Please try again.</p>';
            }
        })
        .catch(error => {
            loadingDiv.classList.add('hidden');
            resultDiv.innerHTML = '<p>Error generating image. Please try again.</p>';
            console.error('Error:', error);
        });
    });
});