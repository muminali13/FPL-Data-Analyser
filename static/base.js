var linkClicked = document.getElementsByClassName('nav-link');
var numClass = linkClicked.length;

for (var i = 0; i < numClass; i++) {
    linkClicked[i].addEventListener('click', function () {
        var onTheMoment = document.getElementsByClassName('nav-active');
        onTheMoment[0].className = onTheMoment[0].className.replace(' nav-active', '');
        this.className += ' nav-active';
    }, false);
}