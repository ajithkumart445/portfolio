 
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
    
//    // this is for smooth scrolling in page
//     $('a[href^=\\#]').on('click',function(event){
//         event.preventDefault();
//         $('html,body').animate({scrollTop:$(this.hash).offset().top}, 5000);
//     });

//     $(document).ready(function(){
//         $('html,body').animate({scrollTop:$(location.hash).offset().top}, 5000);
//     });


   