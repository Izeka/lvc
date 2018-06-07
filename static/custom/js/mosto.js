calc_total();

moment.locale('es');
$('#id_fecha_compra').daterangepicker({
   singleDatePicker: true,
});

 $('.add-row').addClass("fa fa-toggle-down");

 $(document).on('change', '.precio_unitario', function() {
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
     var pu = $(this).closest("tr").find('.precio_unitario').val();
     var sub = pu*q;
     $(this).closest("tr").find('.subtotal').val(function(){

         return sub;
     });
  //   calc_total();
 });

 $( document ).ready(function() {
    //calc_total();
 });
 function calc_total() {
      var sum = 0;

      $('.subtotal').each(function(){
        val = $(this).val();
        if(!val || isNaN(val) || val == 0) {
           val;
       } else{
          sum += parseInt(val);  // Or this.innerHTML, this.innerText
        };
      });
      $('#id_importe_total').val(function(){
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
