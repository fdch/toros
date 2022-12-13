const express = require("express");

const PORT = process.env.PORT || 3001;

const app = express();

app.use(express.static(path.resolve(__dirname, '../client/build')));

app.get("/api", (req, res) => {
	res.json({ message: "Hi there" });
})

app.get("*", (req, res) => {
	res.json({ message: "Server is up!" });
});

app.listen(PORT, () => {
	console.log(`Server listening on ${PORT}`);
});

