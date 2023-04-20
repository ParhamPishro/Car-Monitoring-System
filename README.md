# Car-Monitoring-System

🇬🇧 EN:

In this project, the goal is to store the movement path of the cars, replay the path traveled by them, their speed at any moment, display the origin and destination and the distance between them, coordinates and display the map.

The programming language is Python.

.

.

.

**Step 1) Create Dataset:** The dataset of this project consists of 10 separate routes traveled
by 10 different cars. Each route is a sequence of different points. In this data, it has been assumed that
we have 10 cars, each with a route including 3000 points.
Since each point represents a geographic location, to display it must used latitude and longitude.

In order to create the dataset, you must first create 10 different cars, each of which has a different name,
company, and year (this information must be entered by the user through the GUI);
Then the route of each car, which contains 3000 points, should be built (the longitude and latitude of the starting
point is entered by the user, and the other points should be built randomly).
The 10 created cars along with their route should be saved in a file called car-dataset.txt.
After the creation of the data, a message must be displayed to the user through the GUI
that the creation of the data is successful.


**Step 2) Playback:** In this section, the facilities provided to the user will include the following:
+ By clicking the Start button, the program starts reading the data file and displays one point of each car's route
every second.
+ By clicking the 2x button, the speed of displaying information will be doubled
(one point will be displayed every 0.5 seconds).
+ By clicking the 4x button, the speed of displaying information will be 4 times
(one point will be displayed every 0.25 seconds).
+ By clicking the 8x button, the speed of displaying information will be 8 times
(one point will be displayed every 0.125 seconds).
+ By clicking on the infinite button, the speed of displaying information reaches the maximum mode
(without stopping).
+ By clicking the Pause button, the reading of the points will stop.
+ By clicking the Restart button, the reading of the points will start from the beginning.
+ By clicking on the Map button, the distance traveled by the car between the origin and destination points
will be displayed.
+ information that will be displayed to the user; including car information, car coordinates
(longitude and latitude), the speed of the car at the moment ,the minimum and maximum speed of the car, the origin,
the destination, and the distance between them.

---

:iran: FA:

در این پروژه، هدف ذخیره مسیر حرکت خودروها، پخش مجدد مسیر طی شده توسط آن ها، سرعت آن ها در هر لحظه، نمایش مبدا و مقصد و فاصله بین آن ها، مختصات و نمایش نقشه است.

زبان برنامه نویسی پایتون می باشد.

.

.

.

**گام اول) ساخت مجموعه داده:** دادگان این پروژه از 10 مسیر مجزا که توسط 10 خودروی مختلف طی شده اند، تشکیل می شود.
هر مسیر دنباله ای از نقاط مختلف است. در این دادگان فرض بر این بوده است که ما 10 خودرو داریم که هر کدام مسیری
شامل 3000 نقطه را طی می کنند. از آنجا که هر نقطه نشان دهنده یک موقعیت جغرافیایی است، برای نمایش آن باید
از طول و عرض جغرافیایی استفاده کرد. 

به منظور ساخت دادگان باید ابتدا 10 خودروی مختلف که هر کدام نام، شرکت و سال ساخت
مختلفی دارند را ساخت (این اطلاعات باید توسط کاربر و از طریق رابط کاربری وارد شوند)؛ سپس مسیر هر خودرو که شامل 3000
نقطه است باید ساخته شود (طول و عرض جغرافیایی نقطه شروع توسط کاربر وارد شده و دیگر نقاط باید به صورت تصادفی
ساخته شوند). 10 خودروی ایجاد شده به همراه مسیر حرکت آن ها باید در یک فایل به نام car-dataset.txt ذخیره شوند.
پس از ساخت دادگان باید به کاربر پیامی مبنی بر موفقیت آمیز بودن ساخت دادگان از طریق رابط کاربری نمایش داده شود.

**گام دوم) بازپخش:** در این بخش امکاناتی که در اختیار کاربر قرار می گیرد، شامل موارد زیر خواهد بود:
+ با کلیک بر روی دکمه شروع، برنامه اقدام به خواندن فایل دادگان کرده و در هر ثانیه یک نقطه از مسیر هر خودرو را نمایش می دهد.
+ با کلیک بر روی دکمه 2 برابر، سرعت نمایش اطلاعات 2 برابر می شود (هر 0.5 ثانیه یک نقطه نمایش داده خواهد شد).
+ با کلیک بر روی دکمه 4 برابر، سرعت نمایش اطلاعات 4 برابر می شود (هر 0.25 ثانیه یک نقطه نمایش داده خواهد شد).
+ با کلیک بر روی دکمه 8 برابر، سرعت نمایش اطلاعات 8 برابر می شود (هر 0.125 ثانیه یک نقطه نمایش داده خواهد شد).
+ با کلیک بر روی دکمه بی نهایت، سرعت نمایش اطلاعات به بیشترین حالت برنامه (بدون توقف) می رسد.
+ با کلیک بر روی دکمه توقف، خواندن نقاط مربوط به مسیر خودروها متوقف خواهد شد.
+ با کلیک بر روی دکمه راه اندازی مجدد، فعالیت خواندن مسیر از ابتدا شروع خواهد شد.
+ با کلیک بر روی دکمه نقشه، مسافت طی شده توسط ماشین بین نقاط مبدا و مقصد نمایش داده خواهد شد.
+ اطلاعاتی که به کاربر نمایش داده خواهد شد؛ شامل اطلاعات ماشین، مختصات ماشین (طول و عرض جغرافیایی)،
سرعت ماشین در هر لحظه، حداقل و حداکثر سرعت ماشین، مبدا، مقصد و فاصله بین آن ها می باشد.
