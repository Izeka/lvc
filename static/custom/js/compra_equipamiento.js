//funcion para calcular el monto total
function calc_total() {
  var sum = 0;

  $('.precio_unitario').each(function() {
    val = $(this).val();
    //si el valor del campo unitario es nulo, 0 ó NaN no ignoro
    if (!val || isNaN(val) || val == 0) {
      val;
      //sino los sumo a la variable sum
    } else {
      sum += parseInt(val);
    };
  });
  //asigno el valor de sum a id_importe_total
  $('#id_importe_total').val(function() {
    return sum;
  });
};

//Al iniciar llamo a la funcion para calcular el monto total
calc_total();

$(document).on('change', '.precio_unitario', function() {
  calc_total();
});
