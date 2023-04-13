console.log("hello")

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const handleRedirect = (data) => {
    if (data["redirect"]) {
        location.href=data["url"]
    }
}



const ApiCall = (event_id,party_id) => {
    const postData = {
        party_id,
    };

    window.fetch(`/vote-page/${event_id}`, {
        method: 'POST',
        body: JSON.stringify(postData),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
    }).then(response => {
        if (response.status === 200) {
            response.json().then(data => {
                    console.log(data)
                    handleRedirect(data)
            })
        } else {
            response.json().then(x => {
                console.log(x)
            });
        }
    }).catch(() => {

    });
}









const handleOnLoad = () => {

const vote_btns= document.querySelectorAll(".vote-btn")
for (var i=0;i<vote_btns.length;i++){
    vote_btns[i].addEventListener("click",(e)=>{
        const event_id=e.target.getAttribute("data-event")
        const party_id=e.target.getAttribute("data-party")
        ApiCall(event_id,party_id)
    })
}

}




document.addEventListener('DOMContentLoaded', handleOnLoad, false);