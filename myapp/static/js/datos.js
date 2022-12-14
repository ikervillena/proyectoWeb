var obj = [
    {
        "nombre": "Marina",
        "usuario": "marinaojinaga",
        "contrasenya": "1234",
        "email": "marinaojinaga@opendeusto.es",
        "productos_guardados": []
    },
    {
        "nombre": "Malen Sanz",
        "usuario": "malensanz",
        "contrasenya": "malensanz",
        "email": "malensanz@gmail.com",
        "productos_guardados": []
    },
    {
        "nombre": "Maria Santizo",
        "usuario": "mariasantizo",
        "contrasenya": "mariasantizo",
        "email": "maria@gmail.com",
        "productos_guardados": []
    },
    {
     
        "nombre": "Ane Garcia",
        "usuario": "anegarcia",
        "contrasenya": "ane1234",
        "email": "ane@gmail.com",
        "productos_guardados": []
    },
    {
      
        "nombre": "Asier Olaizola",
        "usuario": "asier",
        "contrasenya": "asier",
        "email": "asier@gmail.com",
        "productos_guardados": []
    },
    {
        "nombre": "ainhoa",
        "usuario": "ainhoa",
        "contrasenya": "ainhoa",
        "email": "ainhoa@gmail.com",
        "productos_guardados": []
    },
    {
        "nombre": "Andres",
        "usuario": "andres",
        "contrasenya": "1234",
        "email": "andres@gmail.com",
        "productos_guardados": []
    },
]

function comprobar(){
    var json = JSON.parse(obj);
    for (x of json){
        if(id_usuario==x.usuario){
            if(id_contrasenya==x.contrasenya){
                alert("Estas dentro!!");
            }
        }
    }
}

function darBoton(){
    var el = document.getElementById("inicioSesionPrueba");
    el.addEventListener("click",comprobar);
}

function saludar(){
    alert("Hola");
}

function boton(){
    var el=document.getElementById("inicioSesionPrueba");
    el.addEventListener("click",saludar,false);
}