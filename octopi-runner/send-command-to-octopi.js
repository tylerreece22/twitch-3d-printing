const myHeaders = new Headers();
myHeaders.append("X-Api-Key", "EFDC0E5BE0B04F0F83616701E367A5BB");
myHeaders.append("Content-Type", "application/json");


const sendCommand = (gcodeCommandList) => {
    const raw = JSON.stringify({
        commands: gcodeCommandList
    });

    const requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("http://octopi.local/api/printer/command", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

}

export default sendCommand