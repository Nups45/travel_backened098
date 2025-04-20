// Fetch and display destinations
function loadDestinations() {
  fetch('http://127.0.0.1:5000/destinations')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('destinations');
      container.innerHTML = '';
      data.forEach(dest => {
        const div = document.createElement('div');
        div.className = 'destination';
        div.innerHTML = `<h3>${dest.name}, ${dest.country}</h3>
                         <p>${dest.description}</p>
                         <img src="${dest.image_url}" alt="${dest.name}" width="200">`;
        container.appendChild(div);
      });
    });
}

// Add new destination
document.getElementById('destinationForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const name = document.getElementById('name').value;
  const country = document.getElementById('country').value;
  const description = document.getElementById('description').value;
  const image_url = document.getElementById('image_url').value;

  fetch('http://127.0.0.1:5000/add-destination', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, country, description, image_url })
  })
  .then(response => response.json())
  .then(data => {
    alert(data.message);
    loadDestinations();
    document.getElementById('destinationForm').reset();
  });
});

// Initial load
loadDestinations();
