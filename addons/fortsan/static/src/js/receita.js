var btn2 = document.getElementById("form");
        var btn = document.getElementById("btnCreditos");
        btn.onclick = function () {
            console.log("Cheguei");
        }
        btn2.onsubmit = function (event) {
            var cnpj = document.getElementById('cnpj').value

            var urls = 'http://' + window.location.host + '/fortsan/receita/'


            // event.preventDefault();
            console.log(event);
            console.log(urls);
            console.log({
                cnpj
            });

            fetch(urls, {
                    method: 'post',
                    headers: {
                        'Content-Type': 'application/json; charset=UTF-8'
                    },
                    body: JSON.stringify({
                        "jsonrpc": "2.0",
                        "params": {
                            cnpj: cnpj,
                        }
                    })
                }).then(res => res.json())
                .then(res => console.log(res));
        }