browser.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "GET_PAGE_TEXT") {
    const text = document.body.innerText;
    sendResponse({ text });
  }
});
