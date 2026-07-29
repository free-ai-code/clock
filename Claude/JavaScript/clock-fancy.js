// clock-fancy.js
const figlet = require('figlet');

setInterval(() => {
  const now = new Date();
  const timeString = `${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}:${String(now.getSeconds()).padStart(2, '0')}`;
  
  console.clear();
  console.log('\n');
  figlet(timeString, (err, data) => {
    if (!err) console.log(data);
  });
}, 1000);
