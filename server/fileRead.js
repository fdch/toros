const fs = require('fs');
const util = require('util');
const readFileContent = util.promisify(fs.readFile);


module.exports = (filePath, callback) => {
  readFileContent(filePath)
    .then(buffer => {
      const contents = buffer.toString();
      callback(contents);
    })
    .catch(err => {
      console.log(`Error reading file: ${filePath}, Error code: ${err.code}`);
    });
};

