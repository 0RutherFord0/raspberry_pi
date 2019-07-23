function myFunction() {
    var x = document.getElementsByClassName("slider");
    if (x.innerHTML === "LED IS OFF") {
      x.innerHTML = "LED IS ON";
    } else {
      x.innerHTML = "LED IS OFF";
    }
  }
