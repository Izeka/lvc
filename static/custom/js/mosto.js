
moment.locale('es');
$('#id_fecha_compra,#id_fecha').daterangepicker({
   singleDatePicker: true,
   dateFormat: 'dd/mm/yy',
   regional: 'es'
});

$('.add-row').addClass("fa fa-toggle-down");

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
