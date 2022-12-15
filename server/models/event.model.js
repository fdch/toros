module.exports = (sequelize, Sequelize) => {
	const Event = sequelize.define("event", {
		name: {
			type: Sequelize.STRING
		},
		date: {
			type: Sequelize.DATE
		},
		place: {
			type: Sequelize.STRING
		},
		description: {
			type: Sequelize.STRING
		},
		url: {
			type: Sequelize.STRING
		}
	});
};
