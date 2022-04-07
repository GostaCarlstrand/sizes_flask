  var female_xs = 0;
  var male_xs = 0;
  var female_s = 0;
  var male_s = 0;
  var female_m = 0;
  var male_m = 0;
  var female_l = 0;
  var male_l = 0;
  var female_xl = 0;
  var male_xl = 0;
  var female_xxl = 0;
  var male_xxl = 0;



function drawChart() {
  const labels = [
    'XS',
    'S',
    'M',
    'L',
    'XL',
    'XXL',
  ];

  const data = {


    labels: labels,
    datasets: [{
      label: 'Females',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(11, 85, 82)',
      data: [female_xs, female_s, female_m, female_l, female_xl, female_xxl, objectSize],
    }, {
      label: 'Males',
      backgroundColor: 'rgb(255, 0, 0)',
      borderColor: 'rgb(11, 85, 82)',
      data: [male_xs, male_s, male_m, male_l, male_xl, male_xxl, objectSize],

    }]
  };

  const config = {
    type: 'bar',
    data: data,
    options: {}
  };

  const myChart = new Chart(
      document.getElementById('myChart'),
      config
  );
}




