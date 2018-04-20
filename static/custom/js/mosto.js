calc_total();

$('#id_Fecha_compra').datepicker({
 dateFormat: 'dd/mm/yy',
   regional: 'es'
});

 $('.add-row').addClass("fa fa-toggle-down");

 $(document).on('change', '.p_unitario', function() {
     var pu  = $(this).val();
     var q = $(this).closest("tr").find('.cantidad').val();
     var sub = pu*q;
     $(this).closest("tr").find('.subtotal').val(function(){
         return sub;
     });
     calc_total();
 });

 $(document).on('change', '.cantidad', function() {
     var q  = $(this).val();
     var pu = $(this).closest("tr").find('.p_unitario').val();
     var sub = pu*q;
     $(this).closest("tr").find('.subtotal').val(function(){

         return sub;
     });
     calc_total();
 });

function calc_total() {
     var sum = 0;
     $('.subtotal').each(function(){
       sum += parseInt(this.value);  // Or this.innerHTML, this.innerText
     });
     $('#id_Importe_Total').val(function(){
         return sum;
     });
 };


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

$('#id_Lleno,#id_Carbonatado').addClass("icheckbox_flat-blue");
