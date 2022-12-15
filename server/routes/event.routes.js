module.exports = app => {
  const events = require("../controllers/event.controller.js");

  var router = require("express").Router();

  // Create a new Tutorial
  router.post("/", events.create);

  // Retrieve all Tutorials
  router.get("/", events.findAll);

  // Retrieve all published Tutorials
  router.get("/upcoming", events.findAllUpcoming);

  // Retrieve a single Tutorial with id
  router.get("/:id", events.findOne);

  // Update a Tutorial with id
  router.put("/:id", events.update);

  // Delete a Tutorial with id
  router.delete("/:id", events.delete);

  // Delete all Tutorials
  router.delete("/", events.deleteAll);

  app.use('/api/events', router);
}
