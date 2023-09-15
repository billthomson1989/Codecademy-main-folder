<!DOCTYPE html>
<html lang="en">
<body>

<div onmouseover="mOver(this)"
onmouseout="mOut(this)"
style="background-color:blue;width:120px;height:20px;padding:40px;">Mouse Over Me</div>







<script>
function mOver(obj) {
    obj.innerHTML = "Thank You"
}

function mOut(obj) {
    obj.innerHTML = "Mouse Over Me"
}
</script>

<var myImage = document.getElementById("image.jpeg");

var imageArray = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg"] 

var imageIndex = 0; 

function changeImage () {
    myImage.setAttribute("src", imageArray[imageIndex]);
    imageIndex++;
    if(imageIndex >= imageArray.length) {
        imageIndex = 0;
    }
}

setInterval((changeImage, 5000) => {
    
}, interval);


</body>
</html>