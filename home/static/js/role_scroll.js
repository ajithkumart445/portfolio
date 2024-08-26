document.addEventListener('DOMContentLoaded',function(){
    const roleElement = document.getElementById('role');
    const roles = ['Full Stack Developer','Django Web Developer','Data Analyst'];
    const col = ['blue','red','green'];

    let index = 0;
    let colindex = 0;
    function showRole(){
        roleElement.textContent = roles[index]
        roleElement.style.opacity = '1';
        roleElement.style.color = col[colindex]

        setTimeout(()=>{
            roleElement.style.opacity = '0';
            index = (index + 1) % roles.length;
            colindex = (colindex + 1) % col.length
            showRole();
        },3000)

    }
    showRole();
});
