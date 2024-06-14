document.addEventListener("DOMContentLoaded", function() {
    const questionInput = document.getElementById("question");
    questionInput.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            event.preventDefault(); // 기본 엔터 동작 방지
            // 폼 전송
            document.querySelector("form").submit();
        }
    });
});
window.onload = function() {
    var questionInput = document.getElementById("question");
    questionInput.value = ""; // 검색창 비우기
    questionInput.focus(); // 검색창에 포커스 맞추기
}