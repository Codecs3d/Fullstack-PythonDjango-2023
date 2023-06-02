function showchild(element) {
    element.children[0].style.display = 'block';
};
function hiddenchild(element) {
    element.children[0].style.display = 'none';
};


var select = document.getElementById("id_region");

select.addEventListener("change", function () {
    var ocultar = document.querySelectorAll("#comuna-container select");
    for (var i = 0; i < ocultar.length; i++) {
        ocultar[i].setAttribute("style", "display:none")
    }
    document.getElementById(select.value).setAttribute("style", "display:block")
});


function reload() {
    location.reload();
}