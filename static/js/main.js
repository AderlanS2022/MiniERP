(function () {
  const btn = document.getElementById("togglePassword");
  const field = document.getElementById("passwordField");
  if (!btn || !field) return;

  btn.addEventListener("click", function () {
    const isPass = field.getAttribute("type") === "password";
    field.setAttribute("type", isPass ? "text" : "password");

    const icon = btn.querySelector("i");
    if (icon) icon.className = isPass ? "bi bi-eye-slash" : "bi bi-eye";
  });
})();