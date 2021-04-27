// load the things we need
var express = require('express');
var app = express();

// required module to make calls to a REST API
const axios = require('axios');
const { response } = require('express');

// set the view engine to ejs
app.set('view engine', 'ejs');

// index page
app.get('/', function(req, res) {
    res.render('pages/index');
});


// result page
app.get('/result', function(req, res) {
    
//local API call to my Python REST API that delivers languages
axios.get(`https://cwrvx8v6xj.execute-api.us-east-2.amazonaws.com/default/apitest`)
.then((response)=>{
    var languages = response.data;
    
    console.log(languages);
         // use res.render to load up an ejs view file
        res.render('pages/result', {
            languages: languages,
    
        });
    });
});

const port = 3000
app.listen(port, () => {
    console.log(`Front-end app listening at http://localhost:${port}`)
});
