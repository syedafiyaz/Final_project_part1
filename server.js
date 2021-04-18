//Load express module
const express = require('express');
const path = require('path');

//Put new Express application inside app variable
const app = express();

//Set views property views engine
app.set("views", path.resolve(_dirname, "views"));
app.set("view engine", "ejs");

const port = 8080;

//When user hits the home page, then the message prints in browser.
app.get('/', (request, response) => response.render("hello", {
    message: "Welcome to express and ejs 'Hello Word' application"
})
);

// Start the express application on port 8080 and print server start message to console.
app.listen(port, () => console.log('Application started listening on port ${port}!'));
