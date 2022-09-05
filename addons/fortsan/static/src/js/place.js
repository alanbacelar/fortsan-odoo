var modal = document.getElementById("modal-Error");
var span = document.getElementsByClassName("close")[0];


        // When the user clicks the button, open the modal 
        function openModelError(value) {
            if(value['estado'] == "" && value['cidade'] == "" && value['longitude'] == "" && value['latitude'] == ""){
                modal.style.display = "block";
                return false;
            }else{
                modal.style.display = "none";
                return true;
            }
        }

        span.onclick = function closeModelError () {
            modal.style.display = "none";
        }

        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }

var btn2 = document.getElementById("form");
        var btn = document.getElementById("btnCreditos");
        btn.onclick = function () {
            console.log("Cheguei");
        }
        btn2.onsubmit = function (event) {
            var palavchav = document.getElementById('palavchav').value
            var disBusca = document.getElementById('disBusca').value
            var latitude = document.getElementById('latitude').value
            var longitude = document.getElementById('longitude').value
            var cidade = document.getElementById('cidade').value
            var estado = document.getElementById('estado').value

            var urls = 'http://' + window.location.host + '/fortsan/fortsan/'
            value = {
                palavchav: palavchav,
                disBusca: disBusca,
                latitude: latitude,
                longitude: longitude,
                cidade: cidade,
                estado: estado
            }
            if (openModelError(value)){
                fetch(urls, {
                        method: 'post',
                        headers: {
                            'Content-Type': 'application/json; charset=UTF-8'
                        },
                        body: JSON.stringify({
                            "jsonrpc": "2.0",
                            "params": {
                                palavchav: palavchav,
                                disBusca: disBusca,
                                latitude: latitude,
                                longitude: longitude,
                                cidade: cidade,
                                estado: estado
                            }
                        })
                    }).then(res => res.json())
                    .then(res => console.log(res));
            }else{
                event.preventDefault();
            }
        }



        var arrow = document.getElementById("arrow-img");
        var hiddemLatlng = document.getElementById("lat-lng");
        var btnLatlng = document.getElementById("btn-click-lat");

        btnLatlng.onclick = () => viewAction("view", "hiddem", "icon-arrow-x", "icon-arrow");

        var arrowCidEst = document.getElementById("arrow-img-1");
        var hiddemCidEst = document.getElementById("cid-est");
        var btnCidEst = document.getElementById("btn-click-cid-est");

        btnCidEst.onclick = () => viewAction("view-1", "hiddem-1", "icon-arrow-x-1", "icon-arrow-1");

        function viewAction(view, hiddem, viewArrow, hiddemArrow, ) {
            if (hiddemCidEst.classList[0] === view || hiddemLatlng.classList[0] === view) {
                var current = document.getElementsByClassName(view);
                current[0].className = current[0].className.replace(view, hiddem);

                var currentIcon = document.getElementsByClassName(viewArrow);
                currentIcon[0].className = currentIcon[0].className.replace(viewArrow, hiddemArrow);
            } else {
                var current = document.getElementsByClassName(hiddem);
                current[0].className = current[0].className.replace(hiddem, view);

                var currentIcon = document.getElementsByClassName(hiddemArrow);
                currentIcon[0].className = currentIcon[0].className.replace(hiddemArrow, viewArrow);
            }
        }

