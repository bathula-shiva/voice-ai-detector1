async function detectVoice() {
    const fileInput = document.getElementById("audioFile");
    const resultDiv = document.getElementById("result");
    const predictionText = document.getElementById("prediction");
    const confidenceText = document.getElementById("confidence");

    if (!fileInput.files.length) {
        alert("Please upload an audio file");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    predictionText.innerText = "Detecting...";
    confidenceText.innerText = "";
    resultDiv.classList.remove("hidden");

    try {
        const response = await fetch("/detect", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        predictionText.innerText = `Prediction: ${data.prediction}`;
        confidenceText.innerText = `Confidence: ${data.confidence * 100}%`;
    } catch (error) {
        predictionText.innerText = "Error detecting voice";
        confidenceText.innerText = "";
    }
}
