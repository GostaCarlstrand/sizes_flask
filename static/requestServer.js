function getPersons() {
    const Http = new XMLHttpRequest();
    const url = 'http://localhost:5000/js_data';
    Http.open("GET", url);
    Http.send();

    Http.onreadystatechange = (e) => {
        console.log(Http.responseText)
    }
}
