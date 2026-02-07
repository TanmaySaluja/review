alert("🔥 content.js LOADED");
console.log("🔥 content.js LOADED");

function extractReviews() {
  const reviewNodes = document.querySelectorAll("li[data-hook='review']");
  console.log("🧩 Reviews found:", reviewNodes.length);

  const reviews = [];

  reviewNodes.forEach((review) => {
    const getText = (selector) => {
      const el = review.querySelector(selector);
      return el ? el.innerText.trim() : null;
    };

    reviews.push({
      rating: getText("i[data-hook='review-star-rating'] span"),
      title: getText("a[data-hook='review-title'] span:last-child"),
      body: getText("span[data-hook='review-body'] span"),
      date: getText("span[data-hook='review-date']")
    });
  });

  return reviews;
}

function sendReviews() {
  const reviews = extractReviews();

  console.log("🚀 Sending structured reviews", reviews);

  fetch("http://127.0.0.1:8000/receive", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      reviews: reviews
    })
  })
    .then(res => {
      console.log("✅ Status:", res.status);
      return res.json();
    })
    .then(data => {
      console.log("📥 Backend reply:", data);
    })
    .catch(err => {
      console.error("❌ Fetch failed:", err);
    });
}

// Wait until reviews actually exist
const observer = new MutationObserver(() => {
  const reviews = document.querySelectorAll("li[data-hook='review']");
  if (reviews.length > 0) {
    console.log("🧩 Reviews detected, extracting…");
    observer.disconnect();
    sendReviews();
  }
});

observer.observe(document.body, {
  childList: true,
  subtree: true
});
