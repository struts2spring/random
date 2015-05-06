
Installing ChromeDriver on Ubuntu

We use Cucumber for integration testing of SupportBee. While the scenarios run smoothly on the CI, but they sometimes fail randomly on the local setup with the below error.

` unable to obtain stable firefox connection in 60 seconds (127.0.0.1:7055) ` ` (Selenium::WebDriver::Error::WebDriverError) `
As you can see above, Firefox is to blame.

Some people have found a solution to this issue Stackoverflow, but I decided to give ChromeDriver a try, and it worked well.

I had to install ChromeDriver on Linux (Ubuntu 14.04.1 in my case) to make it work, here is how you can install it:

    Install Unzip

sudo apt-get install unzip

    Assuming you’re running a 64-bit OS, download the latest version of chromedriver from their website

wget -N http://chromedriver.storage.googleapis.com/2.10/chromedriver_linux64.zip -P ~/Downloads

unzip ~/Downloads/chromedriver_linux64.zip -d ~/Downloads

    Make the file you downloaded executable, and move it to /usr/local/share

chmod +x ~/Downloads/chromedriver

sudo mv -f ~/Downloads/chromedriver /usr/local/share/chromedriver

    Also, create symlinks to the chromedriver. Cucumber would look for the drivers in /usr/bin/chromedriver

sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver 
