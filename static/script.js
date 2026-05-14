const form = document.querySelector('form');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const res = await fetch('/predict', {
    method: 'POST',
    body: new FormData(form)
  });
  const data = await res.json();
  const resultDiv = document.getElementById('result');
  if (data.prediction !== undefined) {
    resultDiv.textContent = data.prediction + ' oz';
  } else if (data.error) {
    resultDiv.textContent = 'Error: ' + data.error;
  }
});
