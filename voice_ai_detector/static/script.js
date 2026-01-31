async function detectVoice() {
    const fileInput = document.getElementById("audioFile");
    const loading = document.getElementById("loading");
    const result = document.getElementById("result");
    const prediction = document.getElementById("prediction");
    const confidence = document.getElementById("confidence");

    if (!fileInput.files.length) {
        alert("Please upload an audio file");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    loading.classList.remove("hidden");
    result.classList.add("hidden");

    const response = await fetch("/detect", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    loading.classList.add("hidden");
    result.classList.remove("hidden");

    prediction.innerText =
        data.prediction === "human"
            ? "✅ Human Voice"
            : "🤖 AI Generated Voice";

    confidence.innerText =
        "Confidence: " + (data.confidence * 100).toFixed(2) + "%";
}
