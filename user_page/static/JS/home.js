$(function () {
    $('#branchselector').change(function(){
    $('.subject').hide();
    $('#' + $(this).val()).show();
    });
    });

    function showDiv(second,third,fourth,result,element)
    {
      var x = document.getElementById("second");
      var y = document.getElementById("third");
      var q = document.getElementById("fourth");
      var z = document.getElementById("result");
       x.style.display = element.value !='none' ? 'block' : 'none';
      y.style.display = element.value !='none' ? 'block' : 'none';
     z.style.display = element.value !='none' ? 'block' : 'none';
      q.style.display = element.value !='none' ? 'block' : 'none';
    }


  function myFunction() {
    var x = document.getElementById("checkbox1").value;
    document.getElementById("textbox1").innerHTML = x;
    // var x = document.getElementById("checkbox2").value;
    // document.getElementById("textbox2").innerHTML = x;
    // var x = document.getElementById("checkbox3").value;
    // document.getElementById("textbox3").innerHTML = x;
    // var x = document.getElementById("checkbox4").value;
    // document.getElementById("textbox1").innerHTML = x;
    // var x = document.getElementById("checkbox4").value;
    // document.getElementById("textbox1").innerHTML = x;
  }


// $(document).ready(function() {
//
//     // Set initial state
// $('#textbox1').val($(this).is(':checked'));
// $('#p1').click(function() {
//   $('#textbox1').val($(this).is(':checked'));
//
// $('#textbox2').val($(this).is(':checked'));
// $('#p2').click(function() {
//   $('#textbox2').val($(this).is(':checked'));
//
// $('#textbox3').val($(this).is(':checked'));
// $('#p3').click(function() {
//   $('#textbox3').val($(this).is(':checked'));
//
// $('#textbox4').val($(this).is(':checked'));
// $('#p4').click(function() {
//   $('#textbox4').val($(this).is(':checked'));
//
// $('#textbox5').val($(this).is(':checked'));
// $('#p5').click(function() {
//   $('#textbox5').val($(this).is(':checked'));
//     });
// });
