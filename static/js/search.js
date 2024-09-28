function performSearch() {
    const query = document.getElementById('query').value;
    
    fetch(`/perform_search?query=${query}`)
      .then(response => response.json())
      .then(data => {
        const resultList = document.getElementById('search-results');
        resultList.innerHTML = '';
        data.forEach(item => {
          const li = document.createElement('li');
          li.textContent = `${item.title}: ${item.description}`;
          resultList.appendChild(li);
        });
      });
  }
  