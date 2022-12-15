module.exports = (sequelize, Sequelize) => {
	const People = sequelize.define("people", {
		name: {
			type: Sequelize.STRING
		},
		lastname: {
			type: Sequelize.STRING
		},
		url: {
			type: Sequelize.STRING
		},
		bio: {
			type: Sequelize.STRING
		},
	});
};
