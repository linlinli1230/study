package autofy;
//定时器
import java.text.DateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;


public class MyTimerTask {

    public static void main(String[] args) {
        MyTask myTask = new MyTask();
        myTask.startTask();
    }

    public static class MyTask {

        private Timer timer;
        private TimerTask task;

        public static final long period = 1000 * 3600 * 24;

        private void startTask() {
            timer = new Timer();
            task = new TimerTask() {
                @Override
                public void run() {
                    System.out.println("Hello World" + " - " + DateFormat.getDateTimeInstance().format(new Date()));
                }
            };
            Date date = getCustomTime(19);
            System.out.println(date);
            timer.schedule(task, date);
        }

        private Date getCustomTime(int hour) {
            int currentDate = Calendar.getInstance().get(Calendar.DAY_OF_MONTH);
            int currentHour = Calendar.getInstance().get(Calendar.HOUR_OF_DAY);
            Calendar calendar = Calendar.getInstance();
            calendar.set(Calendar.HOUR_OF_DAY, hour);
            if (hour < currentHour) {
                calendar.set(Calendar.DAY_OF_MONTH, currentDate + 1);
            }
            return calendar.getTime();
        }
    }
}
