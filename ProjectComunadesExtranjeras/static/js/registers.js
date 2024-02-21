function  cambiarColorPulsera(){
    const selectoresPulsera = document.getElementsByClassName("tipo-pulsera");
    const colores = ['#FFFFFF','#F8F545','#fd7e14','#56D95B','#3AB4E3','#EF7AD3','#B406F2']
    for (let i = 0; i < selectoresPulsera.length; i++) {
        selectoresPulsera[i].addEventListener("change", () => {
            const selectedOption = selectoresPulsera[i].options[selectoresPulsera[i].selectedIndex]; 
            selectoresPulsera[i].style.setProperty("background-color",`${colores[selectedOption.value]}`,"important");
            if(selectedOption.value == "2" || selectedOption.value == "6"){
                selectoresPulsera[i].style.color = "#FFFFFF";
            }else{
                selectoresPulsera[i].style.color = "#000000";
            }
        });
    }
}

document.addEventListener("DOMContentLoaded", () => {
    cambiarColorPulsera()
})

