odoo.define('om_hospital.teste', function(require) {
    'use strict';
    var web = require('web.dom.ready');

    alert("Antes do javascript");
    console.log(web);
    alert("Depois do javascript");

});