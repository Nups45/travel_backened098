document.getElementById('book-now').addEventListener('click', function () {
    document.getElementById('booking-modal').style.display = 'block';
});

document.getElementById('close-modal').addEventListener('click', function () {
    document.getElementById('booking-modal').style.display = 'none';
});

function showService(service) {
    // Hide all service details
    document.querySelectorAll('.service-details').forEach(function (el) {
        el.style.display = 'none';
    });
    
    // Show the selected service
    document.getElementById(service).style.display = 'block';
}
