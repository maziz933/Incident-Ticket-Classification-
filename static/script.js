function predictEmail() {
    const emailContent = document.getElementById('email_content').value;
    console.log("Email content:", emailContent);
    
    // Simulate prediction results
    // Update the progress bars
    updateProgressBar('Serveur Mutualisé', 50);
    updateProgressBar('Serveur Privé', 60);
    updateProgressBar('Accès Internet', 30);
    updateProgressBar('Téléphonie', 20);

    document.querySelector('.form-container').classList.add('with-results');
    document.getElementById('prediction-result').style.display = 'block';
}

function updateProgressBar(label, value) {
    const progressBar = document.querySelector(`.progress-label:contains(${label}) + .progress-bar span`);
    if (progressBar) {
        progressBar.style.width = value + '%';
        progressBar.setAttribute('data-percentage', value + '%');
        progressBar.textContent = value + '%';
    }
}

function refreshPage() {
    document.getElementById('email_content').value = '';
    document.querySelector('.form-container').classList.remove('with-results');
    document.getElementById('prediction-result').style.display = 'none'; // Hide the prediction result
    document.getElementById('refresh-button').style.display = 'none'; // Hide the "Refresh" button
}

// Ensure the DOM is fully loaded before attaching event handlers
window.onload = function() {
    document.getElementById('email-form').onsubmit = function(event) {
        event.preventDefault(); // Prevent form submission to test the front-end

        // predictEmail(); // Simulate the prediction
        
        // Show the "Refresh" button
        document.getElementById('refresh-button').style.display = 'inline-block';
    };
};

function resetProgress() {
    document.getElementById('progress-container').style.display = 'none';
    document.querySelector('textarea[name="email_content"]').value = '';
    document.getElementById('refresh-button').style.display = 'none';// Hide the "Refresh" button
}

function toggleAutoAssign() {
    const checkbox = document.getElementById('auto-assign-btn');
    const assignButtons = document.querySelectorAll('.assign-btn');
    const displayStyle = checkbox.checked ? 'none' : 'inline-block';
    assignButtons.forEach(button => {
        button.style.display = displayStyle;
    });
}

function toggleMessageDetails(event) {
    const emailItem = event.currentTarget;
    const messageDetails = emailItem.querySelector('.message-details');
    if (messageDetails.style.display === 'none' || !messageDetails.style.display) {
        messageDetails.style.display = 'block';
    } else {
        messageDetails.style.display = 'none';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const emailItems = document.querySelectorAll('.email-item');
    emailItems.forEach(item => {
        item.addEventListener('click', toggleMessageDetails);
    });
});


window.onload = function() {
    // Show the progress bars once the prediction is complete
    const progressContainer = document.getElementById('progress-container');
    if (progressContainer && progressContainer.children.length > 0) {
        progressContainer.style.display = 'flex';
        document.getElementById('refresh-button').style.display = 'inline-block';

    }
};
