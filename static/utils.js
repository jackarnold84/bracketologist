// Common javascript utilities

//  sleep utility

const sleep = (sec) => {
    return new Promise(resolve => setTimeout(resolve, sec * 1000));
};


// array utilities

const sum = (arr) => arr.reduce((a, b) => a + b, 0);

const removeDuplcates = (arr) => [...new Set(arr)]

const sortNumericArr = (arr) => arr.sort((a, b) => a - b);


// date time utilities

const getEpochTime = () => Date.now() / 1000;

const epochTimeToDate = (epochTimestamp) => {
    return new Date(epochTimestamp * 1000);
};

const formatDate = (date, type) => {
    // type: date, dateWithYear, textDate, time, weekday
    if (type == undefined) {
        // 3/3/2023, 11:36:24 AM
        return date.toLocaleString('en-US');
    } else if (type === 'date') {
        // 3/3
        return date.toLocaleString('en-US', { month: 'numeric', day: 'numeric' });
    } else if (type === 'dateWithYear') {
        // 3/3/2023
        return date.toLocaleString('en-US', { month: 'numeric', day: 'numeric', year: 'numeric' });
    } else if (type === 'textDate') {
        // Mar 3
        return date.toLocaleString('en-US', { month: 'short', day: 'numeric' });
    } else if (type === 'time') {
        // 11:36 AM
        return date.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric' });
    } else if (type === 'weekday') {
        // Fri
        return date.toLocaleString('en-US', { weekday: 'short' });
    } else {
        return date.toLocaleString('en-US');
    }
};
