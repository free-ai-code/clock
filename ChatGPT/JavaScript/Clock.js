function pad(n) {
  return String(n).padStart(2, "0");
}

function drawClock() {
  const now = new Date();
  const time = `${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;

  process.stdout.write("\x1Bc"); // 画面クリア
  console.log("デジタル時計");
  console.log("================");
  console.log(`      ${time}`);
}

drawClock();
setInterval(drawClock, 1000);
