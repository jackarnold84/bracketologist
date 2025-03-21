// fetch data from APIs

const fetchAnalysisAPI = async (groupID) => {
    const apiUrl = `https://dz1ghyo6k7.execute-api.us-east-2.amazonaws.com/Prod/bracketologist/data/${groupID}`;

    return fetch(apiUrl,
        {
            'method': 'GET',
        }
    )
        .then(response => response.json())
        .catch(error => console.error(error))
};
