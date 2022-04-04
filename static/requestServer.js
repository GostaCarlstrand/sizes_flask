var objectSize;
function getPersons() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function () {
        let persons = JSON.parse(this.responseText);

        objectSize = Object.keys(persons).length
        for (let i = 0; i < objectSize; i++) {
            if (persons[i]['gender'] === 'Male') {
                getMaleSize(persons[i]['size_value'])
            } else {
                getFemaleSize(persons[i]['size_value'])
            }
        }
        drawChart()

    }
        xhttp.open('GET', "http://127.0.0.1:5000/js_data")
        xhttp.send()
}

function getMaleSize(size_value) {
    switch (size_value) {
        case 0:
            male_xs += 1;
            break;
        case 1:
            male_s += 1;
            break;
        case 2:
            male_m += 1;
            break;
        case 3:
            male_l += 1;
            break;
        case 4:
            male_xl += 1;
            break;
        case 5:
            male_xxl += 1;
            break;
    }
}
function getFemaleSize(size_value) {
    switch (size_value) {
        case 0:
            female_xs += 1;
            break;
        case 1:
            female_s += 1;
            break;
        case 2:
            female_m += 1;
            break;
        case 3:
            female_l += 1;
            break;
        case 4:
            female_xl += 1;
            break;
        case 5:
            female_xxl += 1;
            break;
    }
}



getPersons()