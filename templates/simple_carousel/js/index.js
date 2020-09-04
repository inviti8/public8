ACTIVE_IMG = null;
window.fn = {};

window.fn.open = function() {
var menu = document.getElementById('menu');
menu.open();
};

window.fn.chapterOnClick = function(el) {

    var carousel = document.getElementById('AppCarousel');
    var countFab = document.getElementById('pageCountFab');
    var split = el.id.split("_");
    var index = parseInt(split[1]);

    carousel.setActiveIndex(index);
    countFab.innerHTML = '<p style="text-align: center; font-size: 1.7vh;"> ' + index + '</p>';
    
}

var prev = function() {
  var carousel = document.getElementById('AppCarousel');
  carousel.prev();
};

var next = function() {
  var carousel = document.getElementById('AppCarousel');
  carousel.next();
};

var setPageIndex = function(index) {
  var carousel = document.getElementById('AppCarousel');
  carousel.setPageIndex(index);
};

ons.ready(function() {
  var carousel = document.addEventListener('postchange', function(event) {
    var countFab = document.getElementById('pageCountFab');
    var activeImg = document.getElementById('img_' + event.activeIndex);
    ACTIVE_IMG = activeImg;
    console.log(activeImg)
    console.log('Changed to ' + event.activeIndex)
    countFab.innerHTML = '<p style="text-align: center; font-size: 1em;"> ' + event.activeIndex + '</p>';

    var images = document.getElementsByClassName("img");

    for (i = 0; i < images.length; i++) {
      var img = images[i];
      img.setAttribute('onclick','fn.imgOnClick(this)');
    }
  });
});

window.fn.imgOnClick = function(el) {

console.log(el)

var setImageContent = function()
{
    var container = document.getElementById('img-dialog-container');
    var img = document.getElementById(el.id);
    container.innerHTML = '<img id="thumb" class="magnifier-large hidden" data-mode="inside" data-zoomable="true" src= ' + img.src + ' style= " display: block;  margin-top: 20vh; margin-left: auto; margin-right: auto; width: 90%;"></img>';
    var evt = new Event(),
    m = new Magnifier(evt);
    m.attach({
      thumb: '#thumb',
      large: img.src,
      mode: 'inside',
      zoom: 3,
      zoomable: true
    });
}

var showImgDialog = function() {
var dialog = document.getElementById('img-dialog');

  if (dialog) {
      dialog.show();
      setImageContent();
    } else {
    ons.createElement('img-dialog.html', { append: true })
      .then(function(dialog) {
        dialog.show();
        setImageContent();
      });
    }

    var container = document.getElementById('img-dialog-container');
  }
  showImgDialog();
}

var hideDialog = function(id) {
    document
      .getElementById(id)
      .hide();
};

window.fn.load = function(page) {
var content = document.getElementById('content');
var menu = document.getElementById('menu');
content.load(page)
    .then(menu.close.bind(menu));
};