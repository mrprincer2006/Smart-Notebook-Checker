document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    const dropZone = document.getElementById('dropZone');
    const scanCard = document.getElementById('scanCard');
    const processingCard = document.getElementById('processingCard');
    const resultsArea = document.getElementById('resultsArea');
    const resultsList = document.getElementById('resultsList');
    const langBtn = document.getElementById('langBtn');

    let currentLang = 'en';

    // Toggle Language
    langBtn.addEventListener('click', () => {
        currentLang = currentLang === 'en' ? 'hi' : 'en';
        document.querySelectorAll('[data-en]').forEach(el => {
            el.innerText = el.getAttribute(`data-${currentLang}`);
        });
    });

    // Handle File Selection
    dropZone.addEventListener('click', () => fileInput.click());

    fileInput.addEventListener('change', async (e) => {
        if (e.target.files.length > 0) {
            await processImage(e.target.files[0]);
        }
    });

    async function processImage(file) {
        scanCard.style.display = 'none';
        processingCard.style.display = 'block';

        const formData = new FormData();
        formData.append('file', file);

        try {
            // Use environment variable or default to localhost
            // Use environment variable or default to Vercel api path
            const backendUrl = window.BACKEND_URL || '/api';
            const response = await fetch(`${backendUrl}/scan`, {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            displayResults(data.results);
        } catch (error) {
            alert('Error connecting to backend. Make sure the server is running.');
            scanCard.style.display = 'block';
        } finally {
            processingCard.style.display = 'none';
        }
    }

    function displayResults(results) {
        resultsArea.style.display = 'block';
        resultsList.innerHTML = '';

        results.forEach(res => {
            const item = document.createElement('div');
            item.className = `result-item ${res.status}`;

            const statusLabel = currentLang === 'en' ?
                (res.status === 'correct' ? 'Correct' : 'Wrong') :
                (res.status === 'correct' ? 'सही' : 'गलत');

            item.innerHTML = `
                <div>
                    <strong>${res.problem}</strong><br>
                    <small>Student: ${res.student_answer} | Correct: ${res.correct_answer}</small>
                </div>
                <span class="status-badge ${res.status}">${statusLabel}</span>
            `;
            resultsList.appendChild(item);
        });
    }
});
