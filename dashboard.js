
function getMetrics() {
    const ticker = document.getElementById("tickerInput").value;
    fetch(`http://127.0.0.1:8000/metrics/${ticker}`)
    
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("results").innerHTML = `<p>${data.error}</p>`
            } else {
                document.getElementById("results").innerHTML = `
                <p>Sharpe Ratio: ${data.sharpe_ratio.toFixed(2)}</p>
                <p>Annualized Volatility: ${data.annualized_volatility.toFixed(2)}</p>
                <p>Annualized Mean: ${data.annualized_mean.toFixed(2)}</p>
                <p>VaR: ${data.var.toFixed(2)}</p>`
            }
    })
}