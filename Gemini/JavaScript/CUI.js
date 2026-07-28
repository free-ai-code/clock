// CUI.js

function updateConsoleClock() {
  // コンソール画面をクリア
  console.clear();

  const now = new Date();
  
  // 日付と時間のフォーマット
  const date = now.toLocaleDateString('ja-JP', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    weekday: 'short'
  });
  const time = now.toTimeString().split(' ')[0];

  console.log('====================');
  console.log(`   ${date}`);
  console.log(`   ${time}`);
  console.log('====================');
  console.log(' (Ctrl+C で終了)');
}

// 1秒ごとに実行
setInterval(updateConsoleClock, 1000);

// 初回実行
updateConsoleClock();
