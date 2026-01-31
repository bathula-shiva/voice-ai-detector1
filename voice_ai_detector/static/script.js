async function detectVoice() {
    const fileInput = document.getElementById("audioFile");
    const resultDiv = document.getElementById("result");
    const loadingDiv = document.getElementById("loading");
    const predictionText = document.getElementById("prediction");
    const confidenceText = document.getElementById("confidence");

    if (!fileInput.files.length) {
        alert("Please upload an audio file");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    resultDiv.classList.add("hidden");
    loadingDiv.classList.remove("hidden");

    try {
        const response = await fetch("/detect", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        loadingDiv.classList.add("hidden");
        resultDiv.classList.remove("hidden");

        predictionText.innerText =
            data.prediction === "human"
                ? "✅ Human Voice"
                : "🤖 AI Generated Voice";

        confidenceText.innerText =
            "Confidence: " + (data.confidence * 100).toFixed(2) + "%";

    } catch (error) {
        loadingDiv.classList.add("hidden");
        alert("Error processing audio");
        console.error(error);
    }
}
