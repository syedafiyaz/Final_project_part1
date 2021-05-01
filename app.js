  
// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');
const { response } = require('express');
app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');


// index page
app.get('/', function(req, res) {
    
    //local API call to my Python REST API that delivers programming languages in dropdown
    axios.get(`https://cwrvx8v6xj.execute-api.us-east-2.amazonaws.com/default/apitest`)
    .then((response)=>{
        var languages = response.data;
        
        console.log(languages);
             // use res.render to load up an ejs view file
            res.render('pages/index', {
                languages: languages,
        
            });
        });
    });


// All programming languages page
app.get('/about', function(req, res) {
    
    //local API call to my Python REST API that delivers details of all programming languages
    axios.get(`https://cwrvx8v6xj.execute-api.us-east-2.amazonaws.com/default/apitest`)
    .then((response)=>{
      var languages = response.data;
    console.log(languages);
    // use res.render to load up an ejs view file on about page
    res.render('pages/about', {
        languages: languages,
    
        });
    });
}); 

app.post('/processdynamicform', function(req, res){
    //go directly to next.ejs and show dynamic language selection
    console.log(req.body)    
   // res.render to next.ejs page for the result of language selected  
    res.render('pages/next.ejs', {body: req.body})
});      

const port = 3000
app.listen(port, () => {
    console.log(`Front-end app listening at http://localhost:${port}`)
});