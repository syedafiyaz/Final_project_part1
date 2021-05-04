  
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
    
    //local API call to my Python REST API that delivers list of friends from database
    axios.get(`http://127.0.0.1:5000/api/friend/all`)
    
    .then((response)=>{
        var friends = response.data;
        
        console.log(friends);
             // use res.render to load up an ejs view file
            res.render('pages/index', {
                friends: friends,
        
            });
        });
    });

// All friends movielist page
app.get('/about', function(req, res) {
    
    //local API call to my Python REST API that delivers list of all movies
    axios.get(`http://127.0.0.1:5000/api/movielist/all`)
    .then((response)=>{
      var movielists = response.data;
    console.log(movielists);
    // use res.render to load up an ejs view file on about page
    res.render('pages/about', {
        movielists: movielists,
    
        });
    });
}); 



app.post('/processdynamicform', function(req, res) {
    //go directly to next.ejs and show dynamic friends selection
    console.log(req.body)    
   // res.render to next.ejs page for the result of friends selected  
    res.render('pages/next.ejs', {body: req.body})
});      



const port = 3000
app.listen(port, () => {
    console.log(`Front-end app listening at http://localhost:${port}`)
});