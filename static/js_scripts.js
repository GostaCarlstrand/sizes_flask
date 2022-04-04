  const labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'My First dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(11, 85, 82)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }, {
        label: 'My First dataset',
      backgroundColor: 'rgb(255, 0, 0)',
      borderColor: 'rgb(11, 85, 82)',
      data: [10, 20, 5, 2, 20, 30, 45],

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

