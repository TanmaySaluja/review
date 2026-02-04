document.getElementById("send").addEventListener("click", async () => {
  const status = document.getElementById("status");

  // Get active tab
  const tabs = await browser.tabs.query({
    active: true,
    currentWindow: true
  });

  // Ask content script for page text
  const response = await browser.tabs.sendMessage(
    tabs[0].id,
    { action: "GET_PAGE_TEXT" }
  );

  const pageText = response.text;

  // Send text to FastAPI
  try {
    const res = await fetch("http://127.0.0.1:8000/receive", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text: pageText })
    });

    const data = await res.json();
    status.textContent = "Sent! Length: " + data.length;

  } catch (err) {
    status.textContent = "Error sending text";
    console.error(err);
  }
});
