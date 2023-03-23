// fetch data from APIs

const fetchAnalysisAPI = async (groupID) => {
    const apiUrl = 'https://71c9c860jj.execute-api.us-east-2.amazonaws.com/default/bracketFetch';

    return fetch(apiUrl + '?' + new URLSearchParams(
        {
            'groupID': groupID,
        }
    ),
        {
            'method': 'POST',
        }
    )
        .then(response => response.json())
        .catch(error => console.warn(error))
};


const bracketAnalysisAPI = async (token, groupID, limit) => {
    const apiUrl = 'https://71c9c860jj.execute-api.us-east-2.amazonaws.com/default/bracketAnalysis';
    limit = limit || '';

    return fetch(apiUrl + '?' + new URLSearchParams(
        {
            'groupID': groupID,
            'limit': limit,
        }
    ),
        {
            'method': 'POST',
            'body': JSON.stringify({ 'auth': { 'token': token } }),
        }
    )
        .then(response => response.json())
        .catch(error => console.warn(error))
};


const checkAuthAPI = async (token) => {
    // returns returns {'authorized': bool}
    const apiUrl = 'https://71c9c860jj.execute-api.us-east-2.amazonaws.com/default/bracketAnalysis';

    return fetch(apiUrl + '?' + new URLSearchParams(
        {
            'auth': 'checkAuth',
        }
    ),
        {
            'method': 'POST',
            'body': JSON.stringify({ 'auth': { 'token': token } }),
        }
    )
        .then(response => response.json())
        .catch(error => console.warn(error))
};


const requestAuthTokenAPI = async (password) => {
    // returns {'authorized': bool, 'token': string}
    const apiUrl = 'https://71c9c860jj.execute-api.us-east-2.amazonaws.com/default/bracketAnalysis';

    return fetch(apiUrl + '?' + new URLSearchParams(
        {
            'auth': 'requestAuth',
        }
    ),
        {
            'method': 'POST',
            'body': JSON.stringify({ 'auth': { 'password': password } }),
        }
    )
        .then(response => response.json())
        .catch(error => console.warn(error))
};
