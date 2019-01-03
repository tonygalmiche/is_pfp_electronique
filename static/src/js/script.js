
//Doc : https://www.odoo.com/documentation/10.0/howtos/web.html
//Doc : https://www.odoo.com/documentation/10.0/reference/javascript.html#openerp.Model.query


//TODO : Pour que les modifications sur ce fichier soient prise en compte, il faut activer le mode dévellopeur avec les assets


//Cette page est appellée au démarrage d'Odoo
console.log("Test 1bis");


//Cette fonction qui porte le même nom que le module est appellée au démarrage d'Odoo
openerp.is_pfp_electronique = function(instance, local) {

    console.log("Test 2");

    local.HomePage = instance.Widget.extend({
        template: "HomePageTemplate", // Permet de préciser le template QWeb à utiliser

        init: function(parent) {
            this._super(parent);
            this.name = "Mordecai";
        },

        //Cette fonction est appellée en cliquant sur le menu
        start: function() {
            var model = new instance.web.Model("ir.module.module");
            html='<h3>Version actuelle du logiciel</h3>';
            model.query(['name','installed_version'])
                .filter([['name','=','is_lf2016']])
                .all().then(function (data) {
                    $.each(data, function(k, v){
                        html+='<p>Version : '+v.installed_version+'</p>';
                    });
                model.call('lf2016',[[]],{}).then(function (data) {
                    html+='<h3>Clé de contrôle des modules installés</h3>';

                    html+="<p>Clé de contrôle : "+data+"</p>";
                    html+="<p><strong>ATTENTION : </strong>Si un module est installé, modifié ou supprimé cette clé de contrôle sera modifiée automatiquement et l'attestation de conformité ne sera plus valide !</p>";
                    html+='<h3>Modules installés</h3>';
                    model.query(['name','installed_version'])
                        .order_by('name', 'id')
                        .filter([['state','=','installed']])
                        .limit(1000)
                        .all().then(function (data) {
                            $.each(data, function(k, v){
                                console.log(k,v.name)
                                html+='- '+v.name+' ('+v.installed_version+')<br /> ';
                            });

                        $("#lf2016").html(html);
                    });
                });
            });







        },



    });




    //Cette ligne permet de déclarer la fonction précédente  et de faire le lien avec l'action Odoo 
    instance.web.client_actions.add('is_pfp_electronique.homepage', 'instance.is_pfp_electronique.HomePage');


}




