/* Global JSON formats */

const STATIC_INFO = {
    user_agent : undefined,
    language : undefined,
    accepts_cookies : undefined,
    js_enabled : true,
    images_enabled : undefined,
    css_enabled : undefined,
    screen_height : undefined,
    screen_width : undefined,
    window_height : undefined,
    window_width : undefined,
    network_type : undefined
}

/* Init */
init()

function init() {
    getStaticInfo();
    sendPacket(STATIC_INFO, "static");
}

//sends packet to endpoint with the appropriate type
async function sendPacket(packet, type) {
    var url = "https://michaeltam.site/json/" + type;

    fetch(url , {
        headers : {
            'Authorization': 'Basic dXNlcjp1c2Vy',
            'Content-Type': 'application/json'
        },
        method : 'POST',
        body : JSON.stringify(packet)
    })
    .then(response => response.json())
    .then(data => alert(data));
}

function getStaticInfo() {
    STATIC_INFO.user_agent = window.navigator.userAgent;
    STATIC_INFO.language = window.navigator.language;
    STATIC_INFO.accepts_cookies = window.navigator.cookieEnabled;
    STATIC_INFO.network_type = window.navigator.connection.type;
    
    STATIC_INFO.screen_height = window.screen.height;
    STATIC_INFO.screen_width = window.screen.width;
    STATIC_INFO.window_height = window.outerHeight;
    STATIC_INFO.window_width = window.outerWidth;

    //assumed true
    //STATIC_INFO.js_enabled = true;
    STATIC_INFO.css_enabled = "TODO";

    var image = new Image();
    image.onload = function() {
        STATIC_INFO.images_enabled = (image.width > 0) ? true : false;
    }
    image.src = 'clear_px.gif'
}

function getActivityData(closed) {
    
}







/*
var start = new Date();

//one minute
var period_length = 60000;

while (true) {
    var time_elapsed = new Date() - start;
    if (time_elapsed > period_length) {
        getActivityData(false);
    }
}
getActivityData(true);
*/