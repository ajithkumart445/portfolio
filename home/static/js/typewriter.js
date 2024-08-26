 


const historyText = document.getElementById('hist-text');
const text = historyText.textContent.trim();
historyText.textContent = '';
    
let charIndex = 0;
typeWriter();
function typeWriter() {
if (charIndex < text.length) {
    historyText.textContent += text.charAt(charIndex);
    charIndex++;
    setTimeout(typeWriter,225); // Reduce the typing speed to make it even faster (milliseconds)
    } 
}