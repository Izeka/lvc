// Llama al plugin para seleccionar fecha
$('#id_fecha_compra,#id_fecha').daterangepicker({
   singleDatePicker: true,
   locale: {
     format: 'DD/MM/YYYY'
},
   regional: 'es'
});

//agrega clase al boton "agregar linea" en los formsets
$('.add-row').addClass("fa fa-toggle-down");

//activa el modal
$('#modal').on('show.bs.modal', function (event) {
   var modal = $(this);
   var url = $(event.relatedTarget).attr('href');
   $.ajax({
       url: url,
       context: document.body
   }).done(function(response) {
       modal.html(response);
   });
});

//deshabilita el incremento de inputs del tipo número con el mouse
$(document).on("wheel", "input[type=number]", function (e) {
    $(this).blur();
});
