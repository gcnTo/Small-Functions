total_hour = 2;
total_minutes = 2;
total_seconds = 10;

// Look up id to stop by hand. Use clearInterval(id)
const id = setInterval(() => {
  if (total_seconds === 0) {
    total_seconds = 60;
    total_minutes--;
  }
  if (total_minutes === 0) {
    total_minutes = 59;
    total_hour--;
  }

  total_seconds--;
  console.log(
    `${total_hour}:${total_minutes}:${total_seconds} left for breakdown.`
  );
}, 100);
