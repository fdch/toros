const express = require("express");
const path = require("path");
const PORT = process.env.PORT || 3001;
const fileRead = require("./fileRead");
const app = express();
//const axios = require("axios");

//axios.get("https://fdch.ar/toros/static/js/main.bbabd07a.chunk.js")
//  .then(response => {
//    const Module = module.constructor;
//    const m = new Module();
//    m._compile(response.data, '');
//    console.log(m);
//   })
//  .catch(err => {
//    console.log("ERROR", err.code);
//  });


app.use(express.static(path.resolve(__dirname, '../frontend/build')));

app.get("/api", (req, res) => {
	res.json({ message: "Hi there" });
})

app.get("/people", (req, res, next) => {
  fileRead("./data/people.json", (content) => res.json(JSON.parse(content)));
});


app.get("*", (req, res) => {
	res.json({ message: "Server is up!" });
});

app.listen(PORT, () => {
	console.log(`Server listening on ${PORT}`);
});


