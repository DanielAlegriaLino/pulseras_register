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

function asignarPulsera(){
    const colores = ['#FFFFFF','#F8F545','#fd7e14','#56D95B','#3AB4E3','#EF7AD3','#B406F2']
    const tableRows = document.getElementsByTagName("tr");
    const selectedBracelet = document.getElementsByClassName("tipo-pulsera");
    for(let i = 0; i < selectedBracelet.length; i++){
        selectedBracelet[i].style.setProperty("background-color",`${colores[selectedBracelet[i].value]}`,"important");
        if(selectedBracelet[i].value == "2" || selectedBracelet[i].value == "6"){
            selectedBracelet[i].style.color = "#FFFFFF";
        }else{
            selectedBracelet[i].style.color = "#000000";
        }

        if(selectedBracelet[i].value != "0"){
            tableRows[i+1].classList.add("assigned");
        }
    }
}

function filterAssigned(){
    const btn = document.getElementById('filter-btn');
    btn.addEventListener("click", () => {
        const rows = document.getElementsByTagName("tr");
        for(let i = 1; i < rows.length; i++){
            if(rows[i].classList.contains("assigned")){
                rows[i].style.display = "none";
            }
        }
    })
}

function toggleOrder(){
    const toggleButtons = document.querySelectorAll('.sort-btn');
    console.log(typeof(toggleButtons));
    toggleButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const symbol = btn.getElementsByTagName("i");
            symbol[0].classList.toggle("fa-arrow-down-a-z");
            symbol[0].classList.toggle("fa-arrow-up-a-z");
        })
    })
}

document.addEventListener("DOMContentLoaded", () => {
    asignarPulsera();
    cambiarColorPulsera();
    filterAssigned();
    toggleOrder();
})

