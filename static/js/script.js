let selectedTask = "summarize";

function setTask(task, btn) {
    selectedTask = task;
    document.querySelectorAll(".task")
        .forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
}

function toggleTheme() {
    const body = document.body;
    body.classList.toggle("dark");
    body.classList.toggle("light");
}

function processText() {
    const text = document.getElementById("inputText").value;
    const output = document.getElementById("outputText");

    if (!text.trim()) {
        output.innerText = "Please enter some text.";
        return;
    }

    output.innerText = "⏳ Processing...";

    fetch("/process", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            text: text,
            task: selectedTask
        })
    })
    .then(res => res.json())
    .then(data => output.innerText = data.result)
    .catch(() => output.innerText = "❌ Server error.");
}
