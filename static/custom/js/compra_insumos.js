function calc_total() {
  var sum = 0;

  $('.subtotal').each(function() {
    val = $(this).val();
    if (!val || isNaN(val) || val == 0) {
      val;
    } else {
      sum += parseInt(val); // Or this.innerHTML, this.innerText
    };
  });
  $('#id_importe_total').val(function() {
    return sum;
  });
};

calc_total();

$(document).on('change', '.precio_unitario', function() {
  var pu = $(this).val();
  var q = $(this).closest("tr").find('.cantidad').val();
  var sub = pu * q;
  $(this).closest("tr").find('.subtotal').val(function() {
    return sub;
  });
  calc_total();
});

$(document).on('change', '.cantidad', function() {
  var q = $(this).val();
  var pu = $(this).closest("tr").find('.precio_unitario').val();
  var sub = pu * q;
  $(this).closest("tr").find('.subtotal').val(function() {

    return sub;
  });
  calc_total();
});

$(document).on('change', '.subtotal', function() {
  var pu = $(this).val();
  var q = $(this).closest("tr").find('.cantidad').val();
  var sub = pu * q;
  $(this).closest("tr").find('.subtotal').val(function() {
    return sub;
  });
  calc_total();
});
