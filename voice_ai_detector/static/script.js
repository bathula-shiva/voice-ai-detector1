async function predict() {
    const energy = document.getElementById("energy").value;

    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ energy: Number(energy) })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = 
        `Result: ${data.result}<br>Confidence: ${data.confidence * 100}%`;
}
