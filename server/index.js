const express = require("express");
const path = require("path");
const fs = require("fs");
const app = express();
const db = require("./models");
const cors = require("cors");

require("dotenv").config();

const corsOptions = {
	origin: process.env.CLIENT_ORIGIN || "http://localhost:8081"
};

app.use(cors(corsOptions));

app.use(express.json());

app.use(express.urlencoded({ extended: true }));

db.sequelize.sync({ force: true })
	.then(() => {
		console.log("Synced db.")
	})
	.catch((err) => {
		console.log("Failed to sync db: " + err.message)
	});

app.use(express.static(path.resolve(__dirname, '../client/build')));

app.get("/api", (req, res) => {
	res.json({ message: "Hi there" });
})

app.get("/people", (req, res) => {
	res.json({ message: "hi people"});
});

app.get("*", (req, res) => {
	res.json({ message: "Server is up!" });
});

require("./routes/event.routes")(app);

const PORT = process.env.NODE_DOCKER_PORT || 8080;

app.listen(PORT, () => {
	console.log(`Server listening on ${PORT}`);
});

