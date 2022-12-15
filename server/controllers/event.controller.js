const db = require("../models");
const Event = db.events;
const Op = db.Sequelize.Op;
const NOW = new Date();

exports.create = (req, res) => {
  // validate request
  if (!req.body.title) {
    res.status(400).send({
message: "Content cannot be empty!"
});
return;
}

// create an Event
const event = {
name: req.body.name,
      date: req.body.date,
      description: req.body.description,
      place: req.body.place,
      url: req.body.url
};

//save it in the db
Event.create(event)
  .then(data => {
      res.send(data);
      })
.catch(err => {
    res.status(500).send({
message:
err.message || "there was an error creating Event"
});
    });
};

exports.findAll = (req, res) => {
  const place = req.query.place;
  var condition = place ? { place: { [Op.like]: `%${place}%` } } : null;

  Event.findAll({ where: condition })
    .then(data => {
        res.send(data);
        })
  .catch(err => {
      res.status(500).send({
message:
err.message || "Some error occurred while retrieving events."
});
      });
};

exports.findOne = (req, res) => {
  const id = req.params.id;

  Event.findByPk(id)
    .then(data => {
        if (data) {
        res.send(data);
        } else {
        res.status(404).send({
message: `Cannot find Event with id=${id}.`
});
        }
        })
.catch(err => {
    res.status(500).send({
message: "Error retrieving Event with id=" + id
});
    });
};

exports.update = (req, res) => {
  const id = req.params.id;

  Event.update(req.body, {
where: { id: id }
})
.then(num => {
    if (num == 1) {
    res.send({
message: "Event was updated successfully."
});
    } else {
    res.send({
message: `Cannot update Event with id=${id}. Maybe Event was not found or req.body is empty!`
});
    }
    })
.catch(err => {
    res.status(500).send({
message: "Error updating Event with id=" + id
});
    });
};

exports.delete = (req, res) => {
  const id = req.params.id;

  Event.destroy({
where: { id: id }
})
.then(num => {
    if (num == 1) {
    res.send({
message: "Event was deleted successfully!"
});
    } else {
    res.send({
message: `Cannot delete Event with id=${id}. Maybe Event was not found!`
});
    }
    })
.catch(err => {
    res.status(500).send({
message: "Could not delete Event with id=" + id
});
    });
};

exports.deleteAll = (req, res) => {
  Event.destroy({
where: {},
truncate: false
})
.then(nums => {
    res.send({ message: `${nums} Events were deleted successfully!` });
    })
.catch(err => {
    res.status(500).send({
message:
err.message || "Some error occurred while removing all tutorials."
});
    });
};

exports.findAllUpcoming = (req, res) => {
  Event.findAll({ where: { 
published: { 
[Op.ge]: NOW

}
} })
.then(data => {
    res.send(data);
    })
.catch(err => {
    res.status(500).send({
message:
err.message || "Some error occurred while retrieving tutorials."
});
    });
};
