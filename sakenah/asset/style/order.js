function openPage(pageName,elmnt,color) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }
  document.getElementById(pageName).style.display = "block";
  elmnt.style.backgroundColor = color;
}

function pending() {
    var h1 = document.getElementById("highlighter1");
    var h2 = document.getElementById("highlighter2");
    h1.style.visibility = 'visible'
    h2.style.visibility = 'hidden'
}

function complete() {
    var h1 = document.getElementById("highlighter1");
    var h2 = document.getElementById("highlighter2");
    h1.style.visibility = 'hidden'
    h2.style.visibility = 'visible'

}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();