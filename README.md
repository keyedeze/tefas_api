You can use this code to build a local api to take updated funding prices in tefas.
The code is working like the following steps;
1) "server.exe" should be started (you can also automatically start it for every time open your PC. In windows menu -> open run -> write "shell:startup" -> copy the server.exe in here)
   server.exe is worked by your PC on startup.
2) "server.exe" works as the following;
   -  Wait until apply the internet connection.
   -  Scrap tefas funding data and save it under "D:\\phyton\\scrap\\webscrapping\\" link as a json file.
     -  If it is not possible, do not update last scrapped json file.
   - Start a local server as "http://localhost:43560"
   - Whenever the server takes get request, it should read and return json data under the "D:\\phyton\\scrap\\webscrapping\\" link.
