document.addEventListener('DOMContentLoaded', function () {
    fetch('/get_recommendations')
      .then(response => response.json())
      .then(data => {
        const recommendationList = document.getElementById('recommendation-list');
        data.forEach(item => {
          const li = document.createElement('li');
          li.textContent = `${item.title}: ${item.description}`;
          recommendationList.appendChild(li);
        });
      });
  });
  