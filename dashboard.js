
function getMetrics() {
    const ticker = document.getElementById("tickerInput").value;
    fetch(`http://127.0.0.1:8000/metrics/${ticker}`)
        .then(response => response.json())
        .then(data => document.getElementById("results").innerHTML = `
            <p>Sharpe Ratio: ${data.sharpe_ratio}</p>
            <p>Annualized Volatility: ${data.annualized_volatility}</p>
            <p>Annualized Mean: ${data.annualized_mean}</p>
            <p>VaR: ${data.var}</p>
    `)
}