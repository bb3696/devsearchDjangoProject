// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});

let alertWrapper = document.querySelector('.alert');
let alertClose = document.querySelector('.alert__close');


if (alertWrapper && alertClose) {  // 确保 alertClose 存在
  console.log("✅ Adding event listener to close button...");
  alertClose.addEventListener('click', () => {
    console.log("❌ Close button clicked!");
    alertWrapper.style.display = 'none';
  });
}

