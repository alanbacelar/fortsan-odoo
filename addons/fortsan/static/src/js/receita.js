var btn2 = document.getElementById("form");
var btn = document.getElementById("btnCreditos");
btn.onclick = function () {
  console.log("Cheguei");
};
btn2.onsubmit = function (event) {
  var cnpj = document.getElementById("cnpj").value;
  var segmento = document.getElementById("segmento").value;
  var cnae = document.getElementById("cnae").value;
  var municipio = document.getElementById("municipio").value;
  var uf = document.getElementById("uf").value;
  var limit = document.getElementById("limit").value || 100;

  var urls = "http://" + window.location.host + "/fortsan/receita/";

  fetch(urls, {
    method: "post",
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
    },
    body: JSON.stringify({
      jsonrpc: "2.0",
      params: {
        cnpj: cnpj,
        cnpj,
        segmento,
        cnae,
        municipio,
        uf,
        limit,
      },
    }),
  })
    .then((res) => res.json())
    .then((res) => console.log(res));
};
