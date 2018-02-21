function oferta(){
 fecha=new Date(2018,02,28,0,0,0); //año,mes,dia,hora,minuto,segundo
  ahora=new Date();
  dif=new Date(fecha-ahora);
  txt='Las ofertas terminan en: '+dif.getDate()+' días, '+dif.getHours()+' horas, ';
  txt+=+dif.getMinutes()+' minutos y '+dif.getSeconds()+' segundos';
  document.getElementById('oferta').innerHTML=txt;
}
function aviso(){
  alert("Pedido realizado. Gracias por su compra")
}

